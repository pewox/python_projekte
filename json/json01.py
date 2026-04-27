import json
import yaml
data = {
    "vname": "peter",
    "name": "wo",
    "adresse": ["eyba", 47, 68231, {"wohn": {"ort" : "kuzenhausen", "home": "bunker","etage": 2}}],
    "alter": 77
}
with open("data.json", "w") as f:
    json.dump(data, f,sort_keys=False)

print(json.dumps(data))

with open('data.yaml', 'w') as f:
    yaml.dump(data,f, sort_keys=False)
print(yaml.dump_all(data))