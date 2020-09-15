#!/usr/bin/env python

import pytest


def _hasReplacedBy(dd, src, target):
    """Checks if lookup of src lists target as a replaceby"""
    srclist = dd.getItemRelatedList(src)
    for p in srclist:
        if p[0] == target and p[1] == 'replacedby':
            return True
    return False

def _hasReplaces(dd, src, target):
    """Checks if lookup of src lists target as a replaces"""
    srclist = dd.getItemRelatedList(src)
    for p in srclist:
        if p[0] == target and p[1] == 'replaces':
            return True
    return False

def testReplacedItems(dictionary):
    """Tests that forward references for replaced items are valid for select categories"""

    cats = []
    prefixes = ['em_', 'software', 'computing', 'atom', 'pdbx']
    for cat in dictionary.getAllCategory():
        for p in prefixes:
            if cat[0:len(p)] == p:
                cats.append(cat)
                break

    for cat in cats:
        for item in dictionary.getItemNameList(cat):
            relList = dictionary.getItemRelatedList(item)
            if relList:
                for r in relList:
                    if r[1] == 'replaces':
                        print(r, item)
                        assert _hasReplacedBy(dictionary, r[0], item) == True, \
                            "Error: %s could not find replacedby %s" \
                            % (item, r)
                        

                    if r[1] == 'replacedby':
                        assert _hasReplaces(dictionary, r[0], item) == True, \
                        "Error: %s could not find replaces %s" % (item, r)

