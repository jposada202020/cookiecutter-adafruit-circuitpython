# SPDX-FileCopyrightText: Copyright (c) {% now 'utc', '%Y' %} Jose D. Montoya
#
# SPDX-License-Identifier: MIT
"""
`{% if cookiecutter.library_prefix %}{{ cookiecutter.library_prefix | lower | replace(" ", "_") }}_{% endif %}{{ cookiecutter.library_name | lower | replace(" ", "_") }}`
================================================================================

{% if cookiecutter.library_description != "" %}
    {{- cookiecutter.library_description }}
{% else %}
.. todo:: Describe what the library does.
{% endif %}

* Author(s): Jose D. Montoya


"""

# imports

{% if cookiecutter.target_bundle != 'CircuitPython Org' -%}
    {%- if cookiecutter.library_prefix -%}
        {%- set repo_name = (cookiecutter.library_prefix | capitalize) -%}
        {%- set repo_name = repo_name + '_CircuitPython_' -%}
        {%- set repo_name = repo_name + cookiecutter.library_name | replace(" ", "_") -%}
    {%- else -%}
        {%- set repo_name = 'CircuitPython_' -%}
        {%- set repo_name = repo_name + cookiecutter.library_name | replace(" ", "_") -%}
    {%- endif -%}
{% else -%}
    {%- set repo_name = 'CircuitPython_Org_' + cookiecutter.library_name | replace(" ", "_") -%}
{% endif -%}

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/{{ cookiecutter.github_user }}/{{ repo_name }}.git"