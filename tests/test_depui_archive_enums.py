#!/usr/bin/env python

import pytest
from tests.common import DictionaryData

@pytest.fixture
def dictionary():
    """Returns a loaded dictionary"""
    dd = DictionaryData()
    dd.readDictionary()
    return dd


def testDepUiEnums(dictionary):
    """Tests that for public enumerations, DepUI does not have any unaccounted for"""
    for cat in dictionary.getAllCategory():
        for item in dictionary.getItemNameList(cat):

            # If local - what DepUI offers vs archive irrelevant
            if dictionary.wwPDBContext(item):
                continue

            archiveEnum = dictionary.getCategoryItemEnum(item)
            if len(archiveEnum) == 0:
                continue

            depUIEnum = dictionary.getCategoryPdbxItemEnum(item)

            # Look for extra DepUI enums
            for e in depUIEnum:
                assert e in archiveEnum, "%s: Enum in DepUI not archive: %s" % (item, e)
