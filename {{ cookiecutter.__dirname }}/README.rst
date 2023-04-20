{%- if cookiecutter.target_bundle != 'CircuitPython Org' -%}
    {%- if cookiecutter.library_prefix -%}
        {%- set repo_name = (cookiecutter.library_prefix | capitalize) -%}
        {%- set repo_name = repo_name + '_CircuitPython_' -%}
    {%- else -%}
        {%- set repo_name = 'CircuitPython_' -%}
    {%- endif -%}
    {%- set repo_name = repo_name + cookiecutter.library_name | replace(" ", "_") -%}
{%- else -%}
    {%- set repo_name = 'CircuitPython_Org_' + cookiecutter.library_name | replace(" ", "_") -%}
{%- endif -%}
{%- set full_repo_name = cookiecutter.github_user + "/" + repo_name -%}
{%- set pypi_name = cookiecutter.library_name|lower|replace("_", "-")|replace(" ", "-") -%}
{%- if cookiecutter.target_bundle == 'Adafruit' -%}
    {%- set docs_url = 'https://docs.micropython.org/projects/' + cookiecutter.library_name | lower | replace(" ", "-") + '/en/latest/' -%}
{%- else -%}
    {%- set docs_url = 'https://micropython-' + cookiecutter.library_name | lower | replace(" ", "-") | replace("_", "-") + '.readthedocs.io/' -%}
{%- endif -%}
Introduction
============

{% if cookiecutter.sphinx_docs | lower in ["yes", "y"] %}
.. image:: https://readthedocs.org/projects/{% if cookiecutter.library_prefix %}{{ cookiecutter.library_prefix | lower | replace("_", "-")}}-{% endif %}micropython-{{ cookiecutter.library_name | lower | replace(" ", "-") | replace("_", "-") }}/badge/?version=latest
{%- if cookiecutter.target_bundle == 'Adafruit' %}
    :target: {{ docs_url }}
{%- else %}
    :target: {{ docs_url }}
{%- endif %}
    :alt: Documentation Status
{% endif %}

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

{% if cookiecutter.library_description != "" %}
    {{- cookiecutter.library_description }}
{% else %}
.. todo:: Describe what the library does.
{% endif %}


Installing from PyPI
=====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/{%- if cookiecutter.library_prefix -%}{{ cookiecutter.library_prefix }}-{%- endif -%}micropython-{{ pypi_name }}/>`_.
To install for current user:

.. code-block:: shell

    pip3 install {% if cookiecutter.library_prefix %}{{ cookiecutter.library_prefix }}-{% endif %}micropython-{{ pypi_name }}

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install {% if cookiecutter.library_prefix %}{{ cookiecutter.library_prefix }}-{% endif %}micropython-{{ pypi_name }}

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .env/bin/activate
    pip3 install {% if cookiecutter.library_prefix -%}{{ cookiecutter.library_prefix }}-{% endif -%}micropython-{{ pypi_name }}

