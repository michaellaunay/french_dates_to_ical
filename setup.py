#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages


setup(name='french_dates_to_ical',
      version='0.0.1',
      author='Michaël Launay',
      author_email='michaellaunay@ecreall.com',
      url='http://www.ecreall.com/ressources/french_dates_to_ical',
      download_url='https://github.com/michaellaunay/french_dates_to_ical',
      description='Parse a string of french dates to generate the ical rules (RFC 5545)',
      long_description='french_dates_to_ical can be use as a standalone tool or like a library. In both cases, you provide a string of french dates like "Tous les jeudis", and the program returns the ical rules.',

      packages = find_packages(),
      include_package_data = True,
      package_data = {
        '': ['*.txt', '*.rst'],
        #'french_dates_to_ical': ['data/*'],
      },
      exclude_package_data = { '': ['README.txt'] },
      
      scripts = ['bin/fr2ical.py'],
      entry_points = """
          [console_scripts]
          fr2ical = french_dates_to_ical.main:main
          """,
      
      keywords='python tools utils ical',
      license='GPL',
      classifiers=['Development Status :: 2 - Planning',
                   'Natural Language :: French',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 3',
                   'License :: OSI Approved :: GNU Affero General Public License v3',
                   'Topic :: Text Processing :: Dates',
                  ],
                  
      #setup_requires = ['python-stdeb', 'fakeroot', 'python-all'],
      install_requires = ['setuptools', 'docutils>=0.3', 'parsimonious', 'pytest'],
     )
