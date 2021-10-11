import re
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
        Dictionary/json with the following attributes:
            - 'title': str
            - 'rating': float
            - 'votes': int
            - 'version': int
            - 'description': str
            - 'url': str
            - 'lines': str
    '''

    html_body: bytes = requests.get(url).content

    soup: BeautifulSoup = BeautifulSoup(html_body, "html.parser")

    json_string: str = soup.html.body.find_all("div")[2].attrs["data-content"]

    # Separate Tab metadata from the tab sheet music
    data_content_json: dict = json.loads(json_string)
    tab_json_data: dict = data_content_json["store"]["page"]["data"]
    tab_music: str = tab_json_data["tab_view"]["wiki_tab"]["content"]
    tab_metadata: dict = tab_json_data["tab"]

    # Extract meaingful metadata
    info_dict: dict = {
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


#                                                                artist   title
#                                                                    V     V
tab_url_pattern = re.compile("(https://tabs.ultimate-guitar.com/tab/[^&]+/[^&]+)&")

def exploreurl2taburls(url: str, return_json=False) -> Union[dict, "json"]:
    """
    Ultimate-Guitar has explore pages that are lists of tab links.

    Returns:
        Dictionary/json with the following attributes:
            - "tab_urls": a list of strings, each string the https url to a guitar tab

    Parameters:
        - url: a string representing the url of the explore page
        - return_json: whether to return as a dict or json
    """

    # Fetch html from the specified url
    html_body: str = str(requests.get(url).content)
    # Extract all urls using regex
    tabs_url_list: list[str] = tab_url_pattern.findall(html_body)
    tabs_dict = {"tab_urls": tabs_url_list}

    if return_json:
        return json.dumps(tabs_dict, ensure_ascii=False)
    return tabs_dict
