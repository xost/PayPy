from distutils.core import setup
#import sys
import py2exe

#sys.path.append()
setup(windows = [{"script": "paypy.py"}],options = {"py2exe" : {'packages': ['ZODB.config','ZODB.DB']}})
