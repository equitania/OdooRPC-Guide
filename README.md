# OdooRPC-Guide
Hier erklären wir wie man mittels OdooRPC Daten in Odoo mittels WEB-API importieren kann.  
  
Damit kann man Daten in Odoo importieren oder exportieren.  
  
Basis ist Python 3, kann aber auch unter Python 2.7 verwendet werden, wenn Sie die "print" Befehle anpassen und beim Bildimport anpassungen machen.  

## Voraussetzungen 
* Python 3
* OdooRPC https://pythonhosted.org/OdooRPC/  
  
## Skripte  
* [base_helper.py](https://github.com/equitania/OdooRPC-Guide/blob/master/base_helper.py) - Dieses Skript stellt die Verbindung zum Odoo Server her und stellt einige Hilfsklassen zur Verfügung.
* [get_country_id.py](https://github.com/equitania/OdooRPC-Guide/blob/master/get_country_id.py) - Dieses Skript stellt Hilfsklassen für Länderkodierung von Odoo zur Verfügung.
* [main_addresses.py](https://github.com/equitania/OdooRPC-Guide/blob/master/main_addresses.py) - Dieses Skript importiert Hauptadressen aus einen CSV Datei.
* [products.py](https://github.com/equitania/OdooRPC-Guide/blob/master/products.py) - Dieses Skript importiert Produkte aus einen CSV Datei.
* [product_uom.py](https://github.com/equitania/OdooRPC-Guide/blob/master/product_uom.py) - Dieses Skript erzeugt neue Mengeneinheiten für Produkte.
* [ir_config_parameter.py](https://github.com/equitania/OdooRPC-Guide/blob/master/ir_config_parameter.py) - Dieses Skript demonstiert Konfigurationsparameter anzupassen.
* [ir_cron.py](https://github.com/equitania/OdooRPC-Guide/blob/master/ir_cron.py) - Dieses Skript demonstiert Cronjobs anzupassen.
* [set_ir_actions_report.py](https://github.com/equitania/OdooRPC-Guide/blob/master/set_ir_actions_report.py) - Dieses Skript demonstiert wie man die Dateinamen von Druckdokumenten anpasst und diese im Datesystem automatisch speichert.
  
## Start
Öffnen Sie die Datei [base_helper.py](https://github.com/equitania/OdooRPC-Guide/blob/master/base_helper.py) und passen Sie die Konfiguration an.  
  
`    # Use this for http`  
`    odoo_address = '0.0.0.0'`  
`    odoo_port = 8069`  
`    user = 'admin'`  
`    pw = 'dbpassword'`  
`    db = 'dbname'`  
`    protocol = 'jsonrpc'`  
  
----
*Powered by*
*Equitania Software GmbH*
*Weiherstrassse 13*
*75173 Pforzheim*
*Germany - Deutschland*
*www.myodoo.de / www.equitania.de*

----
  
[Odoo Kochbuch](https://leanpub.com/odoo-kochbuch/read_sample)  
  
Weitere Informationen unter [Myodoo.de](https://www.myodoo.de) und im [Wiki](https://equitania.atlassian.net/wiki/spaces/MW/overview).  