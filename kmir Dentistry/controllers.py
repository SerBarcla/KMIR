from odoo import http
from odoo.http import request


class DentistryController(http.Controller):

    @http.route('/dentistry/load_procedure', type='http', auth='user', website=True)
    def open_load_procedure_wizard(self):
        # Create a new instance of the wizard model
        wizard = request.env['kmir.load_procedure.wizard'].create({})

        # Render the wizard form view
        return request.render('your_module.kmir_load_procedure_start_form', {
            'wizard': wizard,
        })


class KmirDentistryController(http.Controller):

    @http.route('/kmir/dentistry/set_odontogram', type='json', auth='user')
    def set_odontogram_start(self):
        # Create a new record for the KmirDentistryOdontogram model
        odontogram_obj = request.env['kmir.dentistry.odontogram']
        odontogram = odontogram_obj.create({})

        # Return the ID of the created record
        return {'odontogram_id': odontogram.id}