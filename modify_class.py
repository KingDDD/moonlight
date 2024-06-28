import argparse
import json
import os

def modify_json_files(directory, classname_to_modify, new_class):
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError as e:
                    print(f"Error loading {filename}: {e}")
                    continue
            
            # Modify the specified element
            if classname_to_modify in data:
                data[clasname_to_modify] = new_class
            else:
                print(f"Class '{classname_to_modify}' not found in {filename}")
                continue
            
            # Write the changes back to the file
            with open(filepath, 'w') as file:
                json.dump(data, file, indent=4) # may need different indentation
                print(f"Modified '{classname_to_modify}' in file {filename}")

if __name__ == "__main__":
   parser = argparse.ArgumentParser(description="Modify a specified element in JSON files in a directory.")
   parser.add_argument("directory", type=str, help="The directory containing JSON files.")
   parser.add_argument("element", type=str, help="The element key to modify.")
   parser.add_argument("value", type=str, help="The new value for the element.")

   args = parser.parse_args()

   modify_json_files(args.directory, args.element, args.value)

# python modify_json_files.py <directory> <element> <value>

