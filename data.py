# Import YAML module

import yaml

# Load YAML data from the file

with open('items.yaml') as file:

    read_data = yaml.load(file, Loader=yaml.FullLoader)

print('This sentence is output to the screen')
