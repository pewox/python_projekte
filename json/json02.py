import json

with open("data.json", "r") as f:
    ausgabe = json.load(f)

print(ausgabe)
print(ausgabe['vname'],'\n', ausgabe['adresse'][0]) 