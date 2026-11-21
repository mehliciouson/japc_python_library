import json
from datetime import datetime, date



def converter(obj):
    #Pandas part
    if hasattr(obj, "to_dict") and callable(obj.to_dict):
        return obj.to_dict(orient="records")
    #numpy part
    if  hasattr(obj, "item") and callable(obj.item):
        return obj.item()

    #custom classes
    if hasattr(obj, "__dict__"):
        return obj.__dict__

    #sets and tuples
    if isinstance(obj, (set, tuple)):
        return list(obj)

    #dates and timestamps
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()

    #fallback to text
    return str(obj)

def tojson(anything, indent=4):
    return json.dumps(anything,default=converter, indent=indent)

def savejson(anything, filename="output.json", indent=4):
    with open(filename, "w") as f:
        f.write(tojson(anything,indent=indent))

def fromjson(json_string):
    return json.loads(json_string)

def loadjson(filename="output.json"):
    with open(filename, "r") as f:
        return json.load(f)

class autojson:
    def tojson(self, indent=4):
        return tojson(self, indent=indent)

    def savejson(self, filename="output.json", indent=4):
        savejson(self, filename,indent=indent)