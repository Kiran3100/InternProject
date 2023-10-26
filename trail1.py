import yaml
from pprint import pprint

# Read the file outside the class and pass the data to the Parser class
def load_yaml_file(file_path):
    global raw_data 
    try:
        with open(file_path, 'r') as yaml_file:
            raw_data = yaml.safe_load(yaml_file)
        return raw_data
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")

class Parser:
    # Parser should take “data” as input.
    def __init__(self,raw_data) -> None:
        self.listkeys = [k for k in raw_data]
        print(self.listkeys)

    # Parser class should have instance methods to get
    # 	Info
    # 	Servers
    # 	Paths
    # 	Components

    def info(self):
        global info_data
        info_data = None
        for x,y in raw_data.items():
            if x == "info":
                info_data = y
        print("Info data in the yaml file : \n")
        return info_data
    
    def servers(self):
        global servers_data
        servers_data = None
        for x,y in raw_data.items():
            if x == "servers":
                servers_data = y
        print("Servers data in the yaml file : \n")
        return servers_data
    
    def paths(self):
        global paths_data
        paths_data = None
        for x,y in raw_data.items():
            if x == "paths":
                paths_data = y
        print("Paths data in the yaml file : \n")
        return paths_data  
     
    def components(self):
        global components_data
        components_data = None
        for x,y in raw_data.items():
            if x == "components":
                components_data = y
        print("Components data in the yaml file : \n")
        return components_data
    
    # Process the “schema” from the components.
    # Make a schema data structure.
    def schemas_components(self):
        global schema
        schema = {}
        for i,j in components_data.items():
            schema[i] = [k for k in j]  
        return schema
    
    # See if path contains “parameters” child.  Print path, it should print if it contains “parameters” child.
    def path_para(self):
        global path_dict
        path_dict = {}
        self.paths = {}
        for i,j in paths_data.items():
            self.paths[i] = {"methods" :[k for k in j]}
        path_dict['paths'] = self.paths
        return path_dict



yaml_file_path = "D:/YamlProject/banking.yml"
yaml_data = load_yaml_file(yaml_file_path)

# Parser class should instantiate the “object”.
p = Parser(yaml_data)
print("")

# Calling these instance methods should print the respective data.

print(p.info())
print("")

print(p.servers())
print("")

print(p.paths())
print("")

print(p.components())
print("")

print(p.schemas_components())
print("")

print(p.path_para())


