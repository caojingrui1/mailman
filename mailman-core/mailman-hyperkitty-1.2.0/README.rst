======================================
Mailman archiver plugin for HyperKitty
======================================


This module contains a `Mailman`_ archiver plugin which sends emails to
`HyperKitty`_, the web archiver.

.. _Mailman: http://www.list.org
.. _HyperKitty: http://hyperkitty.rtfd.org

All documentation on installing HyperKitty can be found in the documentation
provided by the ``HyperKitty`` python package. It is also available online at
the following URL: http://hyperkitty.readthedocs.org.

All documentation on installing HyperKitty Plugin can be found in the
documentation provided by the following URL:
http://hyperkitty.readthedocs.io/en/latest/install.html#connecting-to-mailman.

The source code is available on GitLab
https://gitlab.com/mailman/mailman-hyperkitty.
It is developed by the same people who develop HyperKitty, so you can use the
same communication channels to reach them.

Changelog
=========

1.2.0
-----

- Update the authentication to call Hyperkitty using the API key as a part of
  Authorization HTTP header instead of url parameter.


Copyright & Licensing
=====================

This module is licensed under the
`GPL v3.0 <http://www.gnu.org/licenses/gpl-3.0.html>`_

Copyright (C) 2014-2021 by the Free Software Foundation, Inc.
