'''
This module defines some errors that can appear in the LOSH Reporter
'''

import logging

class ReportNotFound(Exception):
    '''Error indicating that a report is not found at given location'''
    logging.info('The requested report could not be found')

class NoQueryProvided(Exception):
    '''Error indicating that a request was done but no query was provided '''
    logging.info('You must provide a query for doing a request')


class FileNotFound(Exception):
    '''Error indicating that a file is not found at given location'''
    logging.info('The requested file could not be found')


class RequestError(Exception):
    '''Error indicating that the request contained errors'''
    logging.info('The request could not be finished properly.\
        See the logfile for more details')


class NoEnvironmentVariableProvided(Exception):
    '''Error indicating that the environment variables were not set or not found'''
    logging.info('Please set the environment variables and make sure that the \
        system will find them')
        