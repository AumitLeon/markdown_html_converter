from setuptools import setup

# Should match git tag
VERSION = '0.3.0'

def readme():
    with open('README.md') as f:
        return f.read()

with open('requirements.txt') as file:
    REQUIRED_MODULES = [line.strip() for line in file]

with open('requirements-dev.txt') as file:
    DEVELOPMENT_MODULES = [line.strip() for line in file]


setup(name='md-to-html',
      version=VERSION,
      description='Python module for converting Markdown to HTML',
      long_description=readme(),

      keywords='markdown to html',
      url='https://github.com/AumitLeon/markdown_html_converter',
      author='Aumit Leon',
      author_email='aumitleon@gmail.com',
      packages=['src'],
      install_requires=REQUIRED_MODULES,
      extras_require={'dev': DEVELOPMENT_MODULES},
      entry_points={
          'console_scripts': ['md-to-html=src.command_line:main'],
      },
      include_package_data=True)
