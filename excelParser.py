import sys, json, time, os
import xlrd, xlwt
import numpy as np
from customApi import General, chemistryUtils
from pathlib import Path

###########################################
###################ARGS####################
###########################################
filePath = sys.argv[1]

###########################################
###########ARGS CONTROL ERROR##############
###########################################
if os.path.exists(filePath) == False:
  print("El archivo {} no existe".format(filePath))
  sys.exit(0)

###########################################
#############GLOBAL VARABLES###############
###########################################
currentPath = Path.cwd()
arrayMatrix = {}

## Get Excel data
fullExcel = xlrd.open_workbook(filePath)
## Get sheet by name
fullSheet = fullExcel.sheet_by_name('2014')
## Get Headers
headers = fullSheet.row(0)
## Get Cell objects of column X
columnProduct = fullSheet.col(2)
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
  ## Get headers
  if index == 0:
    headers.append(fullSheet.row(index))
  ## Pre - filters
  # Filter short name on column C and 0 value on column G
  if len(str(colName.value)) < 10 or fullSheet.row(index)[6].value == 0 :
    index += 1
    continue  
  # If the product is new, save product name
  if productName == '':
    productName = colName.value
  # Add entire row to product
  matrixProduct.append(fullSheet.row(index))
  index += 1
  # If product is changed, save current product matrix into an array and start next one
  if colName.value != productName:
    arrayMatrix[productName] = matrixProduct
    productName = colName.value
    matrixProduct = []

## Columns to be skipped
skipCols = [1, 2, 3, 4, 5, 25, 26, 27, 28, 29]

## Save json for each product
for product in arrayMatrix:
  newMatrix = chemistryUtils.convert(arrayMatrix[product], skipCols)
  nameFile = currentPath.joinpath('products').joinpath(str(product) + '.json')
  General.write_json(newMatrix,nameFile)

print("Csv file parsed and exported correctly")