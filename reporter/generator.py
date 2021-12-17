import logging
import os
import pathlib

from reporter.core.errors import ReportNotFound, FileNotFound
from reporter.core.requester import request

logger = logging.getLogger(__name__)


def read_file(path):
    if path is None:
        raise Exception('No path provided')

    file = open(path, "r")
    return file.read()


class Generator:

    def __init__(self, reports_path):
        self.reports_path = pathlib.PosixPath(reports_path)

    def generate(self, report_name):

        report_path = f"{self.reports_path}/{report_name}"

        if os.path.exists(report_path) is False or os.path.isdir(report_path) is False:
            raise ReportNotFound(f"Report with name {report_name} could not be found")

        if os.path.exists(f"{report_path}/query.rd") is False:
            raise FileNotFound(f"Query file missing for path {report_path}")

        if os.path.exists(f"{report_path}/template.md") is False:
            raise FileNotFound(f"template file missing for path {report_path}")

        query_file_path = pathlib.PosixPath(f"{report_path}/query.rd")

        query = read_file(query_file_path)

        logger.info('Query %s', query)

        request(query)
