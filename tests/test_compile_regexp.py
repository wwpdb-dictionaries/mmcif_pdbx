#!/usr/bin/env python

import pytest
import re
import os
import subprocess
import tempfile
from tests.common import DictionaryData

__here = os.path.abspath(os.path.dirname(__file__))
__testexe = os.path.join(__here, "regextest", "build", "t_regex")
__runtest = os.path.exists(__testexe)


def testRegExpPy(dictionary):
    """Tests that the regular expressions in dictionary can be compiled in python"""

    tlist = dictionary.getDataTypeList()
    assert len(tlist) > 0, "Unable to get enumeration list"
    for row in tlist:
        rname = row[0]
        rexp = row[2]
        try:
            rec = re.compile(rexp)
            assert rec, "Unable to compile expression for %s" % rname
        except Exception as e:
            raise Exception("Failed to compile expression for %s error %s" % (rname, e))
        

@pytest.mark.skipif(__runtest is False, reason="Cannot run compiled regex tests without test executable")
def testRegExpC(dictionary):
    """Tests that the regular expressions in dictionary can be compiled in C"""
    tlist = dictionary.getDataTypeList()
    assert len(tlist) > 0, "Unable to get enumeration list"
    for row in tlist:
        rname = row[0]
        rexp = row[2]

        if rname in ["binary"]:
            continue
        (handle, tfile) = tempfile.mkstemp()
        with os.fdopen(handle, "w") as fout:
            fout.write("%s\n" % rexp)

        ret = subprocess.call([__testexe, tfile])
        os.unlink(tfile)

        assert ret == 0, "Unable to compile expression for %s" % rname
                       
