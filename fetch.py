import sys
import json
from server.parser import url2dict

if __name__ == '__main__':
    try:
        url = sys.argv[1]
    except:
        print('INCORRECT USAGE\n')
        print('  Usage:')
        print('    python %s {url}' % sys.argv[0])
        sys.exit()

    tab_dict = url2dict(url, return_json=False)
    pretty_format_json = json.dumps(tab_dict, indent=4, sort_keys=True)
    print(pretty_format_json)
