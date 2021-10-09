import json
import requests
from bs4 import BeautifulSoup
from typing import Union

def taburl2dict(url: str, return_json=False) -> Union[dict, "json"]:
    '''
    Creates a dict/json object of guitar tab information given a url

    Parameters:
        - url: UG url to parse
        - return_json: Whether to return a json object or a python dictionary

    Returns:
        - Dictionary with the following attributes:
            {'title': str
             'rating': float
             'votes': int
             'version': int
             'description': str
             'url': str
             'lines': str}
    '''

    html_body = requests.get(url).content

    soup = BeautifulSoup(html_body, "html.parser")

    json_string = soup.html.body.find_all("div")[2].attrs["data-content"]

    # Separate Tab metadata from the tab sheet music
    data_content_json: dict = json.loads(json_string)
    tab_json_data: dict = data_content_json["store"]["page"]["data"]
    tab_music: str = tab_json_data["tab_view"]["wiki_tab"]["content"]
    tab_metadata: dict = tab_json_data["tab"]

    # Extract meaingful metadata
    info_dict = {
        'title': tab_metadata["song_name"],
        'rating': tab_metadata["rating"],
        'votes': tab_metadata["votes"],
        'version': tab_metadata["version"],
        'description': tab_metadata["version_description"],
        'url': tab_metadata['tab_url'],
        'lines': tab_music
    }

    # Return constructed json under a single tag
    if return_json:
        return json.dumps(info_dict, ensure_ascii=False)
    return info_dict
