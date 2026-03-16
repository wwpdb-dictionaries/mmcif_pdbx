#
# pytest common fixtures

import os

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

@pytest.fixture(name="data_dir")
def fixture_data_dir():
    """
    Fixture for the data directory used in tests.

    Returns:
        str: The path to the data directory.
    """
    yield os.path.join(os.path.dirname(__file__), "data")


@pytest.fixture
def wl_data_path(data_dir):
    """
    Fixture for the path to the CNS data file.

    Args:
        data_dir (str): The path to the data directory.

    Returns:
        str: The path to the CNS data file.
    """
    yield os.path.join(data_dir, "WLLIST2")

