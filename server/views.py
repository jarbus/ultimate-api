from server import app
from flask import request, jsonify
from urllib.parse import urlparse
from .parser import taburl2dict, exploreurl2taburls


SUPPORTED_TAB_URI = 'tabs.ultimate-guitar.com'
SUPPORTED_EXPLORE_URI = 'www.ultimate-guitar.com'

def validate_url(supported_uri, url):
    parsed_url = urlparse(url)
    location = parsed_url.netloc
    if location != supported_uri:
        raise Exception('unsupported url scheme')

@app.route('/')
def index():
    return 'hi'

@app.route('/tab')
def tab():
    try:
        ug_url = request.args.get('url')
        validate_url(SUPPORTED_TAB_URI, ug_url)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    tab_dict = taburl2dict(ug_url, return_json=True)
    return jsonify(tab_dict)

@app.route('/explore')
def explore():

    try:
        ug_url = request.args.get('url')
        validate_url(SUPPORTED_EXPLORE_URI, ug_url)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    tabs_dict = exploreurl2taburls(ug_url, return_json=True)
    return jsonify(tabs_dict)
