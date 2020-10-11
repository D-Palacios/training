import os
import sys
import json
from config import Configuration

path = os.getenv("Http_Path")
method = os.getenv("Http_Method")


def process_post(req, config):
    try:
        return "Function " + req + " = " + str(config.data[req])
    except KeyError:
        print("Key not allowed!", file=sys.stderr)


def process_get(config):
    return json.dumps(config.data, indent=4)


def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    config = Configuration()
    
    print(f"Path: {path}. Method: {method}", file=sys.stderr)

    if method == "POST":
        return process_post(req, config)
    elif method == "GET":
        return process_get(config)
    else:
        raise Exception("Only GET or POST allowed!")
