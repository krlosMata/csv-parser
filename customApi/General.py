import json, os

def read_json(arxiu):
  if os.path.isfile(str(arxiu)) == False:
    return []
  with open(str(arxiu)) as conf_file:
    variable = json.load(conf_file)
  return variable

def write_json(variable, arxiu):
  with open(str(arxiu), 'w+') as conf_file:
    json.dump(variable,conf_file)