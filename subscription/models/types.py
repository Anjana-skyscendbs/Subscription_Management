from odoo import fields,models


class Subject(models.Model):
    _name = 'subscription.types'
    _description = 'Types'

    _rec_name = 'sub_name'

    sub_name = fields.Char('Name')
    code = fields.Char('Code')


class SchoolExam(models.Model):
    _name ='subscription.subtype'
    _description = 'Sub Type'

    type_id = fields.Many2one('subscription.types', 'Types')
    month = fields.Float('Monthly Price')
    year = fields.Float('Yearly Price')
    day = fields.Float('Daily Price')
    week =fields.Float('Weekly Price')
    student_id = fields.Many2one('subscriber.plan', 'Subscriber', ondelete='cascade')
    # student_id is the inverse field for O2M field exam_ids in student
    # ondelete='cascade' will delete all (current model)exam records if (comodel) student record is deleted.

