from io import open

from setuptools import find_packages, setup

with open('sfs/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('=')[1].strip(' \'"')
            break
    else:
        version = '0.0.1'

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

REQUIRES = ['nilearn', 'nibabel']

setup(
    name='sfs',
    version=version,
    description='',
    long_description=readme,
    author='Daniel Gomez',
    author_email='d.gomez@posteo.org',
    maintainer='Daniel Gomez',
    maintainer_email='d.gomez@posteo.org',
    url='https://github.com/dangom/sfs',
    license='MIT',

    keywords=[
        '',
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    install_requires=REQUIRES,
    tests_require=['coverage', 'pytest'],

    packages=find_packages(),
)
