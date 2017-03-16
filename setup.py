"""
This file is automatically generated by autosetup.py
Please edit the marked area only. Other areas will be
overwritten when autosetup is rerun.
"""

from setuptools import setup

params = dict(
    name='xdrive',
    description='Portable drive that can be moved between AWS instances',
    version='1.2.63',
    url='ssh://git@github.com/simonm3/xdrive.git',
    install_requires=['PyYAML', 'notebook',
                      'boto3', 'Fabric3', 'Fabric', 'pandas'],
    packages=['xdrive'],
    data_files=[('./etc/xdrive', ['licence.txt', 'readme.md',
                                  'config.yaml', 'version', 'examples.ipynb'])],
    py_modules=[],
    include_package_data=True,
    scripts=None,
    setup_requires=['setuptools_git >= 0.3'])

########## EDIT BELOW THIS LINE ONLY ##########

# pipreqs bug identifies this as well as the correct fabric3
params["install_requires"].remove("Fabric")

# optional but useful
params["install_requires"].append("logcon")
params["install_requires"].append("nbextensions")

########## EDIT ABOVE THIS LINE ONLY ##########

setup(**params)
