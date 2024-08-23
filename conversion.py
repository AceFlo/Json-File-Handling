import json

filename = 'myfile.txt'
output_filename = 'test1.json'

dict1 = {}

with open(filename) as fh:
    for line in fh:
        parts = line.strip().split(None, 1)
        if len(parts) == 2:
            command, description = parts
            dict1[command] = description.strip()


with open(output_filename, "w") as out_file:
    json.dump(dict1, out_file, indent=4, sort_keys=True)




