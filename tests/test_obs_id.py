#!/usr/bin/env python

import pytest
import re

def testObsoletedIds(dictionary):
    """Tests that pdbx_database_PDB_obs_spr.replace_pdb_id limits pdb ids with spaces"""

    pattern = dictionary.getTypeRegex("pdbx_database_PDB_obs_spr", "replace_pdb_id")

    reg = re.compile("^%s$" % pattern)

    print("Pattern", pattern)
    assert reg.fullmatch("3ZN7 3ZN9 3ZND 3ZNE") is not None
    assert reg.fullmatch("4ujz 4uk0 4uk1 4uk2 4uk3") is not None
    assert reg.fullmatch("1abc") is not None
    assert reg.fullmatch("1ABC") is not None
    assert reg.fullmatch("1abccde") is None
    assert reg.fullmatch("emd-1234") is None
