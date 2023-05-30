import json

def read_json(file):
    f=open(file)
    data=json.load(f)
    return data
def write_json(file,data):
    f=open(file,"w")
    json.dump(data,f,indent=3)
    print("data saved succesfully !!")