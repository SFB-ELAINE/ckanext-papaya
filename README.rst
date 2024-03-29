.. image:: https://travis-ci.org/SFB-ELAINE/ckanext-papaya.svg?branch=master
    :target: https://travis-ci.org/SFB-ELAINE/ckanext-papaya

===============
ckanext-papaya
===============

This is an extension for CKAN that uses Papaya
(https://github.com/rii-mango/Papaya) to provide views for NIFTI (.nii) and
DICOM (.dcm) file formats. It provides views for both single DICOM files as well
as DICOM directories uploaded to CKAN as a ZIP file.

------------
Requirements
------------

Tested with CKAN 2.9.0a.

------------
Installation
------------

To install ckanext-papaya:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-papaya Python package into your virtual environment::

     pip install ckanext-papaya

3. Add ``papaya`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``). To avoid having the Papaya viewer
   enabled for all ZIP files, regardless of whether they contain DICOM files,
   do **not** add ``papaya`` to ``ckan.views.default_views``.

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


---------------
Config settings
---------------

None at present. NIFTI files and DICOM directories tend to be rather large,
so you may have to increase the maximum resource size to allow users to upload
these file formats.

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

--------------------
Using the Extension
--------------------

The extension automatically creates a view using the Papaya Viewer for single
DICOM files (with file extension .dcm), NIFTI files (with file extension .nii),
and ZIP archives that contain one or more DICOM files. If a ZIP archive contains
other file types besides DICOM files, or DICOM files without the .dcm extension,
they will simply be ignored when displaying correctly-formatted files in
Papaya.

To view zipped DICOM files, the extension temporarily unzips the archive and
passes the contents of the files with .dcm extensions to Papaya. The unzipped
files are deleted immediately to prevent them from taking up space on the server.
Papaya can't actually read local files, since it's a JavaScript framework, so
it is necessary to pass the raw contents of the files rather than the paths to the
files themselves on to Papaya. Users may experience some lag when trying to view
large DICOM directories, but most of this lag comes from Papaya reading the
individual DICOM files rather than from the CKAN extension passing the data to
Papaya.

Unlike our ParaView extension (https://github.com/SFB-ELAINE/ckanext-paraview),
this extension runs directly in CKAN and does not require a separate server.
Once it is installed in a CKAN instance and added to the config file, it will
work without further setup.

This extension will automatically create Papaya views for newly-uploaded files,
but existing resources with NIFTI files, single DICOM files, or DICOM directories
may need to have the Papaya view added manually.
