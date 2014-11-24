#!/usr/bin/python

import sys
import locale, yaml


DEFAULT_LANG = 'en'

class _translations():
    def __init__(self, path, section):
        try:
            # credits to nrgaway.
            language = DEFAULT_LANG
            language = locale.getdefaultlocale()[0].split('_')[0]
            if language:
                language = language
            self.translations = path
            stream = file(self.translations, 'r')
            data = yaml.load(stream)
            if data:
                self.section = data[section]
                self.language = self.section.get(language, DEFAULT_LANG)

        except (IOError):
            # TODO: add code here.
            pass
        except (yaml.scanner.ScannerError, yaml.parser.ParserError):
            pass

    def gettext(self, key):
        return self.language.get(key, None)