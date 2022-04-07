#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Dieses Skript demonstiert Cronjobs anzupassen.
# This script denies to adjust cronjobs.
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
from odoorpc_toolbox import base_helper
import os
from datetime import datetime

print ("CRON Parameter setzen..")

# Connect to the odoo system
base_path = os.path.dirname(os.path.abspath(__file__))
# Verbindung
helper = base_helper.EqOdooConnection(base_path + '/config.yaml')
odoo = helper.odoo

IR_CRON = odoo.env['ir.cron']

# Elastic Search account.invoice
_cron_id = IR_CRON.search([('name', '=', "Elastic Search account.invoice")])
if len(_cron_id) != 0:
    _cron_data = {}
    _cron_data['active'] = True
    _cron_data['nextcall'] = str(datetime.now())
    _cron = IR_CRON.browse(_cron_id)
    _cron.write(_cron_data)
    print("Elastic Search account.invoice aktualisiert!")
else:
    print("Elastic Search account.invoice NICHT gefunden!")

