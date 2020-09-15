
"""Common loading functions"""

import os

from mmcif.api.DictionaryApi import DictionaryApi
from mmcif.api.PdbxContainers import CifName
from mmcif.io.IoAdapterPy import IoAdapterPy


class DictionaryData(object):
    def __init__(self):
        basedir = os.path.join(os.path.dirname(__file__), "..", "dist")
        self.dictPath = os.path.join(basedir, "mmcif_pdbx_v5_next.dic")

    def readDictionary(self):
        myIo = IoAdapterPy()
        self.__containerList = myIo.readFile(inputFilePath=self.dictPath)
        self._dApi = DictionaryApi(containerList=self.__containerList,
                                  consolidate=True)
        assert len(self.getGroups()) > 0, "Failed to load %s" % self.dictPath

    def getGroups(self):
        groupList = self._dApi.getCategoryGroups()
        return groupList

    def getTypeRegex(self, cat, attrib):
        return self._dApi.getTypeRegex(cat, attrib)

    def getTypeRegexAlt(self, cat, attrib):
        return self._dApi.getTypeRegexAlt(cat, attrib)

    def getDataTypeList(self):
        """ Return list of tuples containing ('code','primitive_code','construct','detail' )
        """
        return self._dApi.getDataTypeList()

    def getEnumList(self, category, attribute, sortFlag=True):
        return self._dApi.getEnumList(category, attribute, sortFlag)

    def getEnumListAlt(self, category, attribute, sortFlag=True):
        return self._dApi.getEnumListAlt(category, attribute, sortFlag)

    def getEnumListAltWithDetail(self, category, attribute):
        return self._dApi.getEnumListAltWithDetail(category, attribute)

    def getAllCategory(self):
        """Returns list of all categories"""
        return self._dApi.getCategoryList()

    def getCategoryList(self):
        return self._dApi.getCategoryList()

    def getItemNameList(self, category):
        return self._dApi.getItemNameList(category)

    def wwPDBContext(self, catItem):
        """Returns true if category or item have local context"""

        category, item = catItem.split('.')
        if category[0] == "_":
            category = category[1:]

        #print "CHECKING ", category, item, self.__dictA.getCategoryContextList(category)
        if self._dApi.getCategoryContextList(category) == ['WWPDB_LOCAL']:
            return True
        if self._dApi.getContextList(category, item) == ['WWPDB_LOCAL']:
            return True

        return False

    def getCategoryItemEnum(self, itemName):
        """Returns any archive enum list"""

        categoryName = CifName.categoryPart(itemName)
        attributeName = CifName.attributePart(itemName)
        return self._dApi.getEnumList(categoryName, attributeName)

    def getCategoryPdbxItemEnum(self, itemName):
        """Returns any DepUI enum list"""

        categoryName = CifName.categoryPart(itemName)
        attributeName = CifName.attributePart(itemName)
        return self._dApi.getEnumListAlt(categoryName, attributeName)

    def getItemRelatedList(self, itemName):
        categoryName = CifName.categoryPart(itemName)
        attributeName = CifName.attributePart(itemName)

        return self._dApi.getItemRelatedList(categoryName, attributeName)


def main():
    d = DictionaryData()
    d.readDictionary()
    print(d.getTypeRegexAlt('diffrn_detector', 'pdbx_collection_date'))
    print(d.getTypeRegex('diffrn_detector', 'pdbx_collection_date'))


if __name__ == '__main__':
    main()
