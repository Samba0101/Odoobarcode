{
    'name': 'Generate Barcode from Product(EAN 13)',
    'version': '17.0.0.0.1',
    'summary': "Generate Barcode from product",
    'category': 'Sales',
    'description': """Generate automatic and manual barcode for products, Generate barcode for barcode, Generate Barcode in odoo
    barcode for product in odoo16, barcode on product, ean13 barcode on product. 
    """,
    'author': 'Captivea',
    'website': 'http://www.captivea.com/',
    'depends': ['base', 'product', 'sale', 'barcodes'],
    'data': [
        'security/ir.model.access.csv',
        'views/barcode_generate_view.xml',
        'views/res_config_view.xml'
    ],
    'demo': [

    ],
    'assets': {

    },
    'images': ['static/description/banner.gif', 'static/description/img/icon.png'],
    'price': 0.0,
    'license': 'OPL-1',
    'currency': 'EUR',
    'installable': True,
    'application': False,
    'auto_install': False,
    'pre_init_hook': '',
    'post_init_hook': '',
    'post_init_hook': '',
}