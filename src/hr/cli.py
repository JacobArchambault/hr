import sys
from hr import export_csv, export_json, users, parser
from hr import users as u

def main():
    args = parser.create_parser().parse_args()
    users = u.fetch_users()
    if args.path:
        file = open(args.path, 'w', newline='')
    else:
        file = sys.stdout
    if args.format == 'json':
        export_json.to_json_file(file, users)
    else:
        export_csv.to_csv_file(file, users)
