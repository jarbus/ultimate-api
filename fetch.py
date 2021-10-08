import sys
import json
from server import tab_parser

if __name__ == '__main__':
    try:
        url = sys.argv[1]
    except:
        print('INCORRECT USAGE\n')
        print('  Usage:')
        print('    python %s {url}' % sys.argv[0])
        sys.exit()

    json_data = tab_parser.json_from_ultimate_tab(url)

    pretty_format_json = json.dumps(json.loads(json_data), indent=4, sort_keys=True)
    print(pretty_format_json)
