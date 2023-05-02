{%- set repo_name = 'CircuitPython_' -%}
{%- set full_repo_name = "jposada202020" + "/" + repo_name -%}
{%- set pypi_name = cookiecutter.library_name|lower|replace("_", "-")|replace(" ", "-") -%}
{%- set docs_url = 'https://circuitpython-' + cookiecutter.library_name | lower | replace(" ", "-") | replace("_", "-") + '.readthedocs.io/' -%}

Introduction
============

{% if cookiecutter.sphinx_docs | lower in ["yes", "y"] %}
.. image:: https://readthedocs.org/projects/circuitpython-{{ cookiecutter.library_name | lower | replace(" ", "-") | replace("_", "-") }}/badge/?version=latest
{%- if cookiecutter.target_bundle == 'Adafruit' %}
    :target: {{ docs_url }}
{%- else %}
    :target: {{ docs_url }}
{%- endif %}
    :alt: Documentation Status
{% endif %}

.. image:: https://img.shields.io/pypi/v/circuitpython-{{ pypi_name }}.svg
    :alt: latest version on PyPI
    :target: https://pypi.python.org/pypi/circuitpython-{{ pypi_name }}

.. image:: https://static.pepy.tech/personalized-badge/circuitpython-{{ pypi_name }}?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Pypi%20Downloads
    :alt: Total PyPI downloads
    :target: https://pepy.tech/project/circuitpython-{{ pypi_name }}

.. image:: https://github.com/jposada202020/CircuitPython_{{ pypi_name | upper }}/workflows/Build%20CI/badge.svg
    :target: https://github.com/jposada202020/CircuitPython_{{ pypi_name | upper }}/actions
    :alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

{% if cookiecutter.library_description != "" %}
    {{- cookiecutter.library_description }}
{% else %}
.. todo:: Describe what the library does.
{% endif %}

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
{%- if cookiecutter.requires_bus_device in ["y", "yes"] %}
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_
{%- endif %}
{%- if cookiecutter.requires_register in ["y", "yes"] %}
* `Register <https://github.com/adafruit/Adafruit_CircuitPython_Register>`_
{%- endif %}

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Community Bundle library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.


Installing from PyPI
=====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/circuitpython-{{ cookiecutter.library_name }}/>`_.
To install for current user:

.. code-block:: shell

    pip3 install circuitpython-{{ cookiecutter.library_name }}

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install circuitpython-{{ cookiecutter.library_name }}

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .env/bin/activate
    pip3 install circuitpython-{{ cookiecutter.library_name }}

Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install {{ cookiecutter.library_name }}

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Usage Example
=============

Take a look at the examples directory

Documentation
=============
API documentation for this library can be found on `Read the Docs <{{ docs_url }}>`_.


Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/{{ full_repo_name }}/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
