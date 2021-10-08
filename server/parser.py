import json
from bs4 import BeautifulSoup

def html_tab_to_json_dict(html_body: str) -> json:
    '''
    Returns a json form of a 'pre' tag in an untimate guitar html tabs body.

    Parameters:
        - html_body: The full html body of an ultimate guitar tab site
        - pre_class_tags: An array of strings for the class names of a 'pre' tag where the chords are located to parse
    '''
    soup = BeautifulSoup(html_body, "html.parser")

    json_string = soup.html.body.find_all("div")[2].attrs["data-content"]

    data_content_json: dict = json.loads(json_string)
    tab_json_data: dict = data_content_json["store"]["page"]["data"]
    tab_music: str = tab_json_data["tab_view"]["wiki_tab"]["content"]
    tab_metadata: dict = tab_json_data["tab"]

    # Extract meaingful metadata
    info_json = {
        'title': tab_metadata["song_name"],
        'rating': tab_metadata["rating"],
        'votes': tab_metadata["votes"],
        'version': tab_metadata["version"],
        'description': tab_metadata["version_description"],
        'url': tab_metadata['tab_url'],
        'lines': tab_music
    }

    # Return constructed json under a single tag
    return {'tab': info_json}
