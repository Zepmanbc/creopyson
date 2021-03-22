=====
Usage
=====

Quickstart
==========

* Download last release_ of Creoson Server for your system.

* Run CreosonSetup and configure it with your Creo's version.

.. _release: https://github.com/SimplifiedLogic/creoson/releases

.. image:: _static/CreosonSetup.png

If you want to launch Creo with Creoson, please create a `nitro_proe_remote.bat` file.

You can copy `C:\\Program Files\\PTC\\Creo x.x\\Mxxx\\Parametric\\bin\\parametric.bat` and rename it `nitro_proe_remote.bat` anywhere you want.

To use Creopyson in a project::

    import creopyson

Create a Client object and create a connection with Creoson::

    c = creopyson.Client()
    c.connect()

Verify is Creo is running::

    c.is_creo_running() # Return a boolean.

Launch Creo::

    c.start_creo("path to nitro_proe_remote.bat")

Basic usage::

    current_directory = c.creo_pwd()  # return current working directory.
    listfiles = c.creo_list_files() # return a list in the working directory.
    listdirs = c.creo_list_dirs() # return a list of folders in the working directory.
    c.creo_cd("new_folder")  # change working directory.
    c.file_exists("my_file.prt")  # verify if `my_file.prt` exists.
    c.file_open("my_file.prt", display=True)  # Open `my_file.prt` in Creo.
    c.dimension_set("my_file.prt", "diamm", 180)  # Modify `diamm` dimension.
    c.file_regenerate("my_file.prt")  # Regenerate file, raise `Warning` if regeneration fails.

-----

Creo 7 Users
============

If you are using Creo 7 you must declare it once per session to prevent errors on deprecated features::

    c.creo_set_creo_version(7)

-----

«Vanilla» Creoson usage
=======================

mostly for debugging::

    import creopyson
    c = creopyson.Client()
    c.connect()

    # Here you define command/function
    # data is a dictionnary with data part of the JSON request
    # Please refer to Creoson documentation
    command = "file"
    function = "open"
    data ={"file":"my_file.prt", "display": True}
    result = c._creoson_post(command, function, data)

*result* would be the *data* part of Creoson's response::

    {'dirname': 'C:/your/working/path/', 'files': ['my_file.prt'], 'revision': 1}

-----

Logging basic usage
===================

If you want see what are the requests to Creoson you should activate logging this way::

    import logging
    logging.basicConfig(level=logging.DEBUG)
    # Hide urllib3 logging
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    import creopyson

    c = creopyson.Client()
    c.connect()

    c.file_open("my_file.prt", display=True)

The result in you console would be something like this::

    DEBUG:creopyson.connection:request: {'sessionId': '', 'command': 'connection', 'function': 'connect', 'data': None}
    DEBUG:creopyson.connection:response: {'status': {'error': False}, 'sessionId': '-8685569143476874454'}
    DEBUG:creopyson.connection:request: {'sessionId': '-8685569143476874454', 'command': 'file', 'function': 'open', 'data': {'display': True, 'activate': True, 'file': 'my_file.prt'}}
    DEBUG:creopyson.connection:response: {'status': {'error': False}, 'data': {'revision': 1, 'files': ['MY_FILE.prt'], 'dirname': 'C:/your/working/path/'}}