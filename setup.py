from distutils.core import setup

setup(
    name = 'django-eintopf',
    packages = ['eintopf'], # this must be the same as the name above
    version = '0.0.1-beta',
    description = 'Collection of small tools and enhancements for Django',
    author = 'Filip Novak',
    author_email = 'filip.f.novak@gmail.com',
    include_package_data=True,
    license='MIT License',
    url = 'https://github.com/fosil/django-eintopf', # use the URL to the github repo
    download_url = 'https://github.com/fosil/django-eintopf/archive/v0.0.1-beta.tar.gz',
    keywords = ['django', 'templatetags', 'filters'], # arbitrary keywords
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
