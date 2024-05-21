import json

def to_json_file(export_file, users):
    json.dump(users, export_file, indent=4)
    export_file.close()
