import json 
import yaml

with open('inv.yaml', 'r') as f:
    d = yaml.safe_load(f)
print(d)

a = yaml.dump(d)
print(a)

print(repr(d))