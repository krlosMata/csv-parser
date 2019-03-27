import urllib.request
import json
import os

# Funció general per afagar dades d'una API
def GetApi(_stringApi):
    req = urllib.request.Request(_stringApi, headers={'User-Agent': 'Mozilla/5.0'})   
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
    return data

# Llegir arxiu Json
def read_json(arxiu):
  if os.path.isfile(str(arxiu)) == False:
    return []
  with open(str(arxiu)) as conf_file:
    variable = json.load(conf_file)
  return variable

# Escriure arxiu Json
def write_json(variable, arxiu):
  with open(str(arxiu), 'w+') as conf_file:
    json.dump(variable,conf_file)

# ReadJsonArray
def openJsonArray(path):
  if os.path.isfile(str(path)) == False:
    return []
  fileObject = open(str(path))
  variable = json.load(fileObject)
  return variable

# writeJsonArray
def writeJsonArray(array, arxiu):
  fileObject = open(str(arxiu), 'w+')
  json.dump(array,fileObject)

# addJsonArray
def addJsonArray(path,message):
  try:
    # Open Json
    jsonArray = openJsonArray(path)
    # Add data to array
    jsonArray.append(message)
    # Save json
    writeJsonArray(jsonArray, path)
  except Exception as e:
    line = sys.exc_info()[-1].tb_lineno
    print('Exception in line: {}\n {}'.format(line,e), flush=True)
    print(Back.RED + 'Error while adding data to json' + Style.RESET_ALL)