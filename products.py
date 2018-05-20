#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Dieses Skript importiert Produkte aus einen CSV Datei
# This script imports products from a CSV file
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
import csv
import base_helper as helper
import time

print ("Artikelimport gestartet.")

# Connect to the odoo system
odoo = helper.odoo_connect()

PRODUCT_TEMPLATE         = odoo.env['product.template']
PRODUCT_CATEGORY         = odoo.env['product.category']
PRODUCT_SUPPLIERINFO     = odoo.env['product.supplierinfo']
STOCK_CHANGE_PRODUCT_QTY = odoo.env['stock.change.product.qty']
#STOCK_WAREHOUSE          = odoo.env['stock.warehouse']
#STOCK_LOCATION           = odoo.env['stock.location']
#STOCK_LOCATION_ROUTE     = odoo.env['stock.location.route']

_count = 0
_import_csv_file = "products.csv"

_csv_reader = csv.DictReader(open(helper.importcsv + _import_csv_file), delimiter=';')

_rows = list(_csv_reader)
_totalcount = len(_rows)

_csv_reader = csv.DictReader(open(helper.importcsv + _import_csv_file), delimiter=';')

# Store start time
start_time = time.time()

# Perform any action like print a string
print("Printing this string takes ...")

for _products in _csv_reader:

    _do_import = _products["Import"].strip()
    if _do_import != "J":
        continue
        # Diesen Datensatz überspringen
    _product_data = {}

    # Produktnummer
    _productno = _products["Produktnr"].strip()
    if _productno != None and _productno != "":
        _product_data['default_code'] = _productno
        _product_data['barcode'] = _productno

    # Produktname
    _productname = _products["Produktname"].strip()
    if _productname != None and _productname != "":
        _product_data['name'] = _productname

    # Produktbild
    _picture = _products["Bild"].strip()
    if _picture != None and _picture != "":
        _product_data['image'] = helper.get_picture(helper.importimages + _picture)

    # Set product data
    _product_data['active'] = True

    # Produktbeschreibung
    _productdesc = _products["Beschreibung"].strip()
    if _productdesc != None and _productdesc != "":
        _product_data['description'] = _productdesc

    # Produktbeschreibung Einkauf
    _productdesc_purchase = _products["Einkaufstext"].strip()
    if _productdesc_purchase != None and _productdesc_purchase != "":
        _product_data['description_purchase'] = _productdesc_purchase

    # Verkaufstext
    _product_data['description_sale'] = _productdesc + " " + _productdesc_purchase

    # Einkaufspreis
    _product_purchase_price = _products["Einkaufspreis"].strip()
    if _product_purchase_price != None and _product_purchase_price != "":
        _product_data['standard_price'] = float(_product_purchase_price.replace(",","."))
        _product_data['purchase_ok'] = True
    else:
        _product_data['purchase_ok'] = False
        _product_data['standard_price'] = 0


    # Verkaufspreis
    _product_sale_price = _products["Verkaufspreis"].strip()
    if _product_sale_price != None and _product_sale_price != "":
        _product_data['list_price'] = float(_product_sale_price.replace(",","."))
        _product_data['sale_ok'] = True
    else:
        _product_data['sale_ok'] = False
        _product_data['list_price'] = 0

    # Liefrzeit Verkauf
    _product_sale_delay = _products["Lieferzeit VK"].strip()
    if _product_sale_delay != None and _product_sale_delay != "":
        _product_data['sale_delay'] = _product_sale_delay
    else:
        _product_data['sale_delay'] = 1

    # Produkt Gewicht
    _product_weight = _products["Gewicht KG"].strip()
    if _product_weight != None and _product_weight != "":
        if not _product_weight:
            _prod_weight = "0.0"
        _product_data['weight'] = float(_product_weight.replace(",","."))

    # Produktart
    _product_kind = _products["Produktart"].strip()
    if _product_kind == "Verbrauchsmaterial":
        _product_data['type'] = 'consu'
    elif _product_kind == "Dienstleistung":
        _product_data['type'] = 'service'
    else:
        _product_data['type'] = 'product'
        
    # Produkt Mengeneinheit
    _product_uom = _products["Einheit"].strip()
    if _product_uom != None and _product_uom != "":
        _uom_id = helper.get_product_uom_id(_product_uom)
        _product_data['uom_id'] = _uom_id

    # Produkt Mengeneinheit Einkauf
    _product_uom_purchase = _products["Einkaufseinheit"].strip()
    if _product_uom_purchase != None and _product_uom_purchase != "":
        _uom_purchase_id = helper.get_product_uom_id(_product_uom_purchase)
        _product_data['uom_po_id'] = _uom_purchase_id

    # Producable product
    #if prod_is_producable == 1:
    #    _product_data['route_ids'] = [(6, 0, STOCK_LOCATION_ROUTE.search([('name', '=', 'Manufacture')]))]



    # Product category
    _prod_category = _products["Kategorie"].strip()
    _product_category_id = PRODUCT_CATEGORY.search([('name', '=', _prod_category)])
    if len(_product_category_id) > 0:
        _product_data['categ_id'] = _product_category_id[0]
    else:
        _category_data = {}
        _category_data['name'] = _prod_category
        _product_data['categ_id'] = PRODUCT_CATEGORY.create(_category_data)

    # Look if product already exists
    _product_id = PRODUCT_TEMPLATE.search([('default_code', '=', _productno)])
    if len(_product_id) == 0:
        _product_id = PRODUCT_TEMPLATE.create(_product_data)
        _importtype = " importiert "
        # RES_PARTNER.env.commit()
        # _partner_id = RES_PARTNER.search([('eq_customer_ref', '=', _customerno)])
        # _res_partner = RES_PARTNER.browse(_partner_id)
    else:
        product = PRODUCT_TEMPLATE.browse(_product_id)
        _product_id = _product_id[0]
        product.write(_product_data)
        _importtype = " aktualisiert "


    # Product weight
    _product_qty = _products["Menge"].strip()
    if _product_qty != None and _product_qty != "":
        if not _product_qty:
            _product_qty = "0.0"
        _product_qty = float(_product_qty.replace(",","."))

        _prod_chg_qty = {'product_id': _product_id, 'new_quantity': _product_qty,}

        try:
            _chg_qty_id = STOCK_CHANGE_PRODUCT_QTY.create(_prod_chg_qty)
            update_ids = [_chg_qty_id]
            STOCK_CHANGE_PRODUCT_QTY.change_product_qty(update_ids)
        except:
            pass

    # Meldebestände
    if _product_data['type'] == "product":
        helper.set_stock_warehouse_orderpoint(_product_id)

    #_supplierno = _products["Lieferantennr"]
    #_supplier_id = helper.get_res_partner_id(_supplierno,None)

    #_supplier_product_no = _products["Herstellernr"]

    _count += 1
    print ("ProduktNr. " + str(_productno) + " / " + _productname + _importtype + " - bereits " + str(_count) + " von " + str(_totalcount) + " Positionen..")

# Store end time
end_time = time.time()

# Calculate the execution time and print the result
print("%.10f seconds" % (end_time - start_time))

print ("Artikelimport abgeschlossen.")
