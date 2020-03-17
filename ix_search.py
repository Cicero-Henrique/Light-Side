#!/usr/bin/env python
import os
import re
import sys
import time
import json
import urllib
import requests

from pygments import lexers
from pygments import highlight
from pygments import formatters


def ix_search(baseurl, apikey, term):
    """ Initiate authentication and query to IntelligenceX API server """
    headers = {
        'User-Agent': 'ix-client/python',
        'x-key': apikey,
        }

    payload = {
        "term": term,
        "buckets": [],
        "lookuplevel": 0,
        "maxresults": 10,  # change the limit of max results here
        "timeout": 0,
        "datefrom": "",
        "dateto": "",
        "sort": 4,
        "media": 0,
        "terminate": []
    }

    searchurl = 'https://{0}/intelligent/search'.format(baseurl)

    try:
        getid = requests.post(
            searchurl,
            data=json.dumps(payload),
            headers=headers
        )
    except Exception as err:
        print('[error] unhanlded exception: {0}'.format(err))
        raise err

    if getid.status_code == 200:
        id_response = getid.json()

        # Authenticate to API
        if id_response['status'] == 0:
            print('[+]Successful API Authentication. Starting records search.')
            # Craft API URL with the id to return results
            resulturl = str(searchurl) + '/result?id={0}'.format(str(id_response['id']))

            status = 3  # status 3 = No results yet, keep trying. 0 = Success with results
            while status == 3 or status == 0:

                try:
                    getresults = requests.get(resulturl,headers=headers)
                    data = getresults.json()
                except Exception as err:
                    print('[error] unhanlded exception: {0}'.format(err))
                    raise err

                status = data['status']

                if status == 0 or status == 1:
                    # pretty-print JSON data to manipulate as desired
                    print(highlight(
                        unicode(json.dumps(data, indent=4, default=jsondate), 'UTF-8'),
                        lexers.JsonLexer(), formatters.TerminalFormatter())
                    )

                elif status == 2:
                    print('----------------------------------------------')
                    print('[!] Error Code 2 Search ID Not Found ')
                    print('----------------------------------------------')

    else:
        print('----------------------------------------------')
        print('[!] Error Code Status: <{0}>'.format(str(getid.status_code)))
        print('----------------------------------------------')
        print('204 | No Content')
        print('400 | Bad Request. Invalid input.')
        print('401 | Unauthorized. Access not authorized.')
        print('402 | Payment Required. No credits available')
        print('404 | Not Found. Item or identifier not found.')
        print('----------------------------------------------')


if __name__ == '__main__':
    try:
        api_domain = sys.argv[1]
        api_key = sys.argv[2]
        selector = sys.argv[3]
    except IndexError:
        print('usage: python3 ix_search.py <api domain> <api key> <search selector>')
        sys.exit(0)

    if not validators.domain(api_domain):
        print('[error] invalid API domain provided; exiting ...')
        sys.exit(1)

    ix_search(api_domain, api_key, selector)

