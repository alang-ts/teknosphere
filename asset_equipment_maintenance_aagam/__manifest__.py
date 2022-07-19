{
	'name':'Asset Equipment Maintenance, Machine Repair/Maintenance, Auto parts, Car Maintenance - All in one Maintenance',
    'version': '15.0.0.1',
    'description': 'Asset Equipment Maintenance, Job order create maintenance request, checklist - All in one Maintenance auto maintenance in odoo 15, 14, 13, 12', 
    'summary':'Asset Equipment Maintenance Repair Operation, Job order create maintenance request, Machine Repair machine Maintenance vehicle maintenance MRO Equipment Maintenance Management - All in one asset Maintenance auto maintenance car maintenance car repair in odoo 15,14, 13, 12',
	'depends': ['hr_maintenance','stock','project','purchase_requisition'],
	'data': [
		'security/ir.model.access.csv',
        'data/maintenance_stage.xml',
		'data/maintenance_inprogress.xml',
		'data/maintenace_repaire_mail.xml',
		'data/maintenance_scrap_mail.xml',
        'view/maintenance_request_view.xml',
        'view/job_order_view.xml',
        'view/res_config_view.xml',
        'view/maintenance_checklist.xml',
        'view/maintenance_equipment.xml',
        'view/purchase_requisition.xml',
		'view/maintenance_dashboard.xml',
		# 'view/assets.xml',
    ],
    # 'qweb': [
        # 'static/src/xml/maintenance_dashboard.xml'
        #      ],
    'images': [
        'static/description/banner.jpg',
    ],

    'installable': True,
    'assets': {

        'web.assets_qweb': [
            'asset_equipment_maintenance_aagam/static/src/xml/maintenance_dashboard.xml',
        ],
        'web.assets_backend': [

            '/asset_equipment_maintenance_aagam/static/src/js/maintenance_dashboard.js',
            '/asset_equipment_maintenance_aagam/static/src/js/jquery.dataTables.min.js',
            '/asset_equipment_maintenance_aagam/static/src/js/datatables.min.js',
            '/asset_equipment_maintenance_aagam/static/src/js/dataTables.buttons.min.js',

            '/asset_equipment_maintenance_aagam/static/src/js/Chart.js',
            '/asset_equipment_maintenance_aagam/static/src/css/nv.d3.css',
            'https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css',
            'asset_equipment_maintenance_aagam/static/src/scss/new_css.css',
        ],


    },

    'auto_install': False,
    'support': 'business@aagaminfotech.com',
    'author': 'Aagam Infotech',
    'website': 'http://www.aagaminfotech.com',
    'license': 'OPL-1',
    'price': 89.00,
    'currency': 'USD',
}