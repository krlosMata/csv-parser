import sys, json, time, os
import xlrd, xlwt, numpy
from customApi import General, dataUtils
from pathlib import Path

###########################################
###################ARGS####################
###########################################
## Source folder to get products files
sourcePath = sys.argv[1]
## Destiny folder to save pruct files parsed
destinyPath = sys.argv[2]
## Output file type
outType = float(sys.argv[3])


###########################################
###########ARGS CONTROL ERROR##############
###########################################
# Check source folder exists
if os.path.exists(sourcePath) == False:
  print("Folder {} does not exists".format(sourcePath))
  sys.exit(0)

# Check destiny folder exists
if os.path.exists(destinyPath) == False:
  print("Folder {} does not exists".format(destinyPath))
  sys.exit(0)

# Check folder has data
if len(os.listdir(sourcePath)) == 0:
  print("There is no files on folder {}".format(sourcePath))
  sys.exit(0)

if outType not in [0,1]:
  print("Output type is out of range")
  sys.exit(0)

###########################################
###############START PARSER################
###########################################
folderObject = Path(sourcePath)
destinyObject = Path(destinyPath)
numMatrix = 0
## Get number of total matrix. We take length of X vector
for product in folderObject.iterdir():
  pr = (product.name).replace('.json','')
  matrix = General.read_json(product)
  colX = dataUtils.getColumn(matrix, 0)
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

if outType == 0:
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
elif outType == 1:
## Build matrix sorted by time
  ultraMatrix = []
  for product in fileList:
    filePath = folderObject.joinpath(product)
    rowMatrix = []
    prName = product.replace('-final.json','') 
    prMatrix = General.read_json(filePath)
    for row in prMatrix:
      row.insert(1, prName)
      ultraMatrix.append(row)

## Save file
nameFile = destinyObject.joinpath('ultraMatrix.json')
General.write_json(ultraMatrix,nameFile)
print("Final matrix done !!")