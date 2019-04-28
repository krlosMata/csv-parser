import json, os

def read_json(file):
  if os.path.isfile(str(file)) == False:
    return []
  with open(str(file)) as conf_file:
    var = json.load(conf_file)
  return var

def write_json(var, file):
  with open(str(file), 'w+') as conf_file:
    json.dump(var,conf_file)