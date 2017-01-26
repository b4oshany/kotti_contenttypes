import os

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ''
try:
    CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()
except IOError:
    CHANGES = ''

version = '0.1.5'

install_requires = [
    'Kotti>=1.0.0',
    'kotti_tinymce',
    'kotti_pdf>=0.3.5'
]


setup(
    name='kotti_contenttypes',
    version=version,
    description="Additional content types for Kotti",
    long_description='\n\n'.join([README, CHANGES]),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "License :: Repoze Public License",
    ],
    author='Kotti developers',
    author_email='kotti@googlegroups.com',
    url='https://github.com/b4oshany/kotti_contenttypes',
    keywords='kotti web cms wcms pylons pyramid sqlalchemy bootstrap',
    license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=[],
    dependency_links=[],
    entry_points={
        'fanstatic.libraries': [
            'kotti_contenttypes = kotti_contenttypes.fanstatic:library',
        ],
    },
    package_data={"kotti_contenttypes": ["templates/*", "static/*",
                                          "locale/*", "views/*",
                                          "alembic/*.*",
                                          "alembic/versions/*"]},
    extras_require={},
)
