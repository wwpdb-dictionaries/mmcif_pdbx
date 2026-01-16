#!/usr/bin/env python

import pytest

def _getTypes(dictionary):
    dTypeList = dictionary.getDataTypeList()
    dDict = set()
    for (code, prim, regex, desc) in dTypeList:
        dDict.add(code)
    return dDict
    

def testPdbxItemTypes(dictionary):
    """Ensures data types are known for all pdbx_item_type"""

    dDict = _getTypes(dictionary)
    cats = dictionary.getAllCategory()

    for cat in cats:
        for item in dictionary.getItemNameList(cat):
            dType = dictionary.getPdbxItemType(item)
            if dType is None:
                continue
            assert dType in dDict, "Error: %s type %s not known" % (item, dType)

def testItemTypes(dictionary):
    """Ensures data types are known for item_type"""

    dDict = _getTypes(dictionary)
    cats = dictionary.getAllCategory()

    for cat in cats:
        for item in dictionary.getItemNameList(cat):
            dType = dictionary.getItemType(item)
            if dType is None:
                continue
            assert dType in dDict, "Error: %s type %s not known" % (item, dType)
            
