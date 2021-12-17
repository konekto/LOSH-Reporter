import os
import shutil
import uuid

import pytest

from reporter.core.errors import ReportNotFound, FileNotFound
from reporter.generator import Generator

reports_path = './tests/.fixtures'


def setup_module():
    os.mkdir(reports_path)


def teardown_module():
    shutil.rmtree(reports_path)


@pytest.fixture
def report_with_no_files():
    name = uuid.uuid4()
    path = f"{reports_path}/{name}"
    os.mkdir(path)
    return str(name)


@pytest.fixture
def report_with_no_template_files():
    name = uuid.uuid4()
    path = f"{reports_path}/{name}"
    os.mkdir(path)
    os.open(path + "/template.md", flags=os.O_RDWR | os.O_CREAT)
    return str(name)


valid_query = """SELECT ?subject ?predicate ?object
WHERE {
  ?subject ?predicate ?object
}
LIMIT 2"""


@pytest.fixture
def report_valid():
    name = uuid.uuid4()
    path = f"{reports_path}/{name}"
    os.mkdir(path)
    os.open(path + "/template.md", flags=os.O_RDWR | os.O_CREAT)
    query_rd = os.open(path + "/query.rd", flags=os.O_RDWR | os.O_CREAT)
    os.write(query_rd, bytes(valid_query.encode('utf-8')))
    return str(name)


class TestGenerator:

    def test_generate(self, report_valid):
        report_generator = Generator(reports_path=reports_path)
        report_generator.generate(report_valid)

    def test_not_found_report_name(self):
        with pytest.raises(ReportNotFound):
            report_generator = Generator(reports_path=reports_path)
            report_generator.generate('NOTFOUND')

    def test_found_report_but_not_query_file(self, report_with_no_files):
        with pytest.raises(FileNotFound):
            report_generator = Generator(reports_path=reports_path)
            report_generator.generate(report_with_no_files)

    def test_found_report_but_not_template_file(self, report_with_no_template_files):
        with pytest.raises(FileNotFound):
            report_generator = Generator(reports_path=reports_path)
            report_generator.generate(report_with_no_template_files)
