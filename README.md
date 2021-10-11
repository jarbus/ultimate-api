# Ultimate-API

:guitar: *An API for ultimate-guitar.com, forked from [joncardasis/ultimate-api](https://github.com/joncardasis/ultimate-api) to work in October 2021*

![Python-Version](https://img.shields.io/badge/Python-3.9.7-blue.svg)

## Setup
1. Install python3 from https://www.python.org/downloads/

1. Create a virtual environment of python3:

    ```Python
    # Install virtualenv:
    # pip install virtualenv
    virtualenv -p /usr/local/bin/python3 venv
    source venv/bin/activate
    ```

1. Install dependancies:

    ```Python
    pip install -r requirements.txt
    ```

1. Usage:

    ```bash
    export FLASK_DEBUG=1 // Export for debug if running Flask server
    python run.py        // Run Flask server for multiple api requests OR
    python fetch.py URL    // Which returns the json for a single url, then quits
    ```

## Endpoints

| Method | Endpoint |  Parameters | Result |
| ------ | -------- | ---------- | ------ |
| `GET`  | `/tab`   | `url`: A full (including protocol) url for an ultimate-guitar.com tab. | JSON response containing tab info as well as each tab line
| `GET`  | `/explore` | `url`: A full (including protocol) url for a ultimate-guitar.com page of tabs. | JSON response containing a list of all tab urls on the webpage |

Example:

`curl http://localhost:5000/tab\?url\=https://tabs.ultimate-guitar.com/tab/radiohead/creep-chords-4169`
`curl http://localhost:5000/explore\?url\=https://www.ultimate-guitar.com/explore\?type\[\]\=Tabs`
