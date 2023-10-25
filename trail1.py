import yaml
from pprint import pprint
def load_yaml_file(file_path):
    try:
        print(file_path)
        with open(file_path, 'r') as yaml_file:
            raw_data = yaml.safe_load(yaml_file)
        return raw_data
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")

yaml_file_path = "D:/YamlProject/banking.yml"
yaml_data = load_yaml_file(yaml_file_path)

if yaml_data:
    print("YAML data as Python data structures:")
    print("")
    pprint(yaml_data)

# listkeys = [k for k in yaml_data]
# print(listkeys)

