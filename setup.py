#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['rqt_image_view'],
    package_dir={'': 'src'},
    scripts=['scripts/rqt_image_view'],
    entry_points={
        'console_scripts': [
            'rqt_image_view = scripts.rqt_image_view:main',
        ],
    },
)

setup(**d)
