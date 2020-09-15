#!/usr/bin/env python

import os
import re
import pytest


# Requirements:
# Blank lines (or with a little space not count
# SPaces before or after numbers
# Final newline optional
# Sets of three
#
# float
flt = '-?(([0-9]+)[.]?|([0-9]*[.][0-9]+))([(][0-9]+[)])?([eE][+-]?[0-9]+)?'
# optional ws
wsO = '[ \t]*'
spO = ' *'
# mandatory ws
wsM = ' +'
nlM = '\n'
# Allow blank lines
blanklO = '([\t ]*\n)*'
nlO = '\n?'
rowNlM = '(%s%s%s){3}?(%s%s%s%s)' % (wsO, flt, wsM, flt, spO, nlM, blanklO)
rowNlO = '(%s%s%s){3}(%s%s%s%s)' % (wsO, flt, wsM, flt, spO, nlO, blanklO)
#Last line with WS might not need nl - not handled by blanklO
assembly_re = '((%s){3})*(%s){2}(%s)%s' % (rowNlM, rowNlM, rowNlO, wsO)


@pytest.fixture
def getRe(dictionary):
    if os.getenv("RE_DEVEL"):
        reg = assembly_re
    else:
        reg = dictionary.getTypeRegexAlt('pdbx_struct_assembly_gen_depositor_info',
                                         'full_matrices')
    return reg

def check_row(assem_str, nlm=False):
    """Checks row to ensure behaves properly"""
    if nlm:
        res = re.search("^%s$" % rowNlM, assem_str)
    else:
        res = re.search("^%s$" % rowNlO, assem_str)

    if res:
        return True
    else:
        return False


def check_rowM(assem_str):
    return check_row(assem_str, True)


def check_assem(reg, assem_str):
    """Checks assembly string to ensure complies with regular expression"""
    res = re.search("^%s$" % reg, assem_str)
    if res:
        return True
    else:
        return False

####  Tests start here
def testRow():
    """Tests logic of what is a row"""
    assert check_row('1 0 0 0\n')
    assert check_row('1 0 0 0\n  \n')
    assert check_row('1 0 0 0')
    assert not check_row('1 0 0 0 0')
    assert not check_row('1 0 0 0 0\n')
    assert not check_row('1 0 0 0\n 0')
    assert not check_row('1 0 0 0 0 0 0 0')
    assert check_rowM('1 0 0 0\n')
    assert check_rowM('1 0 0 0\n  \n')
    assert not check_rowM('1 0 0 0')

def testSimpleAssemblies(getRe):
    reg = getRe
    assert check_assem(reg, '1 0 0 0\n0 1 0 0\n0 0 1 0')
    assert check_assem(reg, '1 0 0 0\n0 1 0 0\n0 0 1 0\n')
    assert not check_assem(reg, '1 0 0 0\n0 1 0 0\n0 0 1 0\n1 0 0 0')

def testExtraspaceAssemblies(getRe):
    reg = getRe
    assert check_assem(reg, ' 1   0   0  0\n0  1 0  0\n  0 0 1 0')
    assert check_assem(reg, ' 1 0 0 0\n 0 1 0 0\n 0 0 1 0\n')
    assert check_assem(reg, '1 0 0 0\n0 1 0 0\n0 0 1 0  \n\n\n')

def testExtraspaceAssemblies(getRe):
    reg = getRe
    assert check_assem(reg, ' 1   0   0  0\n0  1 0  0\n  0 0 1 0')
    assert check_assem(reg, ' 1 0 0 0\n 0 1 0 0\n 0 0 1 0\n')
    assert check_assem(reg, '1 0 0 0\n0 1 0 0\n0 0 1 0  \n\n\n')

def testMultipleAssemblies(getRe):
    reg = getRe    
    assert check_assem(reg, ' 1   0   0  0\n0  1 0  0\n  0 0 1 0\n 1   0   0  0\n0  1 0  0\n  0 0 1 0')
    assert check_assem(reg, ' 1   0   0  0\n0  1 0  0\n  0 0 1 0\n 1   0   0  0\n0  1 0  0\n  0 0 1 0\n')
    assert not check_assem(reg, ' 1   0   0  0\n0  1 0  0\n  0 0 1 0\n 1   0   0  0\n0  1 0  0\n')

def testMultipleNewlines(getRe):
    reg = getRe
    assert check_assem(reg, ' 1   0   0  0\n0  1 0  0\n 0 0 1 0')
    assert check_assem(reg, ' 1   0   0  0\n0  1 0  0\n\n 0 0 1 0\n')
    assert check_assem(reg, ' 1   0   0  0\n0  1 0  0\n\n 0 0 1 0\n\n')
    assert check_assem(reg, ' 1   0   0  0\n0  1 0  0\n\n 0 0 1 0\n\n   \n')
    assert check_assem(reg, ' 1   0   0  0\n0  1 0  0\n\n 0 0 1 0\n    \n   ')

def testDesignedFailures(getRe):
    reg = getRe
    assert not check_assem(reg, '-0.5000000000 0.8660254038 0.0000000000 0.0000000000 -0.8660254038 -0.5000000000 0.0000000000 123.4120841409 0.0000000000 0.1000000000 1.0000000000 0.2000000000')
    assert not check_assem(reg, '1.0000000000 0.0000000000 0.0000000000 0.0000000000\n0.0000000000 1.0000000000 0.0000000000 0.0000000000\n0.0000000000 0.0000000000 1.0000000000 0.0000000000\n-0.5000000000 -0.8660254038 0.0000000000 106.8780000000\n0.8660254038 -0.5000000000 0.0000000000 61.7060420704\n0.0000000000 0.0000000000 1.0000000000 0.0000000000\n-0.5000000000 0.8660254038 0.0000000000 0.0000000000 -0.8660254038 -0.5000000000 0.0000000000 123.4120841409 0.0000000000 0.0000000000 1.0000000000 0.0000000000')
