# Import YAML module

import yaml

# Load YAML data from the file

with open('items.yaml') as file:

    read_data = yaml.load(file, Loader=yaml.FullLoader)

# Print YAML data before sorting

print(read_data)

# Sort YAML data based on keys

sorted_data = yaml.dump(read_data)

# Print YAML data after sorting

print(sorted_data)
