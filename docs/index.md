# Starter repo for python modules

The purpose of this project is to create a shared basis for future python modules precongifugred with continuous integration, delivery, and automated releases. 

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
Downstream modules can be installed in the same way once deployed via `semantic-release`, just replace `module-starter.leon` with the name of the module specified in `setup.py`.

## Development
In order to utilize the structure of this project for downstream modules, you should consider the following notes.

### Configuration
All module metadata lives within `setup.py`. This is where you link depenencies, specify source directories, and other important package metadata. A snippet of our `setup.py`:
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
`setup.py` should live in the root of your project. Other files that should live in the root of your project:

* `MANIFEST.in`: Specifies a list of files outside of your specified `packages` (in this case, `src`) that should be included in your distribution.
* `setup.cfg`: Includes configuration information for `semantic-release`. 
* `requirements.txt`: Dependencies for your project.
* `requirements-dev.txt`: Development dependencies for your project, including any dependencies required for testing.
* `LICENSE`: This project uses the [MIT License](https://opensource.org/licenses/MIT).

### Source Files
All source files (i.e your python files for the module itself) should live in the `src` directory. You could use a different directory name, if you do, be sure update the `packages` option within `setup.py`.

This project currently support modules that are meant to be run as command line tools-- see [issue #10](https://github.com/AumitLeon/module_starter_cli/issues/10) for information on future work necessary to provide support for modules meant to be consumed by other python tools. 

Make modifications to your source files as necessary. 

### CircleCI Configuration
This project is equipped with a basic `config.yml`. The details surrounding CircleCI configuration will vary project to project based on whatever workflows you deem necessary. For more information on CircleCI config files, check out their [website](https://circleci.com/docs/2.0/configuration-reference/).

### Commits
All commits should follow the [Angular Commit Message Convention](#https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#-git-commit-guidelines). It is important that you follow these guidelines, since automatic versioning parses commits messages when generating a release. For more information on semantic release and commits, check out their [github project](https://github.com/semantic-release/semantic-release#commit-message-format).

### Versioning
All versioning is automatically handled by [`python-semantic-release`](https://python-semantic-release.readthedocs.io/en/latest/). This project uses [`semantic-versioning`](https://semver.org/), said to make versioning "[unromantic and unsentimental](http://sentimentalversioning.org/)."

The `VERSION` variable is defined in `setup.py`, and is made avaible to `semantic-release` by our `setup.cfg`:
```cfg
[semantic_release]
version_variable = setup.py:VERSION
upload_to_pypi = true
```

When generating new releases, `semantic-release` will automatically bump this variable to the new version number. This is pushed automatically to github via the `release` workflow in our `config.yml`.

## Generating Releases
Releases and versioning are automatically handled by [`python-semantic-release`](https://python-semantic-release.readthedocs.io/en/latest/). In the `release` workflow within our `config.yml`, we have a step that generates the distribution and publishes to the [Python Package Index](https://pypi.org/) (PyPI):
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
👍🎉 First off, thanks for taking the time to contribute! 🎉👍

If you're looking for a place to start, check out our [open issues](https://github.com/AumitLeon/module_starter_cli/issues) -- this is where open issues with the project will be posted. 

Looking to just get your feet wet? Checkout issues tagged with [documentation](https://github.com/AumitLeon/module_starter_cli/issues?q=is%3Aopen+is%3Aissue+label%3Adocumentation) or [good first issue](https://github.com/AumitLeon/module_starter_cli/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22) (these will often be easier tasks that won't require as much knowledge of the project). 

### Workflow
While making your changes, be sure to follow the [Angular Commit Message Conventions](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#-git-commit-guidelines). It's important to adhere to these guidelines because `semantic-release` will parse your commit messages to figure out how to properly bump the version when generating new releases. 

After you think your changes are ready, push up your branch and open a pull request to merge your branch into `master`. Merging to `master` requires at least one approval, so feel free to add a reviewer from the list of contributors. 

Once your pull request is opened, CircleCI will automatically attempt to build your code using what is creatively dubbed the `build` workflow. Checkout out [`config.yml`](.circleci/config.yml) if you're curious about how this is all tied together. 

After your code passes all checks and receives approval, you can squash and merge to `master`! Make sure that the commit message you use for the squash and merge also uses [Angular Commit Message Conventions](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#-git-commit-guidelines). After you finish the merge, be sure to delete your feature branch.

And viola, you're done! If you added a feature, fix, patch or breaking change, `semantic-release` will automatically generate a release and publish it to PyPI. 
