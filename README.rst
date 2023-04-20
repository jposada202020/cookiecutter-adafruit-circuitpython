Introduction
============


This cookiecutter creates a project structure


Cookiecutter Usage
===================

.. code-block:: bash

  # The first time
  pip install cookiecutter~=2.1


Then, fill in the prompts and accomplish some post generation cleanup:

Prompts
--------

* ``target_bundle`` - Adafruit bundle or Community library bundle
* ``github_user`` - GitHub user or organization which will host this repo. For example, Adafruit funded libraries should say "adafruit" here.
* ``author_name`` - Who you are! Sets the copyright to you.
* ``company`` - Used to give Copyright credit to the company funding the library. For example, Adafruit funded libraries should say "Adafruit Industries" here.
* ``library_name`` - Shortest name for the library.
* ``library_description`` - Write a sentence describing the purpose of this library 
* ``sphinx_docs`` - Should the Sphinx based documentation be included in your repo? If so, enter ``y`` or ``yes`` to include the setup.py. For Adafruit libraries this defaults to Yes.


.. note::

    If you are not uploading the repository for Adafruit (i.e., the Community bundle), and you
    wish to use the Release feature on GitHub to upload libraries to PyPI, you will need to
    add your PyPI token to the repository secrets.  Set a secret named ``PYPI_USERNAME`` to
    ``__token__`` and a secret named ``PYPI_PASSWORD`` to your API token with the proper scope.
    Never share your API token anyone!


