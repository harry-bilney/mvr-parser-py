from setuptools import setup, find_packages


setup(
    name='mvr_parser',
    version='1.0.0-alpha1',
    license='MIT',
    author="Harry Bilney",
    author_email='harry@harrybilney.co.uk',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/harry-bilney/mvr-parser-py',
    keywords='',
)