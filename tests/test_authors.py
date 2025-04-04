#!/usr/bin/env python

import os
import re
import pytest


# "([A-Za-z0-9_]+(( |-|'|\. )[A-Za-z0-9_]+)*( Jr.| III)?, [A-Za-z0-9_]\.(-?[A-Za-z0-9_]+\.)*)|(Seattle Structural Genomics Center for Infectious Disease.*)|(Structural Genomics Consortium.*)|(QCRG Structural Biology Consortium.*)$"

last_name = """[A-Za-z0-9_]+(( |-|'|\\. )[A-Za-z0-9_]+)*( Jr.| III)?"""
first_name = """[A-Za-z0-9_]\\.(-?[A-Za-z0-9_]+\\.)*"""
sgc = "(Seattle Structural Genomics Center for Infectious Disease.*)"
other = "(Structural Genomics Consortium.*)|(QCRG Structural Biology Consortium.*)|(Center for Structures of Membrane Proteins.*)"
author_re = "(" + "(" + last_name + ", " + first_name + ")|" + sgc + "|" + other + ")"

@pytest.fixture(scope = "module")
def getRe(dictionary):
    if os.getenv("RE_DEVEL"):
        reg = author_re
        print("RE_DEVEL: %r" % author_re)
    else:
        reg = dictionary.getTypeRegexAlt('citation_author', 'name')
    return reg

def check_name(reg, name):
    """Checks name to ensure complies with regular expression"""
    res = re.search("^%s$" % reg, name)
    if res:
        return True
    else:
        return False

def test_names_named(getRe):
    reg = getRe
    assert check_name(reg, "Peisach, E.")
    assert not check_name(reg, "Peisach, E")
    assert not check_name(reg, "Peisach,")
    assert not check_name(reg, "Peisach")    
    assert check_name(reg, "Tran, S.C.")
    assert not check_name(reg, "Tran, S.C")
    assert check_name(reg, "Structural Genomics Consortium (SGC)")
    assert check_name(reg, "Center for Structures of Membrane Proteins (CSMP)")
