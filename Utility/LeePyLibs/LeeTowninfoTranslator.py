# -*- coding: utf-8 -*-

import os
from LeePyLibs import LeeTowninfoLua
from LeePyLibs import LeeCommon
from LeePyLibs import LeeBaseTranslator

class LeeTowninfoTranslator(LeeBaseTranslator):
    def __init__(self):
        LeeBaseTranslator.__init__(self)
        self.leeFileIO = LeeTowninfoLua()
        self.translateDefaultDBPath = 'Resources/Databases/TowninfoTranslate.json'
        self.reSrcPathPattern = self.leeCommon.normPattern(r'^.*?/Patches/.*?/Resource/Original/System/Towninfo.*?\.(lua|lub)')
        self.reDstPathPattern = self.leeCommon.normPattern(r'(^.*?/Patches/.*?/Resource)/Original/(System/Towninfo.*?\.(lua|lub))')

    def translate(self, srcFilepath, dstFilepath):
        self.leeFileIO.load(srcFilepath)
        for translateItem in self.translateMap:
            self.leeFileIO.replaceName(translateItem['src'], translateItem['dst'])
        self.leeFileIO.save(dstFilepath)
