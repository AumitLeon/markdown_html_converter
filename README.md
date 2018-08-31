Python module for converting markdown files to HTML. Forked from: https://github.com/AumitLeon/module_starter_cli

# Starter repo for python modules
[![CircleCI](https://circleci.com/gh/AumitLeon/module_starter_cli.svg?style=svg)](https://circleci.com/gh/AumitLeon/module_starter_cli) [![PyPI version](https://badge.fury.io/py/module-starter.leon.svg)](https://badge.fury.io/py/module-starter.leon)
[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/semantic-release/semantic-release)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![Documentation Status](https://readthedocs.org/projects/module-starter-cli/badge/?version=latest)](https://module-starter-cli.readthedocs.io/en/latest/?badge=latest)


The purpose of this project is to create a shared basis for future python modules precongifugred with continuous integration, delivery, and automated releases. 

## Table of Contents
<!-- TOC depthFrom:2 -->
- [Usage](#usage)
- [Installation](#installation)
- [Development](#development)
  - [Configuration](#configuration)
  - [Structure](#structure)
  - [Source Files](#source-files)
  - [CircleCI Configuration](#circleci-configuration)
  - [Commits](#Commits)
  - [Versioning](#Versioning)
- [Generating Releases](#generating-releases)
  - [Generating an Initial Release](#generating-an-initial-release)
- [Contributing](#contributing)
<!-- /TOC -->

This project is preconfigured with [CircleCi](https://circleci.com/) for continuous integration and delivery, and serves as the starting point for the development and deployment of future Python modules that automate releases via `semantic-release.`

## Usage
To create a module while using this repo as a template, create a new repo and set this project as the remote upstream. This means that when you `git fetch` and `git merge` (or `git pull`, if you prefer), your module project will be updated with changes made in this starter project. 

To set the upstream of your project: 
```
git remote add upstream git@github.com:AumitLeon/module_starter_cli.git
```

If you don't want to keep your downstream module project sycned with changes made to this starter project, feel free to just clone or create a fork. 

## Installation
To install this module:
```
pip install module-starter.leon
```
Downstream modules can be installed in the same way once deployed via `semantic-release`, just replace `module-starter.leon` with the name of the module specified in [`setup.py`](setup.py).

## Development
In order to utilize the structure of this project for downstream modules, you should consider the following notes.

### Configuration
All module metadata lives within [`setup.py`](setup.py). This is where you link depenencies, specify source directories, and other important package metadata. A snippet of our [`setup.py`](setup.py):
```python
setup(name='module-starter.leon',
      version=VERSION,
      description='Starter project for python modules',
      long_description=readme(),
      keywords='module starter',
      url='https://github.com/AumitLeon/module_starter_cli',
      author='Aumit Leon',
      author_email='aumitleon@gmail.com',
      packages=['src'],
      install_requires=REQUIRED_MODULES,
      extras_require={'dev': DEVELOPMENT_MODULES},
      entry_points={
          'console_scripts': ['command=src.command_line:main'],
      },
      include_package_data=True)
```

### Structure
The following is an overview of the directory structure:
```
setup.py
setup.cfg
LICENSE
requirements.txt
requirements-dev.txt
.circleci/
    config.yml
src/
    __init__.py
    command_line.py
    module_starter_main.py
tests/
    test.sh

```
[`setup.py`](setup.py) should live in the root of your project. Other files that should live in the root of your project:

* [`MANIFEST.in`](MANIFEST.in): Specifies a list of files outside of your specified `packages` (in this case, `src`) that should be included in your distribution.
* [`setup.cfg`](setup.cfg): Includes configuration information for `semantic-release`. 
* [`requirements.txt`](requirements.txt): Dependencies for your project.
* [`requirements-dev.txt`](requirements-dev.txt): Development dependencies for your project, including any dependencies required for testing.
* [`LICENSE`](LICENSE): This project uses the [MIT License](https://opensource.org/licenses/MIT).

### Source Files
All source files (i.e your python files for the module itself) should live in the [`src`](src) directory. You could use a different directory name, if you do, be sure update the `packages` option within [setup.py](setup.py).

This project currently support modules that are meant to be run as command line tools-- see [issue #10](https://github.com/AumitLeon/module_starter_cli/issues/10) for information on future work necessary to provide support for modules meant to be consumed by other python tools. 

Make modifications to your source files as necessary. 

### CircleCI Configuration
This project is equipped with a basic [`config.yml`](.circleci/config.yml). The details surrounding CircleCI configuration will vary project to project based on whatever workflows you deem necessary. For more information on CircleCI config files, check out their [website](https://circleci.com/docs/2.0/configuration-reference/).

### Commits
All commits should follow the [Angular Commit Message Convention](#https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#-git-commit-guidelines). It is important that you follow these guidelines, since automatic versioning parses commits messages when generating a release. For more information on semantic release and commits, check out their [github project](https://github.com/semantic-release/semantic-release#commit-message-format).

### Versioning
All versioning is automatically handled by [`python-semantic-release`](https://python-semantic-release.readthedocs.io/en/latest/). This project uses [`semantic-versioning`](https://semver.org/), said to make versioning "[unromantic and unsentimental](http://sentimentalversioning.org/)."

The `VERSION` variable is defined in [`setup.py`](setup.py), and is made avaible to `semantic-release` by our [`setup.cfg`](setup.cfg):
```cfg
[semantic_release]
version_variable = setup.py:VERSION
upload_to_pypi = true
```

When generating new releases, `semantic-release` will automatically bump this variable to the new version number. This is pushed automatically to github via the `release` workflow in our [`config.yml`](.circleci/config.yml).

## Generating Releases
Releases and versioning are automatically handled by [`python-semantic-release`](https://python-semantic-release.readthedocs.io/en/latest/). In the `release` workflow within our [`config.yml`](.circleci/config.yml), we have a step that generates the distribution and publishes to the [Python Package Index](https://pypi.org/) (PyPI):
```yaml
- run:
    name: upload to pypi
        command: |
            git config --global user.email "aumitleon1@gmail.com"
            git config --global user.name "aumitleon"
            . venv/bin/activate
            semantic-release publish
```
This step is only run on *merges into master*. Regular PR branches only run the `build_and_test` workflow, which is meant to give the developer information on if builds are passing with their code. 

### Generating an Initial Release
`semantic-release` is dependent upon git tags to generate and bump new releases and versions. When initially deplpying module projects to github, make sure to push a git tag with the initial version before expecting `semantic-release` to automatically generate releases. 

If your code is starting at `version==1.0.3`, before automating releases, create a tag
```
git tag v1.0.3
```
Push the tag to the remote:
```
git push -u origin v1.0.3
```
Moving forward, `semantic-release` should be able to automatically generate releases for you. 

## Contributing
If you find this project useful and would like to contribute back to it, feel free to check out the [`CONTRIBUTING`](CONTRIBUTING.md) page. 
