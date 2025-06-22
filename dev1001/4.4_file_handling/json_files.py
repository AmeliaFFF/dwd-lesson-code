import json

# Read
with open('config.json') as f:
    data = json.load(f) # Parses JSON into Python dict/list
    # print(type(data))
    print(f'Username: {data['username']}')
    print(f'Recent files: {data['recent_files'][0]}')

# Modifying the in-memory Python data structures.
data['recent_files'].append('new_file.txt')

# Write
with open('update_config.json', 'w') as f:
    json.dump(data, f, indent=4)