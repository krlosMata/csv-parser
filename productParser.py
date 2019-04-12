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
## For each product
for product in folderObject.iterdir():
    FinalMatrix = []
    ArrayYVectors = []
    matrix = General.read_json(product)
    colX = chemistryUtils.getColumn(matrix, 0)
    colX = chemistryUtils.arrayToFloat(colX)
    normX = chemistryUtils.normalizationVector(colX) # Normalize X vector of time
    ## Calculate all Yvec interpolated ( Skip X vector )
    for i in range(1, len(matrix[0])):
      colY = chemistryUtils.getColumn(matrix, i)
      colY = chemistryUtils.arrayToFloat(colY)
      tabla = chemistryUtils.getTabla(normX, colY) # Get interpolation table
      finalX, finalY = chemistryUtils.interpolation(tabla, 2) # Get Yvec interpolated from Xvec points
      ArrayYVectors.append(finalY)
    # Build matrix final for an specific product 
    for i in range(0, len(finalX)):
      RowFinalMatrix = []
      RowFinalMatrix.append(finalX[i])
      for vecY in ArrayYVectors:
        RowFinalMatrix.append(vecY[i])
      FinalMatrix.append(RowFinalMatrix)

test = 1
test = test + 1      
#TODO: Extraer matriz full normalizada a partir de: VecX y ArraydeVecY 

## Example getting one column X and Y
# for product in folderObject.iterdir():
#     matrix = General.read_json(product)
#     colX = chemistryUtils.getColumn(matrix, 0)
#     colY = chemistryUtils.getColumn(matrix, 7)
#     colX = chemistryUtils.arrayToFloat(colX)
#     colY = chemistryUtils.arrayToFloat(colY)
#     normX = chemistryUtils.normalizationVector(colX)
#     # Ok until here
#     tabla = chemistryUtils.getTabla(normX, colY)
#     finalX, finalY = chemistryUtils.interpolation(tabla, 2)
#     Ycomp = [colY, finalY]
#     test = 1
#     test = test + 1