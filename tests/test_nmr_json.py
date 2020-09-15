import pytest
import json
import os

from tests.common import DictionaryData


def testDepUiEnums(dictionary):
    """Tests that for public enumerations, DepUI does not have any unaccounted for"""

    dlist = dictionary.getEnumListAlt('pdbx_nmr_software', 'name')
    dlist.sort()
    print(dlist)

    jsonFile = os.path.join(os.path.dirname(__file__), 'nmrsoftware.json')
    with open(jsonFile, 'r') as fin:
        jlist = json.load(fin)

    jkeys = list(jlist)
    jkeys.sort()
        
    for j in jkeys:
        assert j in dlist, "%s not in nmr softare in dictionary"
