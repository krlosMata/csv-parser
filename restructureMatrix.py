import sys, json, time, os
import xlrd, xlwt, numpy
from customApi import General, chemistryUtils
from pathlib import Path

###########################################
###################ARGS####################
###########################################
## Source folder to get products files
folderPath = sys.argv[1]
## Destiny folder to save pruct files parsed
destinyPath = sys.argv[2]

###########################################
###########ARGS CONTROL ERROR##############
###########################################
# Check source folder exists
if os.path.exists(folderPath) == False:
  print("El directorio {} no existe".format(folderPath))
  sys.exit(0)

# Check destiny folder exists
if os.path.exists(destinyPath) == False:
  print("El directorio {} no existe".format(folderPath))
  sys.exit(0)

# Check folder has data
if len(os.listdir(folderPath)) == 0:
  print("No hay archivos en el directorio {}".format(folderPath))
  sys.exit(0)

###########################################
###############START PARSER################
###########################################
folderObject = Path(folderPath)
destinyObject = Path(destinyPath)
numMatrix = 0
## Get number of total matrix. We take length of X vector
for product in folderObject.iterdir():
  pr = (product.name).replace('.json','')
  matrix = General.read_json(product)
  colX = chemistryUtils.getColumn(matrix, 0)
  numMatrix = len(colX)-1
  break

## Sort files name by ascending order
fileSort = []
# Save all product names, type all float
for product in folderObject.iterdir():
  prStr = (product.name).replace('-final.json','')
  fileSort.append(float(prStr))
# Sort list ascending order
fileSort.sort()
# Build file list again
fileList = [str(element).replace('.0','')+'-final.json' for element in fileSort]



## Build matrix sorted by number of product
ultraMatrix = []
for index in range(0, numMatrix + 1): ## For each timestamp, build a matrix
  for product in fileList:
    filePath = folderObject.joinpath(product)
    rowMatrix = []
    prName = product.replace('-final.json','')
    prMatrix = General.read_json(filePath)
    rowMatrix = prMatrix[index]
    rowMatrix.insert(1, prName)
    ultraMatrix.append(rowMatrix)

## Build matrix sorted by time
# ultraMatrix = []
# for product in fileList:
#   filePath = folderObject.joinpath(product)
#   rowMatrix = []
#   prName = product.replace('-final.json','') 
#   prMatrix = General.read_json(filePath)
#   for row in prMatrix:
#     row.insert(1, prName)
#     ultraMatrix.append(row)

nameFile = destinyObject.joinpath('ultraMatrix.json')
General.write_json(ultraMatrix,nameFile)
print("Final matrix done !!")