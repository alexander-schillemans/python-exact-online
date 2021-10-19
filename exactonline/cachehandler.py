import json
import os
import glob

from pathlib import Path

from . import config

class CacheHandler:

    def __init__(self):
        self.rootDir = Path(__file__).parent.absolute()
        self.cacheDir = '{root}/cache'.format(root=self.rootDir)

    def resetCache(self):
        preserveFile = '__init__.py'
        for f in sorted(os.listdir(self.cacheDir)):
            if f != preserveFile:
                fullPath = os.path.join(self.cacheDir, f)
                os.remove(fullPath)
        
        config.CACHE = {}

        return config.CACHE

    def getCache(self, key):
        # if key in config.CACHE: return config.CACHE[key]

        keyPath = '{cache}/{key}.txt'.format(cache=self.cacheDir, key=key)

        try:
            with open(keyPath, 'r') as f:
                value = json.load(f)

            config.CACHE[key] = value
            return value

        except IOError:
            return None
    
    def setCache(self, key, value):
        keyPath = '{cache}/{key}.txt'.format(cache=self.cacheDir, key=key)
        value = json.dumps(value)

        try:
            with open(keyPath, 'w') as f:
                f.write(value)
            
            config.CACHE[key] = value
            return value

        except IOError as e:
            raise IOError('couldnt save to cache. error raised: {0}'.format(e))