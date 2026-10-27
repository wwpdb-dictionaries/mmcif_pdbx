#!/usr/bin/env python

import datetime
import os
import re
import pytest


pdbid_re = "([1-9][A-Z0-9]{3}|pdb_[a-z0-9]{8})"

@pytest.fixture(scope = "module")
def getRe(dictionary):
    if os.getenv("RE_DEVEL"):
        reg = pdbid_re
        print("RE_DEVEL: %r" % reg)
    else:
        reg = dictionary.getTypeRegexAlt('em_start_model', 'pdb_id')
    return reg

def check_pdbid(reg, pdbid):
    """Checks pdbid to ensure complies with regular expression"""
    res = re.search("^%s$" % reg, pdbid)
    if res:
        return True
    else:
        return False


def test_dep_pdbid(getRe):
        reg = getRe
        assert check_pdbid(reg, "1ABC")
        assert not check_pdbid(reg, "1AbC")
        assert not check_pdbid(reg, "0ABC")
        assert not check_pdbid(reg, "0ABC3") # Extra character

def test_ext_pdbid(getRe):
        reg = getRe
        assert check_pdbid(reg, "pdb_00001abc")
        assert check_pdbid(reg, "pdb_a0001abc")        
        assert not check_pdbid(reg, "pdb_0001abc") # 7 characters
        assert not check_pdbid(reg, "pdb_120001abc") # 9 characters        
        
