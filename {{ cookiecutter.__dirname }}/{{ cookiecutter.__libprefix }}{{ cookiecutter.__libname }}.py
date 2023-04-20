# SPDX-FileCopyrightText: Copyright (c) {% now 'utc', '%Y' %} {{ cookiecutter.author_name }}{% if cookiecutter.company %} for {{ cookiecutter.company }}{% endif %}
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

* Author(s): {{ cookiecutter.author_name }}


"""

# imports

