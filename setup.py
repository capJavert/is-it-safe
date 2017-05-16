from setuptools import setup

__author__ = '@capJavert'

setup(
    name='is-it-safe',
    version='0.0.1',
    summary='shell tool',
    homepage='https://github.com/capJavert/is-it-safe',
    author='capJavert',
    author_email='/',
    license='MIT',
    description='Utility for website or email danger checking',
    platforms='windows, linux, os x',

    py_modules=['iisafe'],
    install_requires=[
        'Click',
        'Requests',
        'lxml'
    ],
    entry_points='''
        [console_scripts]
        iisafe=iisafe:main
    ''',
)
