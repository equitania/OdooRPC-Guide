#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Dieses Skript importiert Produkte aus einen CSV Datei
# This script imports products from a CSV file
# Version 1.0.0
# Date 02.05.2022
##############################################################################
#
#    Python Script 3 for Odoo, Open Source Management Solution
#    Copyright (C) 2018-now Equitania Software GmbH(<http://www.equitania.de>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from odoorpc_toolbox import base_helper
import os

print ("Server informations:")

# Connect to the odoo system
base_path = os.path.dirname(os.path.abspath(__file__))
# Verbindung
helper = base_helper.EqOdooConnection(base_path + '/config.yaml')
odoo = helper.odoo

# Current user
user = odoo.env.user
print('Your user: ' + user.name)            # name of the user connected
print('Your user company: ' + user.company_id.name) # the name of its company

print("Your databases:")
for x in range(len(odoo.db.list())):
    print (odoo.db.list()[x])

print("Your odoo config:")
print(odoo.config)

print("Your context:")
print(odoo.env.context)

print("Odoo version: " + str(helper.odoo_version))

