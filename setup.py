import codecs
import os
import re
from setuptools import setup, find_packages, Extension

BASE_PATH = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(BASE_PATH, 'pyaspeller', '__init__.py'), 'r', 'latin1') as fp:
    try:
        version = re.findall(r"^__version__ = '([^']+)'\r?$",
                             fp.read(), re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')


def read(f):
    return open(os.path.join(BASE_PATH, f)).read().strip()



args = dict(
    name='pyaspeller',
    version=version,
    description=('Python text speller'),
    long_description='\n\n'.join((read('README.rst'), read('CHANGES.txt'))),
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP'],
    author='Vassiliy Taranov',
    author_email='taranov.vv@gmail.com',
    url='https://github.com/oriontvv/pyaspeller',
    license='Apache 2',
    packages=find_packages(),
    # install_requires=install_requires,
    # tests_require=tests_require,
    test_suite='tests',
    include_package_data=True,
    # ext_modules=extensions,
    # cmdclass=dict(build_ext=ve_build_ext)
)


try:
    setup(**args)
except Extension as e:
    raise e
    print("************************************************************")
    print("Cannot compile C accelerator module, use pure python version")
    print("************************************************************")
    del args['ext_modules']
    del args['cmdclass']
    setup(**args)