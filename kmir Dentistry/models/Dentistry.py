from odoo import models, fields, api


class Patient(models.Model):
    _inherit = 'res.partner'

    dentistry_treatments = fields.One2many(
        'dentistry.treatment', 'patient', string='Treatments')
    dental_schema = fields.Text('Dental Schema')
    dental_schema_primary = fields.Text('Primary Schema')
    teeth1 = fields.Char('Quadrant 1', compute='_compute_teeth_status')
    teeth2 = fields.Char('Quadrant 2', compute='_compute_teeth_status')
    teeth3 = fields.Char('Quadrant 3', compute='_compute_teeth_status')
    teeth4 = fields.Char('Quadrant 4', compute='_compute_teeth_status')
    use_primary_schema = fields.Boolean('Primary Schema')
    teeth5 = fields.Char('Quadrant 5', compute='_compute_teeth_status_primary')
    teeth6 = fields.Char('Quadrant 6', compute='_compute_teeth_status_primary')
    teeth7 = fields.Char('Quadrant 7', compute='_compute_teeth_status_primary')
    teeth8 = fields.Char('Quadrant 8', compute='_compute_teeth_status_primary')
    dmft_index = fields.Integer('DMFT Index', compute='_compute_dmft_index')
    dmft_index_primary = fields.Integer('dmft index', compute='_compute_dmft_index_primary')

    @api.depends('dental_schema')
    def _compute_teeth_status(self):
        for patient in self:
            if not patient.dental_schema:
                patient.teeth1 = ''
                patient.teeth2 = ''
                patient.teeth3 = ''
                patient.teeth4 = ''
            else:
                # Compute teeth status for quadrants 1, 2, 3, 4
                # Implement the logic to compute the teeth status here

    @api.depends('dental_schema_primary')
    def _compute_teeth_status_primary(self):
        for patient in self:
            if not patient.dental_schema_primary:
                patient.teeth5 = ''
                patient.teeth6 = ''
                patient.teeth7 = ''
                patient.teeth8 = ''
            else:
                # Compute teeth status for quadrants 5, 6, 7, 8
                # Implement the logic to compute the teeth status here

    @api.depends('dental_schema')
    def _compute_dmft_index(self):
        for patient in self:
            if not patient.dental_schema:
                patient.dmft_index = 0
            else:
                # Compute DMFT index for dental_schema
                # Implement the logic to compute the DMFT index here

    @api.depends('dental_schema_primary')
    def _compute_dmft_index_primary(self):
        for patient in self:
            if not patient.dental_schema_primary:
                patient.dmft_index_primary = 0
            else:
                # Compute DMFT index for dental_schema_primary
                # Implement the logic to compute the DMFT index here


class DentistryTreatment(models.Model):
    _name = 'dentistry.treatment'

    patient = fields.Many2one('res.partner', string='Patient', required=True)
    treatment_date = fields.Date('Date', default=fields.Date.context_today)
    healthprof = fields.Many2one('res.partner', string='Health Professional')
    procedures = fields.One2many('dentistry.treatment.procedure', 'treatment', string='Procedures')
    notes = fields.Text('Notes')
    state = fields.Selection([('pending', 'Pending'), ('done', 'Done')], 'State', default='pending')
    signed_by = fields.Many2one('res.partner', string='Signed by')

    @api.onchange('state')
    def _onchange_state(self):
        # Perform actions when the state field changes
        pass

    def load_procedure(self):
        # Perform actions when loading procedures
        pass

    def set_odontogram(self):
        # Perform actions to set odontogram
        pass

    def end_treatment(self):
        # Perform actions to end treatment
        pass


class DentistryProcedure(models.Model):
    _name = 'dentistry.procedure'

    name = fields.Char('Procedure', required=True, translate=True)
    code = fields.Char('Code', required=True, translate=True)


class TreatmentProcedure(models.Model):
    _name = 'dentistry.treatment.procedure'

    treatment = fields.Many2one('dentistry.treatment', string='Treatment', required=True)
    tooth = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], string='Tooth')
    procedure = fields.Many2one('dentistry.procedure', string='Procedure', required=True)
    root = fields.Boolean('Root')
    occlusal = fields.Boolean('Occlusal')
    vestibular = fields.Boolean('Vestibular')
    lingual = fields.Boolean('Lingual')
    mesial = fields.Boolean('Mesial')
    distal = fields.Boolean('Distal')
