#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Dieses Skript demonstiert wie man die Dateinamen von Druckdokumenten anpasst und diese im Datesystem automatisch speichert.
# This script demonstrates how to customize the file names of print documents and save them automatically in the file system.
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

print ("Einstellungen der Reports nun gesetzt...")

# Connect to the odoo system
odoo = helper.odoo_connect()

IR_ACTION_REPORT_XML = odoo.env['ir.actions.report.xml']
REPORT_PAPERFORMAT = odoo.env['report.paperformat']

_report_format_id = REPORT_PAPERFORMAT.search([('name', '=', "European A4")])
_format = REPORT_PAPERFORMAT.browse(_report_format_id)

# Rechnungen
_report_id = IR_ACTION_REPORT_XML.search([('name', '=', "Rechnungen"), ('model', '=', "account.invoice")])
if len(_report_id) != 0:
    _report_data = {}
    _report_data['attachment'] = "(object.state in ('open','paid')) and ('Rechnung-'+(object.number or '').replace('/','')+'.pdf')"
    _report_data['print_report_name'] = "(object.state in ('open','paid')) and ('Rechnung-'+(object.number or '').replace('/','')+'.pdf')"
    _report_data['attachment_use'] = True
    _report_data['paperformat_id'] = _report_format_id[0]
    _report = IR_ACTION_REPORT_XML.browse(_report_id)
    _report.write(_report_data)
    print("Rechnungen aktualisiert!")
else:
    print("Rechnungen NICHT gefunden!")


# Angebot / Bestellung (Verkauf)
_report_id = IR_ACTION_REPORT_XML.search([('name', '=', "Angebot / Bestellung"), ('model', '=', "sale.order")])
if len(_report_id) != 0:
    _report_data = {}
    _report_data['attachment'] = "(object.state in ('draft','sent')) and ('Angebot-' + (object.name or '').replace('/','')+'.pdf') or (object.state in ('sale','done')) and ('Auftrag-' + (object.name or '').replace('/','')+'.pdf')"
    _report_data['print_report_name'] = "(object.state in ('draft','sent')) and ('Angebot-' + (object.name or '').replace('/','')+'.pdf') or (object.state in ('sale','done')) and ('Auftrag-' + (object.name or '').replace('/','')+'.pdf')"
    _report_data['attachment_use'] = True
    _report_data['paperformat_id'] = _report_format_id[0]
    _report = IR_ACTION_REPORT_XML.browse(_report_id)
    _report.write(_report_data)
    print("Angebot / Bestellung aktualisiert!")
else:
    print("Angebot / Bestellung NICHT gefunden!")


# Angebotsanfrage (Einkauf)
_report_id = IR_ACTION_REPORT_XML.search([('name', '=', "Angebotsanfrage"), ('model', '=', "purchase.order")])
if len(_report_id) != 0:
    _report_data = {}
    _report_data['attachment'] = "('Einkaufanfrage-' + (object.name or '').replace('/','')+'.pdf')"
    _report_data['print_report_name'] = "('Einkaufanfrage-' + (object.name or '').replace('/','')+'.pdf')"
    _report_data['attachment_use'] = True
    _report_data['paperformat_id'] = _report_format_id[0]
    _report = IR_ACTION_REPORT_XML.browse(_report_id)
    _report.write(_report_data)
    print("Angebotsanfrage aktualisiert!")
else:
    print("Angebotsanfrage NICHT gefunden!")

# Beschaffungsauftrag (Einkauf)
_report_id = IR_ACTION_REPORT_XML.search([('name', '=', "Beschaffungsauftrag"), ('model', '=', "purchase.order")])
if len(_report_id) != 0:
    _report_data = {}
    _report_data['attachment'] = "('Einkauf-' + (object.name or '').replace('/','')+'.pdf')"
    _report_data['print_report_name'] = "('Einkauf-' + (object.name or '').replace('/','')+'.pdf')"
    _report_data['attachment_use'] = True
    _report_data['paperformat_id'] = _report_format_id[0]
    _report = IR_ACTION_REPORT_XML.browse(_report_id)
    _report.write(_report_data)
    print("Beschaffungsauftrag aktualisiert!")
else:
    print("Beschaffungsauftrag NICHT gefunden!")

# Packvorgänge (Lager)
_report_id = IR_ACTION_REPORT_XML.search([('name', '=', "Packvorgänge"), ('model', '=', "stock.picking")])
if len(_report_id) != 0:
    _report_data = {}
    _report_data['attachment'] = "('Packschein-' + (object.name or '').replace('/','')+'.pdf')"
    _report_data['print_report_name'] = "('Packschein-' + (object.name or '').replace('/','')+'.pdf')"
    _report_data['attachment_use'] = True
    _report_data['paperformat_id'] = _report_format_id[0]
    _report = IR_ACTION_REPORT_XML.browse(_report_id)
    _report.write(_report_data)
    print("Packvorgänge aktualisiert!")
else:
    print("Packvorgänge NICHT gefunden!")

# Lieferschein (Lager)
_report_id = IR_ACTION_REPORT_XML.search([('name', '=', "Lieferschein"), ('model', '=', "stock.picking")])
if len(_report_id) != 0:
    _report_data = {}
    _report_data['attachment'] = "('Lieferschein-' + (object.name or '').replace('/','')+'.pdf')"
    _report_data['print_report_name'] = "('Lieferschein-' + (object.name or '').replace('/','')+'.pdf')"
    _report_data['attachment_use'] = True
    _report_data['paperformat_id'] = _report_format_id[0]
    _report = IR_ACTION_REPORT_XML.browse(_report_id)
    _report.write(_report_data)
    print("Lieferschein aktualisiert!")
else:
    print("Lieferschein NICHT gefunden!")

    #('Packschein-' + (object.name or '').replace('/', '') + '.pdf')

