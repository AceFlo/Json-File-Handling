import json
import os

filename = "self.file_name.json"
if os.path.exists(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    old_key="Name"
    new_key="Full Name"
    if old_key in data:
        data[new_key]=data.pop(old_key)
    with open("self.file_name.json", "w")as f:
        json.dump(data,f,indent=4,sort_keys=False)

    print(f"Key name {old_key} has been changed to {new_key}")
    print(f"Key names in '{filename}' have been updated successfully.")
else:
    print(f"The file '{filename}' does not exist.")



