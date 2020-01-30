=========
Creopyson
=========


.. image:: https://img.shields.io/pypi/v/creopyson.svg
        :target: https://pypi.python.org/pypi/creopyson

.. image:: https://img.shields.io/travis/Zepmanbc/creopyson.svg
        :target: https://travis-ci.org/Zepmanbc/creopyson

.. image:: https://coveralls.io/repos/github/Zepmanbc/creopyson/badge.svg?branch=master
        :target: https://coveralls.io/github/Zepmanbc/creopyson?branch=master

.. image:: https://readthedocs.org/projects/creopyson/badge/?version=latest
        :target: https://creopyson.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://github.com/Zepmanbc/creopyson/raw/master/docs/_static/buymeacoffe.png
        :target: https://www.buymeacoffee.com/Zv7CwOS
        :alt: Buy Me A Coffee

Creopyson is a python library that aim to control `PTC's CREO Parametric`_ via JLink via CREOSON.

CREOSON uses JSON Requests to send commands/functions to CREO, JSON Responses are used to communicate the results of your requests.

Creopyson creates a Client to send JSON Requests to CREOSON server.

* Free software: MIT license
* Documentation: https://creopyson.readthedocs.io.

.. _`PTC's CREO Parametric`: https://www.ptc.com/en/products/cad/creo/parametric

Features
--------

Creopyson can be used to automate actions in CREO:

* Get BOM
* Manage files, Working directories
* Support Familytables
* Export 3D/2D: pdf3d, pdf, STEP, IGES, JPEG...
* Interact with layers, views
* Read/Write parameters, dimensions
* Support Windchill

Basic usage video:

.. image:: https://github.com/Zepmanbc/creopyson/raw/master/docs/_static/video.png
        :target: https://youtu.be/NjkvRZJQzXs

See documentation for more informations...

Credits
-------

CREOSON_ from `Simplified Logic, Inc.`_

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _CREOSON: http://www.creoson.com/
.. _`Simplified Logic, Inc.`: http://www.simplifiedlogic.com/
