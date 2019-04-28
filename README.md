# csv-parser
Specific csv parser and data processing

## Considerations
- This code is writen from scratch and it has the aim to match very specific requirements. Other python modules to process data could be used instead.
- Very basic input errors has been take into account
- Python version used: Python 3.5.2
- Dependencies:
  ```
  import sys, json, time, os
  import xlrd, xlwt
  import numpy as np
  from pathlib import Path
  ```
## Basic Usage
Basically, it is intended to load data from an `.csv` file into `.json` given a separation for a concrete `.csv` column. Once we have all the `.csv` separated into different `.json` objects, we can start data processing.
The objective is achieving all variables having the same length and values. That is reached applying a simple linear interpolation and normalization afterwards. Once we have all data correctly processed, we build a `.txt` file to be easily portable to external software.
As an example, it has been written a script for an specific software ( Matlab ) in order to decode `.txt` file.   

### 1
Load `.csv` file
`python3 excelParser.py #sourceFile #nameSheet #MainColumn #destinyPath`

### 2
Data interpolation and normalizaton
`python3 productParser.py #sourcePath #destinyPath`

### 3
Organize data into `.txt` fil to be portable into external software
`pyhon3 restructureMatrix #sourcePath #destinyPath #OutputType`

`#OutputType` --> [0, 1]
Represnts two different approaches at the time to restructure data
- 0 --> Each matrix represents one time slot. Hence, all products are stored in one matrix which represents one time slot
- 1 --> Each matrix represents one product. Hence, one product is represented with its data in one matrix