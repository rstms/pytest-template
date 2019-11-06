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
