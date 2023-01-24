import json

json_string = '{"first_name": "Guido", "last_name": "Rossum"}'
print(json_string)
print(type(json_string))

json_dict = json.loads(json_string)
print(json_dict)
print(type(json_dict))
print(json_dict.keys())

d = {
    "first_name": "Guido",
    "last_name": "Rossum",
    "titles": ['BDFL', 'Developer']
}

d_json = json.dumps(d)
print(d_json)
print(type(d_json))
