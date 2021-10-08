import sys
import json
import requests
from .parser import html_tab_to_json_dict

def dict_from_ultimate_tab(url: str) -> json:
    '''
    Given a Ultimate Guitar tab url, will return a dictionary representing the
    song along with the song info
    '''
    html = requests.get(url).content
    tab_dict = html_tab_to_json_dict(html)
    return tab_dict


def json_from_ultimate_tab(url: str) -> json:
    '''
    Given a Ultimate Guitar tab url, will return a json object representing the
    song along with the song info
    '''
    tab_dict = dict_from_ultimate_tab(url)
    data = json.dumps(tab_dict, ensure_ascii=False)
    return data
