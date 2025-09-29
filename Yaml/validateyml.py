# pip install pyyaml
import yaml
with open('myfile.yaml','r') as file:
    try:
        print(yaml.safe_load(file))
    except yaml.YAMLError as exc:
        print(exc)