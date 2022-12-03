# -*- coding: utf-8 -*-
{
    'name': "primer_modulo",

    'summary': """
       Este es un modulo del curso de odoo 14
    """,

    'author': "Palonsky - Villalba",
    'website': "http://www.learning.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'General',
    'version': '0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail', 'hr'],

    # always loaded
    'data': [
        'views/menu_view.xml',
        'views/libros_view.xml',
        'security/ir.model.access.csv'

    ],
    # only loaded in demonstration mode
    'instalable': True,
    'application': True
}