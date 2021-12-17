import logging
import os
import json

import requests

from reporter.core.errors import NoQueryProvided, RequestError

logger = logging.getLogger(__name__)

FUSEKI_URL = os.getenv('FUSEKI_URL')
FUSEKI_DATASET_NAME = os.getenv('FUSEKI_DATASET_NAME')


def request(query):
    if query is None:
        raise NoQueryProvided()

    logger.debug('Start query %s', query)

    url = f"{FUSEKI_URL}/{FUSEKI_DATASET_NAME}/sparql"
    response = requests.request('POST', url, data={"query": query})

    if response.status_code != 200:
        raise RequestError(f"{response.status_code}: {response.text}")

    logger.debug(response.text)

    json_response = json.loads(response.content)

    logger.debug(json_response)


    # /http://localhost:3030/dataset.html?tab=upload&ds=/loshrdf#query=%0A%0ASELECT+%3Fsubject+%3Fpredicate+%3Fobject%0AWHERE+%7B%0A++%3Fsubject+%3Fpredicate+%3Fobject%0A%7D%0ALIMIT+25
    #
    # curl
    # http: // localhost: 3030 / loshrdf / sparql - X
    # POST - -data
    # 'query=%0A%0ASELECT+%3Fsubject+%3Fpredicate+%3Fobject%0AWHERE+%7B%0A++%3Fsubject+%3Fpredicate+%3Fobject%0A%7D%0ALIMIT+25' - H
    # 'Accept: application/sparql-results+json,*/*;q=0.9'
