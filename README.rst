Avanza
======

=========== ====
**tests**   |lint|
            |docs|
            |codecov|
**package** |pypi_version|
            |pypi_license|
            |pypi_pversion|
=========== ====

Based on https://github.com/fhqvst/avanza

Python wrapper for Unofficial Avanza API

Code is work in progress and is only meant as “proof of concept”

Authentication is done with selenium, which will save cookies in current
working directory.

Short example of getting the current buyprice for msft stock:

.. code:: python

   import avanza

   msft = avanza.Ticker(3873)
   price = msft.buy_price
   print(price)
   > 166.48

Short example of displaying graph price of msft stock, using matplotlib:

.. code:: python

  import avanza
  import matplotlib.pyplot as plt

  df = avanza.ChartData().get_ticker_chartdata(3873)
  df.plot(kind='line', x='timestamp', y='value')
  plt.show()

More examples can be found
`here <https://github.com/North14/avanza-client>`__

`Documentation <https://avanza.readthedocs.io/en/latest/>`__

Security Notice
===============

This python wrapper voids following bandit codes:
`B101 <https://bandit.readthedocs.io/en/latest/plugins/b101_assert_used.html>`__
`B108 <https://bandit.readthedocs.io/en/latest/plugins/b108_hardcoded_tmp_directory.html>`__
`B301 <https://bandit.readthedocs.io/en/latest/blacklists/blacklist_calls.html#b301-pickle>`__

.. |docs| image:: https://img.shields.io/readthedocs/avanza?style=flat-square&logo=read-the-docs
   :target: https://avanza.readthedocs.io/
   :alt: Read the Docs

.. |lint| image:: https://img.shields.io/github/workflow/status/North14/avanza/python-lint?style=flat-square&logo=github&label=lint%20and%20test
   :alt: GitHub Workflow Status

.. |codecov| image:: https://codecov.io/gh/North14/avanza/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/North14/avanza
  :alt: CodeCov

.. |pypi_version| image:: https://img.shields.io/pypi/v/avanza?style=flat-square&logo=pypi
   :target: https://pypi.org/project/Avanza/
   :alt: PyPI

.. |pypi_license| image:: https://img.shields.io/pypi/l/avanza?style=flat-square&logo=pypi
   :target: https://pypi.org/project/Avanza/
   :alt: PyPI - License

.. |pypi_pversion| image:: https://img.shields.io/pypi/pyversions/avanza?style=flat-square&logo=pypi
   :target: https://pypi.org/project/Avanza/
   :alt: PyPI - Python Version

