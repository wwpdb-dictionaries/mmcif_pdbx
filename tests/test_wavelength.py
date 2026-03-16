#!/usr/bin/env python

import os
import re
import pytest


# .7 and 0.7
num="([0-9]*(\\.[0-9]*)?)"

# Leading digits before decimal
numlead = "([0-9]+(\\.[0-9]*)?)"
num=f"({numlead}|(\\.[0-9]+))"

wl_re = "([0-9]+(\\.[0-9]*)?|\\.[0-9]+)[[:space:]]*-[[:space:]]*([0-9]+(\\.[0-9]*)?|\\.[0-9]+)|([0-9]+(\\.[0-9]*)?|\\.[0-9]+)([[:space:]]*,[[:space:]]*([0-9]+(\\.[0-9]*)?|\\.[0-9]+))+|[0-9]+(\\.[0-9]*)?|\\.[0-9]+"


wl_re = f"{num}( *[-,] *{num} *)*"

# A number
wl_re = f"{num}"

# number, comma separated number
wl_re = f"{num}( *, *{num} *)*"

rng = f"{num} *- *{num} *"
wl_re = f"({num}|{rng}) *(, *({num}|{rng}) *)*"

# num/range comma, num/range
@pytest.fixture(scope = "module")
def getRe(dictionary):
    if os.getenv("RE_DEVEL"):
        reg = wl_re
        # print("RE_DEVEL: %r" % wl_re)
    else:
        reg = dictionary.getTypeRegexAlt('diffrn_source',
                                         'pdbx_wavelength_list')
    print(reg)
    return reg

def check_wl(reg, wlstr):
    """Checks if wavelength matches regulat expresseion"""
    res = re.search("^%s$" % reg, wlstr)
    if res:
        return True
    else:
        return False


def testSimpleWL(getRe):
    reg = getRe
    assert not check_wl(reg, "")    
    assert check_wl(reg, "1.0333")
    assert check_wl(reg, "1")
    assert check_wl(reg, ".7")
    assert not check_wl(reg, "-.7")    

def testCommaWL(getRe):
    reg = getRe
    assert check_wl(reg, "1.03, 1.02")
    assert check_wl(reg, "1.03,1.02,  12.1")    

#@pytest.mark.skip
def testRange(getRe):
    reg = getRe
    assert check_wl(reg, "1.03 - 1.02")
    assert check_wl(reg, "1.03-1.04")
    assert not check_wl(reg, "1.03-1.04-1.05")    
    

#@pytest.mark.skip
def testfull(getRe, wl_data_path):
    reg = getRe
    with open(wl_data_path) as fin:
        lines = fin.read().splitlines()

    for line in lines:
        d = line.split("\t")
        site= d[0]
        ent = d[1]
        wl = d[2]
        if wl:
            a = check_wl(reg, wl)
            if not a:
                print(site, ent, wl)
        
