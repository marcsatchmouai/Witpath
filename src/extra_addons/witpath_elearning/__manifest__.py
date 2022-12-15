# -*- coding: utf-8 -*-
{
    'name': "witpath_elearning",

    'summary': """
       Modulo de e-learning del proyecto witpath
    """,

    'author': "Palonsky - Villalba",
    'website': "http://www.witpath-elearning.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'General',
    'version': '0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'hr'],

    # always loaded
    'data': [
        'data/wp.cursos.csv',
        'data/wp.alumnos.csv',
        'data/wp.alumnos.wp.cursos.rel.csv',
        'data/wp.clases.csv',
        'data/wp.contactos.csv',
        'data/wp.contenido.csv',
        'data/wp.contratos.csv',
        'data/wp.cotizaciones.csv',
        'data/wp.cotizaciones_detalle.csv',
        'data/wp.foros.csv',
        'data/sequence.xml',
        'views/alumnos_view.xml',
        'views/clases_view.xml',
        'views/clientes_view.xml',
        'views/contactos_view.xml',
        'views/contenido_view.xml',
        'views/contratos_view.xml',
        'views/cotizaciones_view.xml',
        'views/cursos_view.xml',
        'views/foros_view.xml',
        'views/cotizacion_detalle_view.xml',
        'views/menu_view.xml',
        'security/witpath_security.xml',
        'security/ir.model.access.csv'

    ],
    'demo': [
        'demo/demo.xml'
    ],
    # only loaded in demonstration mode
    'instalable': True,
    'application': True
}