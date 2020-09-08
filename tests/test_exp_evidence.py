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
    """Tests that depositor experimental evidence and public enumerations are in sync"""

    mapping = [["pdbx_struct_assembly_auth_evidence_depositor_info.experimental_support",
                "pdbx_struct_assembly_auth_evidence.experimental_support"]]

    for m in mapping:
        firstAttr = m[0]
        secondAttr = m[1]

        firstEnum = set(dictionary.getCategoryItemEnum(firstAttr))
        assert len(firstEnum) != 0, print("Missing enumeration for %s" % firstAttr)

        secondEnum = set(dictionary.getCategoryItemEnum(secondAttr))
        assert len(secondEnum) != 0, print("Missing enumeration for %s" % secondAttr)

        assert len(firstEnum-secondEnum) == 0, print("%s has extra enum than %s: %s" % (firstAttr, secondAttr, firstEnum - secondEnum))
        assert len(secondEnum-firstEnum) == 0, print("%s has extra enum than %s: %s" % (secondAttr, firstAttr, secondEnum - firstEnum))        
