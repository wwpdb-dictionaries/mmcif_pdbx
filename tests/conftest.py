#
# pytest common fixtures

import pytest
from tests.common import DictionaryData

@pytest.fixture(scope = "session")
def dictionary():
    """Returns a loaded dictionary"""
    dd = DictionaryData()
    dd.readDictionary()
    return dd
