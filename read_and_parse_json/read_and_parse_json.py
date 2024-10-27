import json
def read_and_parse_json(path):
    with open(path, 'r') as file:
        return json.load(file)


