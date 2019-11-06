# Python Testing
----------------

Objectives
----

- verification - prove code works as designed

- facilitate development / debugging:
  - create environment for unit testing functions 
  - recreate issues
  - manage test data 
  

- self-documenting - tests show usage examples

- regression test - prevent new changes from breaking existing function


TDD
----
- Write (failing) test
 - desired new feature or function
 - recreate known failure  
- Develop code to pass test
- Repeat
 


Pytest Main Ideas
-----------------
- uses assert to verify correctness  
- uses introspection to generate diagnostics on test failure
- very simple structure to add tests
- like python, has many plugins and extensions
- provides command line options for unit or regression test
- PyCharm supports testing from the IDE


Installation
------------
CLI: pip install pytest

Pycharm: Project Settings->Tools->Python Integrated Tools->Testing (change default test runner to pytests)

add pytest to install_requires in setup.py


Source Structure
----------------
Autodiscovery:
  test sources matching `test_*.py` containing functions starting with `test_*()`
  or `class Test*()` containing methods starting with `test_*(self)`

Example minimal project layout:
Project name: `pytesto` 
Module: testbed
```
pytesto
pytesto/README.md
pytesto/docs
pytesto/setup.py
pytesto/testbed
pytesto/testbed/testbed.py
pytesto/testbed/__init__.py
pytesto/tests
pytesto/tests/test_testbed.py
pytesto/tests/__init__.py
```
minimal setup.py
```
from setuptools import setup, find_packages


requires = [
    'pytest',
    'flake8',
    'pyaml'
]

setup(
    name='pytesto',
    version='0.0.1',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=requires,
    author='Matt Krueger',
    author_email='mkrueger@rstms.net',
    description='pytest example',
)
```

Links
-----

http://pytest.org/en/latest/contents.html
https://www.jetbrains.com/help/pycharm/pytest.html
https://github.com/navdeep-G/samplemod




Demonstration
-------------
- CLI usage
 - virtualenvwrapper `workon cfgdir`
 - `make test`
 - tox
- open cfgdir project in PyCharm-
 - IDE testing API:
 - all tests
 - single test
 - debug in test
- Configure PyCharm:
 - pytest
 - flake8
- New Project With Tests
 - pytesto
 - example from https://github.com/navdeep-G/samplemod (Hitchhiker's Guide to Python)
