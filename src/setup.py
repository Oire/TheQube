# -*- coding: utf-8 -*-


from setuptools import setup, find_packages
import py2exe
import shutil
from glob import glob
import os
from logger import logger
logging = logger.getChild("Installer")


name = 'TheQube'
__version__ = 0.9
__author__ = 'Andre Polykanine also known as Menelion Elensúlë'

def get_datafiles():
 return [("", ["main.defaults"] + glob('*.exe') + glob("*.dll"))
] + list_all_documentation() + list_session_defaults()  + accessible_output_data() + sound_lib_data() + certifi_data() + get_soundpacks() + get_locales()

def accessible_output_data():
 import accessible_output2
 return accessible_output2.find_datafiles()

def sound_lib_data():
 import sound_lib
 return sound_lib.find_datafiles()

def certifi_data():
 import certifi
 path = os.path.join(certifi.__path__[0], '*.pem')
 results = glob(path)
 dest_dir = os.path.join('certifi')
 return [(dest_dir, results)]

def list_session_defaults():
 files = glob('session/*/*.defaults') + glob('core/sessions/*/*.defaults')
 answer = []
 for i in files:
  answer.append((os.path.split(i)[0], [i]))
 return answer

def get_soundpacks():
 answer = []
 depth = 6
 for root, dirs, files in os.walk('sounds'):
  if depth == 0:
   break
  new = (root, glob('%s/*.wav' % root))
  answer.append(new)
  depth -= 1
 return answer

def get_locales():
 answer = []
 for root, dirs, files in os.walk('locale'):
  new = (root, glob(os.path.join(root, '*.mo')))
  answer.append(new)
 return answer

def list_all_documentation ():
 answer = []
 depth = 6
 for root, dirs, files in os.walk('../Documentation'):
  if depth == 0:
   break
  readme = (root[3:], [os.path.join(root, 'readme.html')])
  answer.append(readme)
  changelog = (root[3:], [os.path.join(root, 'changelog.html')])
  answer.append(changelog)
  depth -= 1
 return answer

if __name__ == '__main__':
 setup(
  name = name,
  author = __author__,
  author_email = "theqube@groups.io",
  version = __version__,
  url = 'http://theqube.oire.org/',
  packages = find_packages(),
  data_files = get_datafiles(),
  options = {
   'py2exe': {
    'packages': ['packaging', 'appdirs'],
    'compressed': False,
    'dll_excludes': ['w9xpopen.exe', 'MSVCP90.dll', 'mswsock.dll', 'powrprof.dll', 'MPR.dll', 'MSVCR100.dll', 'mfc90.dll', 'MSVFW32.dll', 'AVIFIL32.dll', 'AVICAP32.dll', 'ADVAPI32.dll', 'CRYPT32.dll', 'WLDAP32.dll'],
    'optimize': 1,
    'skip_archive': True,
    'excludes': ["win32ui", "pywin.dialogs", "pywin.debugger.dbgcon", "tkinter", "tk", "Tkconstants", "Tkinter", "tcl", "_imagingtk", "PIL._imagingtk", "ImageTk", "PIL.ImageTk", "FixTk", "django", "gobject", "gtk", "unittest", "remote", "ZODB"],
   }
  },
  windows = [
   {
    'script': 'main.pyw',
    'dest_base': 'TheQube',
   }
  ],
  install_requires = [
  ]
 )


