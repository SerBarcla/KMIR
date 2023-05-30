from odoo import models, fields, api


class LoadProcedureWizard(models.TransientModel):
    _name = 'kmir.load_procedure.wizard'

    procedure = fields.Selection([
        ('procedure1', 'Procedure 1'),
        ('procedure2', 'Procedure 2'),
        # Add more procedure options as needed
    ], string='Procedure', required=True)

    # Add more fields as needed

    @api.multi
    def load_procedure(self):
        # Implement the logic when the user confirms the wizard
        selected_procedure = self.procedure
        # Perform actions based on the selected procedure
        # For example, create a new record in the Dentistry Procedure model
