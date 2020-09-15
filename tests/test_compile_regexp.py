#!/usr/bin/env python

import pytest
import re
from tests.common import DictionaryData

@pytest.fixture
def dictionary():
    """Returns a loaded dictionary"""
    dd = DictionaryData()
    dd.readDictionary()
    return dd


def testRegExpPy(dictionary):
    """Tests that the regular expressions in dictionary can be compiled in python"""

    tlist = dictionary.getDataTypeList()
    assert len(tlist) > 0, "Unable to get enumeration list"
    for row in tlist:
        rname = row[0]
        rexp = row[2]
        try:
            rec = re.compile(rexp)
            assert rec, "Unable to compile expression for %s" % rname
        except Exception as e:
            raise Exception("Failed to compile expression for %s error %s" % (rname, e))
        
