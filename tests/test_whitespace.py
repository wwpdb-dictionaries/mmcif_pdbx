import pytest
import re

def testWhiteSpace(dictionaryPaths):
    """Tests for trailing whitespaces in dictionary"""

    ws = re.compile(" +$")

    dpaths = dictionaryPaths
    for (dname, dpath) in dictionaryPaths.items():
        print("My path is", dpath)
        with open(dpath, "r") as fin:
            lines = [x.rstrip("\n") for x in fin.readlines()]

        count = 0
        for line in lines:
            count += 1
            if ws.search(line):
                pytest.fail("Extra widespaces in %s line # %s: %s" % (dname, count, line))
