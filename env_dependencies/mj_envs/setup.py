import os
import sys

from setuptools import find_packages, setup

if sys.version_info.major != 3:
    print(
        "This Python is only compatible with Python 3, but you are running "
        f"Python {sys.version_info.major}. The installation will likely fail."
    )


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="mj_envs",
    version="1.0.0",
    packages=find_packages(),
    description="environments simulated in MuJoCo",
    long_description=read("README.md"),
    url="https://github.com/vikashplus/mj_envs.git",
    author="Movement Control Lab, UW",
    install_requires=[
        "click",
        "termcolor",
    ],
)
