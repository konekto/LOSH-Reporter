'''
This module reads the querys from the querys.json file and initializes the requests to the fuseki
server, the extraction of data out of the results objects and the rendering of the template.
'''

import logging
import json
import pathlib

from datetime import datetime
from reporter.templater import templating
from reporter.core.errors import ReportNotFound, FileNotFound
from reporter.core.requester import request
import subprocess as sp


def get_querys(path) -> dict:
    '''
    Reads the json-file in which the querys are deposited and returns the querys as a dict.

    Parameters:
    path (pathlib.Path): path to the querys.json file

    Returns:
    the querys as dict
    '''

    if path is None:
        raise Exception('No path provided')
    with open(path, encoding='utf-8') as file:
        return json.load(file)


def map_result(result):
    # result is dict
    return_dict = {}

    for key in result:

        keys_of_var = result[key].keys()
        if 'datatype' in keys_of_var:
            if 'integer' in result[key]['datatype']:
                return_dict[key] = int(result[key]["value"])
            if 'decimal' in result[key]['datatype']:
                return_dict[key] = float(result[key]["value"])
        else:
            return_dict[key] = result[key]["value"]

    return return_dict


class Generator:
    '''
    This class reads the querys from the querys.json file and initializes the requests to the
    fuseki server, the extraction of data out of the results objects and the rendering of the
    template
    '''

    def __init__(self, reports_path):
        self.reports_path = pathlib.Path(reports_path)

    def generate(self, args) -> None:
        '''
        Reads in the querys from a file, initializes the request and passes the results to the
        templater

        Parameters:
        self(Generator): The Generator object which contains the path to the template and
                        the query-file
        args (argparse.Namespace): arguments that were passed as cli-parameters

        Returns:
        None
        '''

        report_path = pathlib.Path(f'{self.reports_path}/{args.report_name}')

        if report_path.exists() is False or report_path.is_dir() is False:
            raise ReportNotFound(f'Report with name {args.report_name} could not be found')

        if pathlib.Path(f'{report_path}/query.json').exists() is False:
            raise FileNotFound(f'Query file missing for path {report_path}')

        if pathlib.Path(f'{report_path}/template.md').exists() is False:
            raise FileNotFound(f'template file missing for path {report_path}')

        query_file_path = pathlib.Path(f'{report_path}/query.json')

        querys = get_querys(query_file_path)

        logging.info('Query %s', querys)

        report_module = f'reports.{args.report_name}.report'

        result_data = {}
        for query_name, query in querys.items():
            results = request(query)
            result_data[query_name] = list(map(map_result, results))

        # create output-folder for images if not exists
        path = pathlib.Path(f'./{args.out}/{args.report_name}/img')
        path.mkdir(parents=True, exist_ok=True)
        image_output_path = path.resolve()

        # extract data out of the query results


        result_data['PROJECT_VERSION'] = sp.getoutput('git rev-parse --short HEAD')
        result_data['PROJECT_VERSION_DATE'] = datetime.today().strftime('%Y-%m')
        result_data['PROJECT_VERSION_URL']  = 'https://github.com/OPEN-NEXT/OKH-LOSH/'

        # pass over data to the templater
        templating(result_data, args)
