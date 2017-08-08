# -*- coding: utf-8 -*-

{
    'name': 'website tupulperia',
    'category': 'Hidden',
    'summary': 'website tupulperia',
    'version': '1.0',
    'description': """website tupulperia""",
    'author': 'Moldeo Interactive - www.moldeointeractive.com.ar',
    'depends': ['base','website','website_sale','product','partner_person','payment'],
    'data': [
        'views/tu_website_view.xml',
	'views/templates.xml'
    ],
    'qweb': [
    ],
    'installable': True,
}
