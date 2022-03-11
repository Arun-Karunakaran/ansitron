#! /usr/bin/python3

from __future__ import print_function
from setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommand
from setuptools.command.build_py import build_py
#from distutils.command.build_py import build_py
from Cython.Build import cythonize
from shutil import copyfile, copy2
from datetime import datetime
import io
import codecs
import os
import sys
import time
import ansitron
import generator

here = os.path.abspath(os.path.dirname(__file__))
os.environ['MY_PROJECT'] = os.path.dirname(os.path.abspath(__file__))
configvarstore= os.path.join(os.environ['MY_PROJECT'], 'ansitron/config/varstore.dat')
versionstore= os.path.join(os.environ['MY_PROJECT'], 'versionstore.dat')

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

def get_version(filename=versionstore):
    with open(filename, "a+") as f:
        f.seek(0)
        v = float(f.read()) + 0.1
        #val = '{0:.2g}'.format(val)
        val = format(v,".2f")
        f.seek(0)
        f.truncate()
        f.write(val)
        return val

def set_packageparams(filename=configvarstore):
    with open(filename, "a+") as f:
        f.seek(0)
        f.truncate()
        f.write("name=ansitron-core\n")
        f.write("author=Arun Karunakaran\n")
        f.write("copyright=Copyright 2020 ArunKarunakaran <akarunakaran.ind@gmail.com>\n")
        f.write("version=%s\n" % get_version())
        f.write("date=%s\n" % datetime.today().strftime("%d-%m-%Y"))
        f.write("email=akarunakaran.ind@gmail.com\n")
        f.write("status=Alpha-Release\n")
        f.write("releaseinfo=%s\n" % "Initial Release for ansitron-core. Description: This product is used for managing the ansible projects more effectively.")

def parsedatfile(*data):

    try:
        myvar = {}
        if len(data) != 1:
            raise Exception("No of parameter passed: 1 arg required.")
        with open(data[0]) as f:
            for line in f:
                key, value = line.partition("=")[::2]
                myvar[key.strip()] = str(value)
            return myvar
    except FileNotFoundError:
        return False

setpkgparam = set_packageparams()
pf = parsedatfile(configvarstore)

extensions = [Extension('ansitron.bin.*', ['ansitron/bin/*.py']),]
#exclude = ['*.ansitron_actions','*.ansitron_builder']

long_description = read('README.md')
with open("requirements.txt", "r") as fh:
    install_reqs = fh.read()

#vlicense = __license__
#vcopyright = __copyright__
#package_names =

setup(
    name=pf['name'].rstrip("\n"),
    #revision=input("Enter the version number of build:"),
    version=format(float(pf['version']),".2f").rstrip("\n"),
    date=pf['date'].rstrip("\n"),
    url="",
    #license=read('LICENSE.md'),
    author=pf['author'].rstrip("\n"),
    license=('LICENSE.md',),
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    install_requires=install_reqs,
    author_email=pf['email'].rstrip("\n"),
    description=pf['releaseinfo'].rstrip("\n"),
    long_description=long_description,
    ext_modules=cythonize(extensions),
    cmdclass={'build_py': build_py},
    #package_dir={"": "nohuyuarintel"}
    packages=find_packages(exclude = ['*.ansitron_actions','*.ansitron_builder','*.ansitronlic*'],include = ['ansitron','ansitron.lib','ansitron.test','ansitron/*.py']),
    package_data={
        'ansitron':['config/*.*'],
        },
    #scripts=['ansitron/bin/ansitron_builder'],
    entry_points={
        'console_scripts': ['ansitron=ansitron.__init__:ansitron','ansitron-builder=ansitron.bin.ansitron_builder:buildactions', 'ansitronlicchk=ansitron.bin.ansitronliccheck:main', 'ansitron-pbook-process=ansitron.bin.ansitron_actions:process_playbook', 'ansitron-pbook-store=ansitron.bin.ansitron_actions:store_playbook', 'ansitron-pbook-retreive=ansitron.bin.ansitron_actions:retreive_playbook'],
        },
    #cmdclass={'build_py': build_py, 'test':PyTest},
    #excluded = [
       # 'ansitron/bin/ansitron_builder.py',
       # 'ansitron/bin/ansitron_actions.py'
       # ],
    #data_files=[('config',['config/ansitron.ini']),('',['_version.py']),('',['_release.py'])],
    zip_safe=False,
    platforms='any',
    #test_suite='src.test.test_nohuyuar',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache License 2.0",
        "Operating System :: Linux",
        "Development Status :: 0 - Prototype",
        "Natural Language :: English",
        #"Environment :: Web Environment',
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        ],
    python_requires='>=3.6',
    extras_require={
        'testing': ['pytest'],
    },
)
