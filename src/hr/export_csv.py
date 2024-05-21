import csv

def to_csv_file(export_file, users):
    export_file.write('name,id,home,shell\n')
    csv.writer(export_file).writerows([[user['name'], user['id'], user['home'], user['shell']] for user in users])
    export_file.close()
