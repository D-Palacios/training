import os
import sys
import pandas as pd

path = os.getenv("Http_Path")
method = os.getenv("Http_Method")

def process_post(req):
    flowfile = [line.split(',') for line in req.split('\n')]
    flowfile = pd.DataFrame(data=flowfile[1:], columns=flowfile[0])
    flowfile.drop(flowfile.tail(1).index, inplace=True)
    flowfile['RSE'].replace('', 0, inplace=True)
    averages = dict.fromkeys(set(flowfile['MsCode'].values))
    for key,_ in averages.items():
        averages[key] = flowfile['RSE'].where(flowfile['MsCode'] == key).astype(float).mean()

    flowfile['RSE'].replace(0, '', inplace=True)
    flowfile['Avg_RSE'] = flowfile['MsCode'].replace(averages)

    return flowfile.to_csv(index=False)

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """    
    print(f"Path: {path}. Method: {method}", file=sys.stderr)

    if method == "POST":
        return process_post(req)
    else:
        raise Exception("Only POST allowed!")
