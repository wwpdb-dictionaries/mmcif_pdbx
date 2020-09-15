#!/usr/bin/env python

import datetime
import os
import re
import pytest

#Old regular expression
#collection_date_re="((([0-9][0-9])(([02468][048])|([13579][26]))-02-29)|((([0-9][0-9])([0-9][0-9])))-((((0[0-9])|(1[0-2]))-((0[0-9])|(1[0-9])|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))"

collection_date_re = "([1-9][0-9](([02468][048])|([13579][26]))-02-29)|[1-9][0-9][0-9][0-9]-((((0[1-9])|(1[0-2]))-((0[1-9])|(1[0-9])|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30))))"

@pytest.fixture(scope = "module")
def getRe(dictionary):
    if os.getenv("RE_DEVEL"):
        reg = collection_date_re
        print("RE_DEVEL: %r" % reg)
    else:
        reg = dictionary.getTypeRegexAlt('diffrn_detector',
                                        'pdbx_collection_date')
    return reg

def check_date(reg, date_str):
    """Checks date string to ensure complies with regular expression"""
    res = re.search("^%s$" % reg, date_str)
    if res:
        return True
    else:
        return False


def test_dep_dates(getRe):
        reg = getRe
        assert check_date(reg, "2016-01-01")
        assert not check_date(reg, "2017-02-29")
        assert check_date(reg, "2016-02-29")

def test_dep_years(getRe):
    reg = getRe
    base = datetime.date(2012, 1, 1)
    delta = datetime.timedelta(days=1)
    for i in range(1000):
        dt = base.strftime('%Y-%m-%d')
        assert check_date(reg, dt)
        base += delta

def test_dep_leapyears(getRe):
    
    reg = getRe

    # 2000 is a special case of divisible by four leap year - otherwise divide by 100 not allowed
    for i in range(100):
        dt = "%04d-%02d-%02d" % (i + 2000, 2, 29)
        if i % 4:
            assert not check_date(reg, dt)
        else:
            assert check_date(reg, dt)

    # 2100 should not be allowed - but will wait 80 years to fix regex
    assert check_date(reg, "2100-02-29")

def test_dep_zeros(getRe):
    reg = getRe

    # We do not wish to allow zeros for month/day
    badlist = ['0000-01-01', '0000-02-29', '0000-01-29', '0000-03-29', '2011-00-00', '2011-05-00', '2011-00-03']
    for b in badlist:
        assert not check_date(reg, b), "Date should not be allowed %s" % b
