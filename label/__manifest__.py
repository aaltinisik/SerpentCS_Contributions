<<<<<<< HEAD
# -*- coding: utf-8 -*-
=======
>>>>>>> upstream/12.0
# See LICENSE file for full copyright and licensing details.
{
    "name": "Mass Label Reporting",
    "version": "12.0.1.0.0",
    "category": "Tools",
    "license": "AGPL-3",
    "summary": "Generate customised labels of any document",
    "author": 'Serpent Consulting Services Pvt. Ltd.',
    "website": "http://www.serpentcs.com",
<<<<<<< HEAD
    "summary": "Generate customised labels of any document",
    "description": """
    The video : https://www.youtube.com/watch?v=Fps5FWfcLwo
    """,
    'depends': ['report'],
=======
    "maintainer": 'Serpent Consulting Services Pvt. Ltd.',
    'depends': ['base'],
>>>>>>> upstream/12.0
    'data': [
        'data/report_paperformat.xml',
        'security/label.brand.csv',
        'security/label.config.csv',
        'security/ir.model.access.csv',
        'views/label_config_view.xml',
        'views/label_print_view.xml',
        'views/label_size_data.xml',
        'wizard/label_print_wizard_view.xml',
        'views/label_report.xml',
        'report/dynamic_label.xml'
    ],
    'uninstall_hook': 'uninstall_hook',
    'images': ['static/description/Label.png'],
    'installable': True,
    'auto_install': False,
}
