import sys, json, time, os
from customApi import General
from pathlib import Path

###########################################
################General####################
###########################################
def arrayToFloat(array):
  typeOf = type(array[0])
  if typeOf == type(''):
    arrayMod = [x.replace(',', '.') for x in array]
    arrayFloats = [(float(x)) for x in arrayMod]
    return arrayFloats
  return array

def convert(matrix):
  outputTotal = []
  for element in matrix:
    outputRow = []
    for x in element:
      if x.ctype != 0:
        outputRow.append(x.value)
    outputTotal.append(outputRow)
  return outputTotal

def getColumn(matrix, col):
  colData = []
  for element in matrix:
    colData.append(element[col])  
  return colData


###########################################
############FUNCTIONS NORM#################
###########################################
## Returns normalization of vector in [0, 1] range
def normalizationVector(inputVec):
  output = []
  baseElement = float(inputVec[0])
  baseVec = [(float(x) - baseElement) for x in inputVec]
  normElem = baseVec[len(baseVec)-1]
  for element in baseVec:
    output.append(float(element/normElem))
  return output

def getTramo(x, tabla):
  for i in range(len(tabla)-1):
    if (x >= tabla[i]['init']) and (x <= tabla[i+1]['init']):
      return i
  return i + 1

def interpolation(tabla, step):
  xOut = range(0, 101, step)
  xOut = [x/100 for x in xOut]
  yOut = []
  for x in xOut:
    tramo = getTramo(x, tabla)
    y = tabla[tramo]['pendiente']*x + tabla[tramo]['ordenada']  
    yOut.append(y)
  return xOut, yOut

def getTabla(xVec, yVec):
  tabla = []
  lenTramos = len(xVec) - 1
  tramos = range(1, lenTramos + 1)
  for i in tramos:
    elemTabla = {}
    xM = xVec[i] - xVec[i-1]
    yM = yVec[i] - yVec[i-1]
    m = yM / xM
    n = yVec[i] - m * xVec[i]
    numTramo = i - 1
    elemTabla['numTramo'] = numTramo
    elemTabla['pendiente'] = m
    elemTabla['ordenada'] = n
    elemTabla['init'] = xVec[i-1]
    tabla.append(elemTabla)
  return tabla