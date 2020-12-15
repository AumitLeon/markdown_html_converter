Python module for converting markdown files to HTML. Forked from: https://github.com/AumitLeon/module_starter_cli

# Markdown to HTML Converter
[![CircleCI](https://circleci.com/gh/AumitLeon/markdown_html_converter.svg?style=svg)](https://circleci.com/gh/AumitLeon/markdown_html_converter) [![PyPI version](https://badge.fury.io/py/md-to-html.svg)](https://badge.fury.io/py/md-to-html)
[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/semantic-release/semantic-release)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![Documentation Status](https://readthedocs.org/projects/markdown-html-converter/badge/?version=latest)](https://markdown-html-converter.readthedocs.io/en/latest/?badge=latest)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Downloads](https://pepy.tech/badge/md-to-html)](https://pepy.tech/project/md-to-html)


The purpose of this project is to create a simple to use python module that can convert markdown files into rich HTML.

## Table of Contents
<!-- TOC depthFrom:2 -->
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
<!-- /TOC -->

This project is preconfigured with [CircleCi](https://circleci.com/) for continuous integration and delivery; releases are automated via `semantic-release.`

## Requirements
This module requires python version >= 3.5.

## Installation

To install this module:
```
pip install md-to-html
```

## Usage
This module's usage is summarized below:
```
usage: md-to-html [-h] --input INPUT [--output OUTPUT]

Convert Markdown File to HTML file

optional arguments:
  -h, --help show this help message and exit
  --input INPUT, -i INPUT input markdown file
  --output OUTPUT, -o OUTPUT output HTML file
```

## Contributing
If you find this project useful and would like to contribute back to it, feel free to check out the [`CONTRIBUTING`](CONTRIBUTING.md) page. 

### Disclaimer
This project uses the [mistune library](https://github.com/lepture/mistune) for parsing markdown into html. Disclaimer below: 

> Copyright (c) 2014, Hsiaoming Yang
>
> All rights reserved.
>
> Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
>
> * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
>
> * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
>
> * Neither the name of the creator nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
>
> THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
