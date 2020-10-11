import os
import sys

path = os.getenv("Http_Path")
method = os.getenv("Http_Method")


def process_post(req):
    return "This is a POST: " + req


def process_get(req):
    return "This is a GET: " + req


def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    
    print(f"Path: {path}. Method: {method}", file=sys.stderr)

    if method == "POST":
        return process_post(req)
    elif method == "GET":
        return process_get(req)
    else:
        raise Exception("Only GET or POST allowed!")
