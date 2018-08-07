# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.
{
   "name": "Stock Adjustment Barcode Scanner",

    'author' : 'Softhealer Technologies',
    
    'website': 'https://www.softhealer.com',
        
    'version': '11.0.1',
        
    "category": "Warehouse",

    "summary": "This module useful to do stock inventory adjustment operation by barcode scanner.",   
        
    'description': """Do your time wasting in stock inventory adjustment operations by manual product selection ?
                So here is the solutions this modules useful do quick operations of stock inventory adjustment barcode scanner.
                You no need to select product and do one by one. 
                scan it and you done!
                So be very quick in all operations of odoo and cheers!""",
    
    "depends": ['barcodes','stock'],
    
    "data": [
        'views/stock_inventory_template.xml',
    ],    
    'images': ['static/description/background.png',],            
    
    "installable": True,    
    "application": True,    
    "autoinstall": False,
    "price": 10,
    "currency": "EUR"        
}
