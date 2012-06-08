import os
from distutils.core import setup
from faq import VERSION


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-faq',
    version=VERSION,
    description='Frequently Asked Question (FAQ) management for Django apps.',
    url='https://github.com/benspaulding/django-faq/',
    author='Ben Spaulding',
    author_email='ben@benspaulding.us',
    license='BSD',
    download_url='http://github.com/benspaulding/django-faq/tarball/v%s' % VERSION,
    long_description = read('README.rst'),
    packages = ['faq', 'faq.urls', 'faq.views'],
    package_data = {'faq': ['locale/*/LC_MESSAGES/*',
                            'templates/faq/*',
                            'templates/search/indexes/faq/*']},
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Internet :: WWW/HTTP :: Site Management'],
)
