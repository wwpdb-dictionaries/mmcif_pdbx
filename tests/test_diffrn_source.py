import pytest

@pytest.fixture(scope = "module")
def getSourceTypes(dictionary):
    stypes = dictionary.getEnumListAltWithDetail('diffrn_source', 'type')
    return stypes

@pytest.fixture(scope = "module")
def getSourceSources(dictionary):
    stypes = dictionary.getEnumListAltWithDetail('diffrn_source', 'source')
    return stypes


@pytest.fixture(scope = "module")
def getSites(dictionary):
    sites = dictionary.getEnumListAlt('diffrn_source', 'pdbx_synchrotron_site')
    return sites

@pytest.fixture(scope = "module")
def getSitesLC(getSites):
    siteslc = list(map(lambda s: s.lower(), getSites))
    return siteslc

@pytest.fixture(scope = "module")
def getBeamlines(dictionary):
    blines = dictionary.getEnumListAlt('diffrn_source', 'pdbx_synchrotron_beamline')
    return blines

def test_beamlinelist(getSourceTypes, getSitesLC, getBeamlines):
    """Test consistency of beamlines and broken down lists"""
    sTypes = getSourceTypes
    sSitesLC = getSitesLC
    sBeams = getBeamlines

    for (sName, sType) in sTypes:
        if sType in ['SYNCHROTRON', 'FREE ELECTRON LASER']:
            (sSite, sBeam) = sName.split(' BEAMLINE ')
            assert sSite.lower() in sSitesLC, "Site %s unknown" % sSite
            assert sBeam in sBeams, "Beamline %s not listed properly" % sBeam

def test_beamlinesused(getSourceTypes):
    """Test if a given beamline name is used"""
    sTypes = getSourceTypes

    # Need list of available beamlines
    beamlines = set()
    for (sName, sType) in sTypes:
        if sType in ['SYNCHROTRON', 'FREE ELECTRON LASER']:
            (sSite, sBeam) = sName.split(' BEAMLINE ')
            beamlines.add(sBeam)

    #for bLine in self._sBeams:
    #    self.assertIn(bLine, beamlines)
    # Not ready to remove beamlines yet.

def test_sourcetypes(getSourceTypes, getSourceSources):
    """Tests if the type fo the source is listed"""
    stypes = [v[0] for v in getSourceSources]

    for s in getSourceTypes:
        src = s[0]
        st = s[1]
        if st:
            assert st in stypes, f"'{src}' type '{st}' not in source types"

