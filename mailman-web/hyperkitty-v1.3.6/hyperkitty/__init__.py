# -*- coding: utf-8 -*-
# Copyright (C) 2012-2022 by the Free Software Foundation, Inc.
#
# This file is part of HyperKitty.
#
# HyperKitty is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# HyperKitty is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# HyperKitty.  If not, see <http://www.gnu.org/licenses/>.
#
# Author: Aurelien Bompard <abompard@fedoraproject.org>
#

import sys
import logging

VERSION = "1.3.6"
default_app_config = 'hyperkitty.apps.HyperKittyConfig'

if sys.version > '3':
    try:
        # noinspection PyUnresolvedReferences
        import pymysql
        # noinspection PyUnresolvedReferences
        from pymysql import install_as_MySQLdb

        pymysql.version_info = (1, 4, 13, "final", 0)
        install_as_MySQLdb()
    except ImportError as e:
        logging.error('Import pymysql failed, please check this package, if not required please ignore it.')
