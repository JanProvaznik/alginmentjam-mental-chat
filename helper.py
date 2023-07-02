import json

# Read the JSON file
with open('/home/janpro/alignmenjam/alignmentjam/data/questions/schizophrenia_2023-07-01_22-08-237.json') as file:
    data = json.load(file)

# Create a dictionary to map existing IDs to new IDs
id_map = {obj['id']: index for index, obj in enumerate(data)}

# Update the IDs in the objects
for obj in data:
    obj['id'] = id_map[obj['id']]

# Write the updated JSON to a new file
with open('fixed.json', 'w') as file:
    json.dump(data, file)
