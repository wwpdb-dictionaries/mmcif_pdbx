#!/usr/bin/env python

import os
import re
import pytest

oldRe = '(C[1-9][0-9]*|D[2-9]|D[1-9][0-9]+|O|T|I)'

@pytest.fixture(scope = "module")
def getRe(dictionary):
    if os.getenv("RE_DEVEL"):
        reg = oldRe
        print("RE_DEVEL: %r" % reg)
    else:
        reg = dictionary.getTypeRegexAlt('em_single_particle_entity', 'point_symmetry')
    return reg

def check_point_group(reg, pg):
    """Checks date string to ensure complies with regular expression"""
    res = re.search("^%s$" % reg, pg)
    if res:
        return True
    else:
        return False

def test_pointgroup(getRe):
    reg = getRe
    assert check_point_group(reg, 'C1')
    assert check_point_group(reg, 'C2')
    assert check_point_group(reg, 'I')
    assert check_point_group(reg, 'D2')
    assert check_point_group(reg, 'D4')
    assert check_point_group(reg, 'O')
    assert check_point_group(reg, 'C14')
    assert not check_point_group(reg, 'C1 imposed C3 assumed')

