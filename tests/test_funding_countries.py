#!/usr/bin/env python

import pytest

def testFundingCountries(dictionary):
    """Tests the countries listed in funding source"""

    countries = dictionary.getCategoryPdbxItemEnum("pdbx_audit_support.country")

    funding = dictionary.getEnumListAltWithDetail("pdbx_audit_support", "funding_organization")
    assert len(countries) != 0, print("Missing enumeration for pdbx_audit_support.country")

    assert len(funding) != 0, print("Missing enumeration for pdbx_audit_support.funding_organization")

    for (funder, country) in funding:
        if country == None:
            continue
        assert country in countries, print("Country unknown %s %s" % (funder, country))
