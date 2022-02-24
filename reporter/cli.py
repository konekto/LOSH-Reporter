'''
This module is the entry point for the LOSH Reporter. It parses the command line arguments
and starts the generation of the reports.
'''

import argparse
import logging
import pathlib

from reporter.generator import Generator


def main() -> None:
    '''
    Parses command line arguments and starts generation of report or prints help message
    to command line

    Parameters:
    -

    Returns:
    None
    '''

    parser = argparse.ArgumentParser(
        prog='reporter.py',
        description='LOSH Reporter - Generate beautiful reports for OSH RDF data with Apache Jena')
    parser.add_argument('command', choices=['generate'],
                        help='Command to run')
    parser.add_argument('report_name',
                        help='The name of the report to generate')
    parser.add_argument('--out', type=pathlib.Path,
                        help='The path to generate the output in', default='tmp')
    parser.add_argument('format', choices=['pdf', 'md', 'html'],
                        help='The format the report should be generated in')
    parser.add_argument('--log_to', choices=['file', 'console'], default='file',
                        help='Print logging to console by setting log_to to console')

    args = parser.parse_args()

    # according to parameter log_to: log to file or to console
    if args.log_to == 'file':
        logging.basicConfig(level=logging.DEBUG, filename='./logfile.log', filemode='w',
                            format='%(asctime)s:%(levelname)s:%(message)s')
    if args.log_to == 'console':
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

    logging.info('Start command...')

    if args.command == 'generate':
        report_generator = Generator(reports_path=pathlib.Path('./reports'))
        report_generator.generate(args)
        return

    parser.print_help()


if __name__ == '__main__':
    main()
