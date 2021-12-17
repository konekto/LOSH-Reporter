import pytest

from reporter.core import requester
from reporter.core.errors import NoQueryProvided


class TestRequester:
    def test_request(self):
        with pytest.raises(NoQueryProvided):
            requester.request(None)

