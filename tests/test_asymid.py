import pytest
import re
import sys

@pytest.fixture(scope = "module")
def getRe(dictionary):
    reg = dictionary.getTypeRegexAlt('pdbx_struct_assembly_gen_depositor_info',
                                     'chain_id_list')
    return reg


def check_idlist(reg, idlist):
    """Checks idlist valid"""
    print("Testing %s with %s" % (idlist, reg))
    res = re.search("^%s$" % reg, idlist)
    if res:
        return True
    else:
        return False

def testIds(getRe):
    """Tests for different asym id lists with spaces for pdbx_struct_assembly_gen_depositor_info"""

    reg = getRe
    assert check_idlist(reg, 'A')
    assert check_idlist(reg, 'A,B')
    assert check_idlist(reg, 'A,B,C')
    assert check_idlist(reg, ' A,B,C')
    assert check_idlist(reg, ' A ,B,C')
    assert check_idlist(reg, ' A , B,C')
    assert check_idlist(reg, ' A , B ,C')
    assert check_idlist(reg, ' A , B ,C  ')
