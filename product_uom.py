#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Dieses Skript erzeugt neue Mengeneinheiten für Produkte
# This script creates new units of measure for products
# Version 2.0.0
# Date 20.05.2018
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
import base_helper as helper

print ("Mengeneinheit werden überprüft und ggf. gesetzt...")

# Connect to the odoo system
odoo = helper.odoo_connect()

PRODUCT_UOM = odoo.env['product.uom']

#  100 Stück Einheit anlegen
_uom_id = PRODUCT_UOM.search([('name', '=', "100 Stück")])
if len(_uom_id) == 0:
    _product_uom_data = {
        'name': "100 Stück",
        'uom_type': "bigger",
        'factor_inv': 100.00,
        'category_id': 1
    }
    _uom_id = PRODUCT_UOM.create(_product_uom_data)
    print("Einheit 100 Stück ergänzt")

#  1.000 Stück Einheit anlegen
_uom_id = PRODUCT_UOM.search([('name', '=', "1.000 Stück")])
if len(_uom_id) == 0:
    _product_uom_data = {
        'name': "1.000 Stück",
        'uom_type': "bigger",
        'factor_inv': 1000.00,
        'category_id': 1
    }
    _uom_id = PRODUCT_UOM.create(_product_uom_data)
    print("Einheit 1.000 Stück ergänzt")
