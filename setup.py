from distutils.core import setup

# read the contents of README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'python-billtobox-api',         
  packages=['billtobox', 'billtobox.models', 'billtobox.constants', 'billtobox.cache', 'billtobox.endpoints'],
  version = '0.1.3',
  license='GPL-3.0-or-later',
  description = 'Wrapper for the Bill-To-Box / BanqUP (UnifiedPost) API - v4',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Alexander Schillemans',
  author_email = 'alexander.schillemans@lhs.global',
  url = 'https://github.com/alexanderlhsglobal/python-billtobox-api',
  download_url = 'https://github.com/alexanderlhsglobal/python-billtobox-api/archive/refs/tags/0.1.1.tar.gz',
  keywords = ['bill-to-box', 'api', 'banqup', 'unifiedpost'],
  install_requires=[
          'requests',
          'oauthlib',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Programming Language :: Python :: 3.6',
  ],
)