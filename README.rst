.. You should enable this project on travis-ci.org and coveralls.io to make
   these badges work. The necessary Travis and Coverage config files have been
   generated for you.

.. image:: https://travis-ci.org//ckanext-papaya.svg?branch=master
    :target: https://travis-ci.org//ckanext-papaya

.. image:: https://coveralls.io/repos//ckanext-papaya/badge.svg
  :target: https://coveralls.io/r//ckanext-papaya

.. image:: https://img.shields.io/pypi/v/ckanext-papaya.svg
    :target: https://pypi.org/project/ckanext-papaya/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/pyversions/ckanext-papaya.svg
    :target: https://pypi.org/project/ckanext-papaya/
    :alt: Supported Python versions

.. image:: https://img.shields.io/pypi/status/ckanext-papaya.svg
    :target: https://pypi.org/project/ckanext-papaya/
    :alt: Development Status

.. image:: https://img.shields.io/pypi/l/ckanext-papaya.svg
    :target: https://pypi.org/project/ckanext-papaya/
    :alt: License

=============
ckanext-papaya
=============

.. Put a description of your extension here:
   What does it do? What features does it have?
   Consider including some screenshots or embedding a video!


------------
Requirements
------------

For example, you might want to mention here which versions of CKAN this
extension works with.


------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-papaya:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-papaya Python package into your virtual environment::

     pip install ckanext-papaya

3. Add ``papaya`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


---------------
Config settings
---------------

None at present

.. Document any optional config settings here. For example::

.. # The minimum number of hours to wait before re-checking a resource
   # (optional, default: 24).
   ckanext.papaya.some_setting = some_default_value


----------------------
Developer installation
----------------------

To install ckanext-papaya for development, activate your CKAN virtualenv and
do::

    git clone https://github.com//ckanext-papaya.git
    cd ckanext-papaya
    python setup.py develop
    pip install -r dev-requirements.txt


-----
Tests
-----

To run the tests, do::

    nosetests --nologcapture --with-pylons=test.ini

To run the tests and produce a coverage report, first make sure you have
coverage installed in your virtualenv (``pip install coverage``) then run::

    nosetests --nologcapture --with-pylons=test.ini --with-coverage --cover-package=ckanext.papaya --cover-inclusive --cover-erase --cover-tests


----------------------------------------
Releasing a new version of ckanext-papaya
----------------------------------------

ckanext-papaya should be available on PyPI as https://pypi.org/project/ckanext-papaya.
To publish a new version to PyPI follow these steps:

1. Update the version number in the ``setup.py`` file.
   See `PEP 440 <http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers>`_
   for how to choose version numbers.

2. Make sure you have the latest version of necessary packages::

    pip install --upgrade setuptools wheel twine

3. Create a source and binary distributions of the new version::

       python setup.py sdist bdist_wheel && twine check dist/*

   Fix any errors you get.

4. Upload the source distribution to PyPI::

       twine upload dist/*

5. Commit any outstanding changes::

       git commit -a

6. Tag the new release of the project on GitHub with the version number from
   the ``setup.py`` file. For example if the version number in ``setup.py`` is
   0.0.1 then do::

       git tag 0.0.1
       git push --tags