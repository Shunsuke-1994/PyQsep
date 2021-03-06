import pandas as pd 
from scipy import interpolate

def load_report(path_to_report):
    df = pd.read_excel(path_to_report).iloc[:, 4:]
    for i, row in df.iterrows():
        if row[0] == "No":
            row_start = i
            break

    report = df.iloc[row_start+1:, :]
    report.columns = df.iloc[row_start, :]
    report = report.reset_index(drop=True)
    report = report[["No", "Time\n(sec.)", "RFU", "PeakArea", "bp", 'PeakStart\n(sec.)', 'PeakEnd\n(sec.)']]
    report = report[[str(bp).isnumeric() for bp in report["bp"]]].dropna(axis = 0)
    report["bp"] = report["bp"].apply(lambda x: float(x.replace(",", "")))
    report["Time\n(sec.)"] = report["Time\n(sec.)"].apply(lambda x: float(x))
    return report

def load_rawdata(path_to_rawdata):
    return pd.read_csv(path_to_rawdata)

def get_interp(report):
    return interpolate.interp1d(report["Time\n(sec.)"], report["bp"], fill_value='extrapolate')

def get_tidy_data(rawdata, interp):
    rawdata["bp_esti"] = interp(rawdata.Time)
    return rawdata[["Time", "Signal", "bp_esti"]]


if __name__ == "__main__":
    import argparse
    import os
    import pandas as pd 

    parser = argparse.ArgumentParser()
    parser.add_argument("--signal", required = True)
    parser.add_argument("--report", required = True)
    parser.add_argument("-o", "--output")
    parser.add_argument("--suffix", default = "_bp")
    args = parser.parse_args()

    rawd = load_rawdata(args.signal)
    repo = load_report(args.report)
    interp = get_interp(repo)
    if args.output:
        outname = args.output
    else:
        outname = os.path.splitext(os.path.basename(args.signal))[0] + args.suffix + ".csv"

    get_tidy_data(rawd, interp).to_csv(outname)


