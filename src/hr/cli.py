import argparse
def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='the path to the export file')
    parser.add_argument('--format', default='json', choices=['json', 'csv'], type=str.lower)
    return parser

def main():
    import sys
    from hr import export_csv, export_json, users
    from hr import users as u
    args = create_parser().parse_args()
    users = u.fetch_users()
    if args.path:
        file = open(args.path, 'w', newline='')
    else:
        file = sys.stdout
    if args.format == 'json':
        export_json.to_json_file(file, users)
    else:
        export_csv.to_csv_file(file, users)
