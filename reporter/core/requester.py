'''
This module reads the environment variables and executes sparql querys.
A running local instance of an apache fuseki server which answers the querys is necessary.
'''
import logging
import os
import json
from dotenv import load_dotenv
import requests

from reporter.core.errors import NoQueryProvided, RequestError, NoEnvironmentVariableProvided


load_dotenv()

FUSEKI_URL = os.getenv('FUSEKI_URL')
FUSEKI_DATASET_NAME = os.getenv('FUSEKI_DATASET_NAME')


def request(query) -> list:
    '''
    Gets the query as a string parameter and sends it to a local instance of the fuseki server.

    Parameters:
    query (str): Query string that is sent to the server

    Returns:
    result_list: Return the answer of the fuseki server as a list
    '''

    if query is None:
        raise NoQueryProvided('You must provide a query for doing a request')

    if FUSEKI_URL is None or FUSEKI_DATASET_NAME is None:
        raise NoEnvironmentVariableProvided('please set environment variables for apache fuseki \
            server in the .env-file')
    url = f'{FUSEKI_URL}/{FUSEKI_DATASET_NAME}/sparql'

    # concatenate prefixe and the query
    prefix = 'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>  \
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \
        PREFIX okh: <https://github.com/OPEN-NEXT/OKH-LOSH/raw/master/OKH-LOSH.ttl#>'

    query = prefix + query

    logging.debug('Start query %s', query)

    response = requests.request('POST', url, data={'query': query})

    if response.status_code != 200:
        raise RequestError(f'{response.status_code}: {response.text}')

    logging.debug(response.text)

    result_list = json.loads(response.content)['results']['bindings']

    return result_list
