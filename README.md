# OdooRPC-Guide
Hier erklären wir wie man mittels OdooRPC Daten in Odoo mittels WEB-API importieren kann.  
  
Unterstützte Funktionen:  
- Zugriff auf alle Datenmodellmethoden (auch Browse) mit einer API, die der serverseitigen API ähnelt,  
- Verwendung benannter Parameter mit Modellmethoden,  
- automatisches Senden des Benutzerkontextes mit Unterstützung für die Internationalisierung,  
- Durchsuchen von Datensätzen,  
- Ausführen von Workflows,  
- Datenbanken verwalten,  
- Herunterladen von Berichten,  
- JSON-RPC-Protokoll (SSL unterstützt),  

  
## Voraussetzungen 
* Python 3.6 oder höher  
* OdooRPC https://pypi.org/project/OdooRPC/ Dokumentation https://pythonhosted.org/OdooRPC/  `pip install odoorpc`  
* odoorpc-toolbox `pip install odoorpc-toolbox`  
  
## Skripte  
* [base_helper.py](https://github.com/equitania/OdooRPC-Guide/blob/master/base_helper.py) - Dieses Skript stellt die Verbindung zum Odoo Server her und stellt einige Hilfsklassen zur Verfügung.
* [get_country_id.py](https://github.com/equitania/OdooRPC-Guide/blob/master/get_country_id.py) - Dieses Skript stellt Hilfsklassen für Länderkodierung von Odoo zur Verfügung.
* [main_addresses.py](https://github.com/equitania/OdooRPC-Guide/blob/master/main_addresses.py) - Dieses Skript importiert Hauptadressen aus einen CSV Datei.
* [products.py](https://github.com/equitania/OdooRPC-Guide/blob/master/products.py) - Dieses Skript importiert Produkte aus einen CSV Datei.
* [product_uom.py](https://github.com/equitania/OdooRPC-Guide/blob/master/product_uom.py) - Dieses Skript erzeugt neue Mengeneinheiten für Produkte.
* [ir_config_parameter.py](https://github.com/equitania/OdooRPC-Guide/blob/master/ir_config_parameter.py) - Dieses Skript demonstiert Konfigurationsparameter anzupassen.
* [ir_cron.py](https://github.com/equitania/OdooRPC-Guide/blob/master/ir_cron.py) - Dieses Skript demonstiert Cronjobs anzupassen.
* [set_ir_actions_report.py](https://github.com/equitania/OdooRPC-Guide/blob/master/set_ir_actions_report.py) - Dieses Skript demonstiert wie man die Dateinamen von Druckdokumenten anpasst und diese im Datesystem automatisch speichert.
* [systeminfo.py](https://github.com/equitania/OdooRPC-Guide/blob/master/systeminfo.py) - Dieses Skript demonstiert wie man Systeminformationen ausliest.  
  
## Start
Öffnen Sie die Yamal config.yaml und passen Sie die Konfiguration an.
  
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