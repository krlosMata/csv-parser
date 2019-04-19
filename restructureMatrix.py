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

ultraMatrix = []

for index in range(0, numMatrix): ## For each timestamp, build a matrix
  unitMatrix = []
  for product in folderObject.iterdir(): ## For each product
    productMatrix = General.read_json(product)
    rowUnitMatrix = []
    for i in range(1, len(productMatrix[0])): ## For each variable
      colY = chemistryUtils.getColumn(productMatrix, i)
      rowUnitMatrix.append(colY[index])
    unitMatrix.append(rowUnitMatrix)
  ultraMatrix.append(unitMatrix)

nameFile = destinyObject.joinpath('ultraMatrix.json')
General.write_json(ultraMatrix,nameFile)
print("Final matrix done !!")