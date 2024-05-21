# First we need to import the packages we'll need from the standard library:
import json

# This section deals with exporting to JSON. First we'll create and define
# a function called to_json_file. It will take the user data from the fetch_users
# function

def to_json_file(export_file, users):

    # And then it will dump it out (it will look nice with the indent=4 we're specifying)
    json.dump(users, export_file, indent=4)

    # Then we'll close the export file
    export_file.close()
