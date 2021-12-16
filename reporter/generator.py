import logging
import os
import pathlib

from reporter.core.errors import ReportNotFound

REPORTS_DIR = pathlib.PosixPath('./reports')


def generate(report_name):
    report_path = [report_path for report_path in os.listdir(REPORTS_DIR) if report_path == report_name]

    if len(report_path) == 0:
        raise ReportNotFound(f"Report with name {report_name} could not be found");

    logging.info(report_path)
