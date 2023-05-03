# SPDX-FileCopyrightText: Copyright (c) {% now 'utc', '%Y' %} Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import board
import {{ cookiecutter.library_name}}

i2c = board.I2C()  # uses board.SCL and board.SDA
xxx = {{cookiecutter.library_name}}.{{ cookiecutter.library_name | upper }}(i2c)

while True:
    #print("Pressure: {:.2f}hPa".format(lps.pressure))
    time.sleep(0.5)