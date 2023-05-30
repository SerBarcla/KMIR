from odoo import fields, models

class KmirDentistryOdontogram(models.Model):
    _name = 'kmir.dentistry.odontogram'
    _description = 'Odontogram'

    # Define the fields to store tooth-related information
    # Example fields, modify as per your requirements
    tooth_number = fields.Char(string='Tooth Number')
    condition = fields.Selection([
        ('healthy', 'Healthy'),
        ('cavity', 'Cavity'),
        ('missing', 'Missing'),
        # Add more options as needed
    ], string='Condition')
    vitality = fields.Boolean(string='Vitality')
    mobility = fields.Selection([
        ('normal', 'Normal'),
        ('mild', 'Mild'),
        ('severe', 'Severe'),
        # Add more options as needed
    ], string='Mobility')
    # Add more fields as per your requirements
