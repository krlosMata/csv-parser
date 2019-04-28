import sys, json, time, os
import xlrd, xlwt
import numpy as np
from customApi import General, dataUtils
from pathlib import Path

###########################################
###################ARGS####################
###########################################
sourceFile = sys.argv[1]
nameSheet = sys.argv[2]
columnSelected = sys.argv[3]
destinyPath = sys.argv[4]

###########################################
###########ARGS CONTROL ERROR##############
###########################################
if os.path.exists(sourceFile) == False:
  print("The file {} does not exist".format(sourceFile))
  sys.exit(0)

if os.path.exists(destinyPath) == False:
  print("The path {} does not exist".format(destinyPath))
  sys.exit(0)

###########################################
#############GLOBAL VARABLES###############
###########################################
destinyObjectPath = Path(destinyPath)
arrayMatrix = {}

## Get Excel data
fullExcel = xlrd.open_workbook(sourceFile)
## Get sheet by name
fullSheet = fullExcel.sheet_by_name(nameSheet)
## Get Headers
headers = fullSheet.row(0)
## Get Cell objects of column 'columnSelected'
columnProduct = fullSheet.col(columnSelected)
columnProduct.pop(0)

###########################################
#########GET MATRIX EACH PRODUCT###########
###########################################
index = 1
productName = ''
matrixProduct = []
headers = []
## Get matrix for each product
for colName in columnProduct: 
  # If the product is new, save product name
  if productName == '':
    productName = colName.value
  # If product is changed, save current product matrix into an array and start next one
  if colName.value != productName:
    arrayMatrix[productName] = matrixProduct
    productName = colName.value
    matrixProduct = []
  # Add entire row to product
  matrixProduct.append(fullSheet.row(index))
  index += 1

## Columns to be skipped
# Enter which columns of 'csv' have to be skipped
# If it is empty, all columns are saved
skipCols = []

## Save json for each product
for product in arrayMatrix:
  newMatrix = dataUtils.convert(arrayMatrix[product], skipCols)
  nameFile = destinyObjectPath.joinpath(str(product) + '.json')
  General.write_json(newMatrix,nameFile)

print("Csv file parsed and saved correctly")