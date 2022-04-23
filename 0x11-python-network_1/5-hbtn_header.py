#!/usr/bin/python3
"""
Python script that sends a request to the URL and
displays the value of a variable in the response header
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    if argv[1]:
        resp = requests.get(argv[1])
        print(resp.headers.get('X-Request-Id'))
