from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    aadhar_number = fields.Char(string='Aadhar Number', help='Employee Aadhar Number')
    pan_number = fields.Char(string='PAN Number', help='Employee PAN Number')