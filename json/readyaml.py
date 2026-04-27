import yaml
import json

with open('data.yaml', 'r') as f:
    out = yaml.safe_load(f)
print(out)
print(type(f))