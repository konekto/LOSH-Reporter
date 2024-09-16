import unittest

from reporter.core import requester


class RequesterTest(unittest.TestCase):
    def test_request(self):

        resp = requester.request(None)
        self.assertEqual(resp, False)


if __name__ == '__main__':
    unittest.main()
