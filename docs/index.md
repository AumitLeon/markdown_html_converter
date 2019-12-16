# Markdown to HTML Converter

This project is preconfigured with [CircleCi](https://circleci.com/) for continuous integration and delivery; releases are automated via `semantic-release.`

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

# Contributing to the Markdown to HTML Converter Project

👍🎉 First off, thanks for taking the time to contribute! 🎉👍

If you're looking for a place to start, check out our [open issues](https://github.com/AumitLeon/markdown_html_converter/issues) -- this is where open issues with the project will be posted. 

Looking to just get your feet wet? Checkout issues tagged with [documentation](https://github.com/AumitLeon/markdown_html_converter/issues?q=is%3Aopen+is%3Aissue+label%3Adocumentation) or [good first issue](https://github.com/AumitLeon/markdown_html_converter/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22) (these will often be easier tasks that won't require as much knowledge of the project). 

## Development

This project uses [python 3.7](https://www.python.org/downloads/). Use a virtual environment to store all of the necessary dependencies for this project.

You can use either [`pyenv`](https://github.com/pyenv/pyenv) or [`virtualenv`](https://virtualenv.pypa.io/en/latest/) as your python virtual environment. No matter what virtual environment module you choose, make sure that you start a virtual environment using python 3.7. 

Once you activate your virtual envrionment, to setup your development environment, first clone the repo, and then run the development setup script to install the necessary dependencies and git hooks

```
sh dev-setup.sh
```

This project uses the [black](https://github.com/psf/black) code formatter, which enforces a clean and consistent code style. 

You are now ready to write code!

### Workflow
While making your changes, be sure to follow the [Angular Commit Message Conventions](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#-git-commit-guidelines). It's important to adhere to these guidelines because `semantic-release` will parse your commit messages to figure out how to properly bump the version when generating new releases. 

After you think your changes are ready, push up your branch and open a pull request to merge your branch into `master`. Merging to `master` requires at least one approval, so feel free to add a reviewer from the list of contributors. 

Once your pull request is opened, CircleCI will automatically attempt to build your code using what is creatively dubbed the `build` workflow. Checkout out [`config.yml`](.circleci/config.yml) if you're curious about how this is all tied together. 

After your code passes all checks and receives approval, you can squash and merge to `master`! Make sure that the commit message you use for the squash and merge also uses [Angular Commit Message Conventions](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#-git-commit-guidelines). After you finish the merge, be sure to delete your feature branch.

And viola, you're done! If you added a feature, fix, patch or breaking change, `semantic-release` will automatically generate a release and publish it to PyPI. 
