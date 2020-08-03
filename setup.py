#!/usr/bin/env python
import os
from glob import glob
from os.path import splitext, basename

import setuptools

__version__ = None
exec(open("src/slack_bolt/version.py").read())

with open("README.md", "r") as fh:
    long_description = fh.read()

here = os.path.abspath(os.path.dirname(__file__))

test_dependencies = [
    "pytest>=5,<6",
    "pytest-asyncio<1",  # for async
    "aiohttp>=3,<4",  # for async
    "black==19.10b0",
]

setuptools.setup(
    name="slack_bolt",
    version=__version__,
    author="Slack Technologies, Inc.",
    author_email="opensource@slack.com",
    description="The Bolt Framework for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/slackapi/bolt-python",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    setup_requires=["pytest-runner==5.2"],
    # python setup.py test
    tests_require=test_dependencies,
    install_requires=[
        "slack_sdk==3.0.0a1",
    ],
    extras_require={
        # pip install -e ".[async]"
        "async": [
            # async features heavily depends on aiohttp
            "aiohttp>=3,<4",
        ],
        # pip install -e ".[adapter]"
        "adapter": [
            # any of async ones
            "aiohttp>=3,<4",
            # used only under src/slack_bolt/adapter
            "boto3<=2",
            "bottle>=0.12,<1",
            "chalice>=1,<2",
            "click>=7,<8",  # for chalice
            "Django>=3,<4",
            "falcon>=2,<3",
            "fastapi>=0.54,<0.55",
            "Flask>=1,<2",
            "pyramid>=1,<2",
            "sanic>=20,<21",
            "starlette>=0.13,<1",
            "tornado>=6,<7",
        ],
        # pip install -e ".[testing]"
        "testing": test_dependencies,
    },
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
