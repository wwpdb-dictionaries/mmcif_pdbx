#!/usr/bin/env python

import pytest
import re

def testObsoletedIds(dictionary):
    """Tests that _pdbx_initial_refinement_model.entity_id_list limits to ids with no spaces"""

    pattern = dictionary.getTypeRegex("pdbx_initial_refinement_model", "entity_id_list")

    reg = re.compile("^%s$" % pattern)

    print("Pattern", pattern)
    assert reg.fullmatch("1") is not None
    assert reg.fullmatch("123") is not None
    assert reg.fullmatch("1 ") is None    
    assert reg.fullmatch("1,2,3,4") is not None
    assert reg.fullmatch("1,2,347,4") is not None    
    assert reg.fullmatch("1, 2") is None
