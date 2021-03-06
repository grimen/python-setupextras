
# `setupextras` [![PyPI version](https://badge.fury.io/py/setupextras.svg)](https://badge.fury.io/py/setupextras) [![Build Status](https://travis-ci.com/grimen/python-setupextras.svg?branch=master)](https://travis-ci.com/grimen/python-setupextras) [![Coverage Status](https://codecov.io/gh/grimen/python-setupextras/branch/master/graph/badge.svg)](https://codecov.io/gh/grimen/python-setupextras)

*Additional common `setuptools` helpers - for Python.*

## Introduction

TODO


## Install

Install using **pip**:

```sh
$ pip install setupextras
```


## Use

Very basic **[example](https://github.com/grimen/python-setupextras/tree/master/examples/basic.py)**:

```python
# =========================================
#       IMPORTS
# --------------------------------------

import os
import json
import setuptools

import setupextras


# =========================================
#       PACKAGE
# --------------------------------------

name = 'foo'
version = '1.0.0'
description = 'A foo library.'
keywords = [
    'foo',
    'bar',
]

packages = setupextras.get_packages()
data_files = setupextras.get_data_files(['*.*'], os.path.join(name, 'tests', '__fixtures__'))
requirements = setupextras.get_requirements()
readme = setupextras.get_readme()

config = {
    'name': name,
    'version': version,
    'description': (description),
    'keywords': keywords,
    'author': 'Jonas Grimfelt',
    'author_email': 'grimen@gmail.com',
    'url': 'https://github.com/grimen/python-{name}'.format(name = name),
    'download_url': 'https://github.com/grimen/python-{name}'.format(name = name),
    'project_urls': {
        'repository': 'https://github.com/grimen/python-{name}'.format(name = name),
        'bugs': 'https://github.com/grimen/python-{name}/issues'.format(name = name),
    },
    'license': 'MIT',
    'long_description': readme,
    'packages': packages,
    'data_files': data_files,
    'install_requires': requirements,
}

print('CONFIG {0}'.format(json.dumps(config, indent = 4)))


# =========================================
#       MAIN
# --------------------------------------

setuptools.setup(**config)
```


## Test

Clone down source code:

```sh
$ make install
```

Run **colorful tests**, with only native environment (dependency sandboxing up to you):

```sh
$ make test
```

Run **less colorful tests**, with **multi-environment** (using **tox**):

```sh
$ make test-tox
```


## About

This project was mainly initiated - in lack of solid existing alternatives - to be used at our work at **[Markable.ai](https://markable.ai)** to have common code conventions between various programming environments where **Python** (research, CV, AI) is heavily used.


## License

Released under the MIT license.
