# PyQsep
a Python script for parsing Qsep100(DNA Fragment Analyzer from BiOptics inc.) files.  
Generates signal-time csv data by interpolating peak-time relation.  
input:  
    - raw signal data(csv)  
    - report file (xlsx)  
output:  
    - csv file containing time/signal/estimated bp  

# Version
0.2

# Requirements
- scipy >1.2.1
- pandas

# Usage
```
python pyqsep.py --signal example/signal.csv --report example/report.xlsx --output example/test.csv
```

# TODO
- upate to applicable to various running modes.  
- batch processing.  


# Author
Shunsuke Sumi