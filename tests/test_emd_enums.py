#!/usr/bin/env python

import pytest

def testDepUiEnums(dictionary):
    """Tests that EMD vs EM enumerations are in sync"""
    #            first                second             use_alt
    mapping = [["emd_software.name", "em_software.name", True],
               ]

    for m in mapping:
        firstAttr = m[0]
        secondAttr = m[1]
        useAlt = m[2]

        if useAlt:
            firstEnum = set(dictionary.getCategoryPdbxItemEnum(firstAttr))
            secondEnum = set(dictionary.getCategoryPdbxItemEnum(secondAttr))
        else:
            firstEnum = set(dictionary.getCategoryItemEnum(firstAttr))
            secondEnum = set(dictionary.getCategoryItemEnum(secondAttr))

        assert len(firstEnum) != 0, print("Missing enumeration for %s" % firstAttr)

        assert len(secondEnum) != 0, print("Missing enumeration for %s" % secondAttr)

        assert len(firstEnum-secondEnum) == 0, print("%s has extra enum than %s: %s" % (firstAttr, secondAttr, firstEnum - secondEnum))
        assert len(secondEnum-firstEnum) == 0, print("%s has extra enum than %s: %s" % (secondAttr, firstAttr, secondEnum - firstEnum))        
