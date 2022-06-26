# PyQsep
a Python script for Qsep100 files.
Generates signal-time csv data.
input:
    - raw signal data(csv)
    - report file (xlsx)
output:
    - csv file containing time/signal/estimated bp

# Requirements
- scipy >1.2.1
- pandas

# Usage
```
python PyQsep.py --signal example/signal.csv --report example/report.xlsx --output example/test.csv
```

# Author
Shunsuke Sumi
