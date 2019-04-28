import json, sys, os, time
from pathlib import Path

## Insert path to json file
pathJson = str(sys.argv[1])

###########################################
###########ARGS CONTROL ERROR##############
###########################################
if os.path.exists(pathJson) == False:
  print("The file {} does not exist".format(pathJson))
  sys.exit(0)

## Read Json file
def read_json(file):
  with open(str(file)) as conf_file:
    var = json.load(conf_file)
  return var

## Open Csv file
def openCsv(path):
  try:
    fileObject = open(str(path), mode = 'a+')
    return fileObject
  except Exception as e:
    line = sys.exc_info()[-1].tb_lineno
    print('Exception in line: {}\n {}'.format(line,e), flush=True)

## Write Csv file
def writeCsv(path,message):
  try:
    streamIO = openCsv(path)
    streamIO.write(message + '\n')
    streamIO.close()
  except Exception as e:
    line = sys.exc_info()[-1].tb_lineno
    print('Exception in line: {}\n {}'.format(line,e), flush=True)

## Create path for csv file
pathCsv = pathJson.replace('.json','.csv')

dataJson = read_json(pathJson)
for element in dataJson:
  stringElement = ((str(element)).replace('[','')).replace(']','')
  writeCsv(pathCsv, stringElement)
