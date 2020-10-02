#
# pytest common fixtures

import pytest
from tests.common import DictionaryData, DictionaryNames

@pytest.fixture(scope = "session")
def dictionary():
    """Returns a loaded dictionary"""
    dd = DictionaryData()
    dd.readDictionary()
    return dd

@pytest.fixture(scope = "session")
def dictionaryPaths():
    """Returns a dictionary with paths to dictionaries"""
    dn = DictionaryNames()
    rd = dn.getPaths()
    return rd
