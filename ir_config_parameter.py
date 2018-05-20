#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Dieses Skript demonstiert Konfigurationsparameter anzupassen.
# This script denies to adjust configuration parameters.
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

print ("System Parameter setzen..")

# Connect to the odoo system
odoo = helper.odoo_connect()

IR_CONFIG_PARAMETER = odoo.env['ir.config_parameter']

# Ribbon Name
_paramater_id = IR_CONFIG_PARAMETER.search([('key', '=', "ribbon.name")])
if len(_paramater_id) != 0:
    _parameter_data = {}
    _parameter_data['value'] = "SKR03<br/>({db_name})"
    _parameter = IR_CONFIG_PARAMETER.browse(_paramater_id)
    _parameter.write(_parameter_data)
    print("Ribbon-Name aktualisiert!")
else:
    print("Ribbon-Name NICHT gefunden!")

# Ribbon Textfarbe
_paramater_id = IR_CONFIG_PARAMETER.search([('key', '=', "ribbon.color")])
if len(_paramater_id) != 0:
    _parameter_data = {}
    _parameter_data['value'] = "#f0f0f0"
    _parameter = IR_CONFIG_PARAMETER.browse(_paramater_id)
    _parameter.write(_parameter_data)
    print("Ribbon-Textfarbe aktualisiert!")
else:
    print("Ribbon-Textfarbe NICHT gefunden!")

# Ribbon Hintergrundfarbe
_paramater_id = IR_CONFIG_PARAMETER.search([('key', '=', "ribbon.background.color")])
if len(_paramater_id) != 0:
    _parameter_data = {}
    _parameter_data['value'] = "rgba(180,0,0,.4)" # Letzer Wert die die Transparenz
    _parameter = IR_CONFIG_PARAMETER.browse(_paramater_id)
    _parameter.write(_parameter_data)
    print("Ribbon-Hintergrundfarbe aktualisiert!")
else:
    print("Ribbon-Hintergrundfarbe NICHT gefunden!")
