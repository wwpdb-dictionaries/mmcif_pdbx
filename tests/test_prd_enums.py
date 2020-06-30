#!/usr/bin/env python

import pytest
from tests.common import DictionaryData

@pytest.fixture
def dictionary():
    """Returns a loaded dictionary"""
    dd = DictionaryData()
    dd.readDictionary()
    return dd


def testDepUiEnums(dictionary):
    """Tests that for PRD vs model enumerations are in sync"""

    mapping = [["pdbx_reference_molecule.class", "pdbx_molecule_features.class"],
               ["pdbx_reference_molecule.type", "pdbx_molecule_features.type"]]

    for m in mapping:
        firstAttr = m[0]
        secondAttr = m[1]

        firstEnum = set(dictionary.getCategoryItemEnum(firstAttr))
        assert len(firstEnum) != 0, print("Missing enumeration for %s" % firstAttr)

        secondEnum = set(dictionary.getCategoryItemEnum(secondAttr))
        assert len(secondEnum) != 0, print("Missing enumeration for %s" % secondAttr)

        assert len(firstEnum-secondEnum) == 0, print("%s has extra enum than %s: %s" % (firstAttr, secondAttr, firstEnum - secondEnum))
        assert len(secondEnum-firstEnum) == 0, print("%s has extra enum than %s: %s" % (secondAttr, firstAttr, secondEnum - firstEnum))        
