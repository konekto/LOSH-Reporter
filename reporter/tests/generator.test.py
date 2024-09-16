import unittest

from reporter import generator
from reporter.core.errors import ReportNotFound


class GeneratorTest(unittest.TestCase):
    def not_found_report_name(self):
        self.assertRaises(ReportNotFound, generator.generate, "notfound")


if __name__ == '__main__':
    unittest.main()
