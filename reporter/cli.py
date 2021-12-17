import argparse
import logging
import pathlib

from reporter import generator
from reporter.generator import Generator


def main():
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser(
        prog="reporter.py",
        description='LOSH Reporter - Generate beautiful reports for OSH RDF data with Apache Jena')
    parser.add_argument('command', choices=['generate'],
                        help='Command to run')
    parser.add_argument('report_name',
                        help='The name of the report to generate')
    parser.add_argument('--out', type=pathlib.Path,
                        help='The path to generate the output in', default="tmp")
    args = parser.parse_args()

    logging.info('Start command...')

    if args.command == "generate":
        report_generator = Generator(reports_path='./reports')

        return report_generator.generate(args.report_name)

    parser.print_help()


if __name__ == '__main__':
    main()
