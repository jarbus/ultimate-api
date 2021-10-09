from server import app
from flask import request, jsonify
from urllib.parse import urlparse
from .parser import url2dict


SUPPORTED_UG_URI = 'tabs.ultimate-guitar.com'

@app.route('/')
def index():
    return 'hi'

@app.route('/tab')
def tab():
    try:
        ultimate_url = request.args.get('url')

        # Ensure sanitized url
        parsed_url = urlparse(ultimate_url)
        location = parsed_url.netloc
        if location != SUPPORTED_UG_URI:
            raise Exception('unsupported url scheme')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    tab_dict = url2dict(ultimate_url, return_json=True)
    return jsonify(tab_dict)
