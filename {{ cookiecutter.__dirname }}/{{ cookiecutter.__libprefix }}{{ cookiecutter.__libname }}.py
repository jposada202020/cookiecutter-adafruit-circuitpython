{%- set pypi_name = cookiecutter.library_name|lower|replace("_", "-")|replace(" ", "-") -%}
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

from micropython import const
from adafruit_bus_device import i2c_device
from adafruit_register.i2c_struct import ROUnaryStruct, UnaryStruct
from adafruit_register.i2c_bits import RWBits

try:
    from busio import I2C
    from typing import Tuple
except ImportError:
    pass

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
__repo__ = "https://github.com/{{ cookiecutter.github_user }}/CircuitPython_{{ pypi_name | upper }}.git"


class {{ pypi_name | upper }}:
    """Driver for the {{ pypi_name | upper }} Sensor connected over I2C.

    :param ~busio.I2C i2c_bus: The I2C bus the {{ pypi_name | upper }} is connected to.
    :param int address: The I2C device address. Defaults to :const:`0x69`

    :raises RuntimeError: if the sensor is not found

    **Quickstart: Importing and using the device**

    Here is an example of using the :class:`{{ pypi_name | upper }}` class.
    First you will need to import the libraries to use the sensor

    .. code-block:: python

        import board
        import {{ pypi_name }}

    Once this is done you can define your `board.I2C` object and define your sensor object

    .. code-block:: python

        i2c = board.I2C()  # uses board.SCL and board.SDA
        {{ pypi_name }} = {{ pypi_name | upper }}.{{ pypi_name | upper }}(i2c)

    Now you have access to the attributes

    .. code-block:: python

    """

    def __init__(self, i2c_bus: I2C, address: int = xxx) -> None:
        self.i2c_device = i2c_device.I2CDevice(i2c_bus, address)

        if self._device_id != xxx:
            raise RuntimeError("Failed to find {{ pypi_name | upper }}")