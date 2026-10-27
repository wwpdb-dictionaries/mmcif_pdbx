#!/usr/bin/env python

import os
import re
import pytest

seq_re="[a-zA-Z0-9\t \r\n\v\f()]+"

@pytest.fixture(scope = "module")
def getRe(dictionary):
    if os.getenv("RE_DEVEL"):
        reg = seq_re
        print("RE_DEVEL: %r" % seq_re)
    else:
        reg = dictionary.getTypeRegexAlt('entity_poly',
                                         'pdbx_seq_one_letter_code')
        print("RE dict: %r" % reg)
    return reg

def check_seq(reg, seq):
    """Checks sequence to ensure complies with regular expression"""
    res = re.search("^%s$" % reg, seq)
    if res:
        return True
    else:
        return False

def test_depositor_sequences(getRe):
    reg = getRe
    assert check_seq(reg, "ABCHDD JDDJ(MSE)MORESEQ")
    assert check_seq(reg, "AG00")
    assert not check_seq(reg, "#SEQ")    
    assert check_seq(reg, "AG\n0\t0")

    
