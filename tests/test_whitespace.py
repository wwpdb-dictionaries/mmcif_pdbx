import pytest
import re

@pytest.mark.skip(reason="writer will introduce this into file for multiline data items")
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
