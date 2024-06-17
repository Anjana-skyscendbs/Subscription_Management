from odoo import models,fields,api

class Employee(models.Model):
    # If you use _inherit along with _name it will create a new model.
    # _name will be the new model with all features of _inherit
    # All fields will be added in a new table of the new model.
    # This does not change anything in the existing model.
    _inherit = 'subscription.user'
    _name = 'subscription.employee'

    department_ids = fields.Many2many('subscription.type',string='Departments')
    qualification = fields.Char('Qualification')
    # act_ids = fields.Many2many('school.activity','teacher_id','activity_id','teacher_act_rel','Activities')
 # department_ids = fields.Many2many('subscription.type',string='Department')
 #    qualification = fields.Char('Qualification')
 #    recurrence_ids = fields.Many2many('subscription.recurrence','Recurrence')
    salary = fields.Integer('Salary')