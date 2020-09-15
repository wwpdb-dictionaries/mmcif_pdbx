#!/usr/bin/env python

import os
import re
import pytest

#Old regular expression
#collection_date_re = "((([0-9][0-9])(([02468][048])|([13579][26]))-02-29)|((([0-9][0-9])([0-9][0-9])))-((((0[0-9])|(1[0-2]))-((0[0-9])|(1[0-9])|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))"

collection_date_re = "([1-9][0-9](([02468][048])|([13579][26]))-02-29)|[1-9][0-9][0-9][0-9]-((((0[1-9])|(1[0-2]))-((0[1-9])|(1[0-9])|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30))))"

emd_id_re = 'EMD-[0-9]{4,}'

@pytest.fixture(scope = "module")
def getRe(dictionary):
    if os.getenv("RE_DEVEL"):
        reg = emd_id_re
        print("RE_DEVEL: %r" % reg)
    else:
        reg = dictionary.getTypeRegexAlt('em_obsolete',
                                         'entry')
    return reg

def check_emdId(reg, idStr):
    """Checks if emd id is allowed"""
    res = re.search("^%s$" % reg, idStr)
    if res:
        return True
    else:
        return False

def testIds(getRe):
    """Tests existing ids"""
    reg = getRe
    assert check_emdId(reg, 'EMD-1234')
    assert not check_emdId(reg, 'EMD-123')
    assert check_emdId(reg, 'EMD-0123')
    assert check_emdId(reg, 'EMD-12345')
    assert check_emdId(reg, 'EMD-12346789')
