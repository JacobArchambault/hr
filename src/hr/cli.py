import sys
from hr import export_csv, export_json, users, parser
from hr import users as u

def main():
    args = parser.create_parser().parse_args()
    users = u.fetch_users()
    file = open(args.path, 'w', newline='') if args.path else sys.stdout
    if args.format == 'json':
        export_json.to_json_file(file, users)
    else:
        export_csv.to_csv_file(file, users)
