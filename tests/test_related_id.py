#!/usr/bin/env python

import pytest
import re

def testReplacedItems(dictionary):
    """Tests that pdbx_database_related.db_id limits spaces, semicolon, or comma"""

    pattern = dictionary.getTypeRegex("pdbx_database_related", "db_id")

    reg = re.compile("%s" % pattern)

    assert reg.fullmatch("1abc") is not None
    assert reg.fullmatch("1abc cde") is None
    assert reg.fullmatch("1abccde") is not None
    assert reg.fullmatch("emd-1234") is not None
