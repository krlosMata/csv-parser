import sys, json, time, os
import xlrd, xlwt
from customApi import General, chemistryUtils
from pathlib import Path

###########################################
###################ARGS####################
###########################################
folderPath = sys.argv[1]

###########################################
###########ARGS CONTROL ERROR##############
###########################################
# Check folder exists
if os.path.exists(folderPath) == False:
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
for product in folderObject.iterdir():
    matrix = General.read_json(product)
    colX = chemistryUtils.getColumn(matrix, 0)
    colY = chemistryUtils.getColumn(matrix, 7)
    colX = chemistryUtils.arrayToFloat(colX)
    colY = chemistryUtils.arrayToFloat(colY)
    normX = chemistryUtils.normalizationVector(colX)
    # Ok until here
    tabla = chemistryUtils.getTabla(normX, colY)
    finalX, finalY = chemistryUtils.interpolation(tabla, 2)
    Ycomp = [colY, finalY]
    test = 1
    test = test + 1