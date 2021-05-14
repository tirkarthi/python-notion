======
notion
======


.. image:: https://img.shields.io/pypi/v/pynotion.svg
        :target: https://pypi.python.org/pypi/pynotion

A Python package for notion API at https://developers.notion.com/reference/intro.


* Free software: MIT license


Usage
-----

```
>>> from notion import Notion
>>> client = Notion(api_token="XYZ")
>>> client.get_users(notion_version="2021-12-12")
```

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
