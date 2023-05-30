{
    'name': 'Dentistry',
    'version': '1.0',
    'author': 'Mr Barcla',
    'category': 'Services/Medical',
    'depends': [
        'base',
        # Add other dependencies if needed
    ],
    'data': [
        'views/kmir_dentistry_procedure_form.xml',
        'views/kmir_dentistry_procedure_tree.xml',
        'views/kmir_dentistry_treatment_form.xml',
        'views/kmir_dentistry_treatment_tree.xml',
        'views/kmir_dentistry_treatment_procedure_form.xml',
        'views/kmir_dentistry_treatment_procedure_tree.xml',
        'views/kmir_load_procedure_start_form.xml',
        'views/kmir_set_odontogram_start_form.xml',
        'views/kmir_dentistry_odontogram_form.xml',
        'views/odontogram_widget.xml',
        'views/Dentistry_views.xml.xml',
        'security/ir.model.security.csv',
        'security/dentistry_security.xml',
        
        # Add other XML files as needed
    ],
    'qweb': [
        'static/src/xml/odontogram_widget.xml',
    ],
    'js': [
        'static/src/js/odontogram_widget.js',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
