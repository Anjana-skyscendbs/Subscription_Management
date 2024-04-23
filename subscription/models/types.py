from odoo import fields,models,api


class Types(models.Model):
    _name = 'subscription.types'
    _description = 'Types'

    _rec_name = 'sub_name'

    sub_name = fields.Char('Name')
    code = fields.Char('Code')
    month = fields.Float('Monthly Price')
    year = fields.Float('Yearly Price')
    day = fields.Float('Daily Price')
    week = fields.Float('Weekly Price')


class Subtype(models.Model):
    _name ='subscription.subtype'
    _description = 'Sub Type'

    type_id = fields.Many2one('subscription.types', 'Types')
    month = fields.Float('Monthly Price')
    year = fields.Float('Yearly Price')
    day = fields.Float('Daily Price')
    week = fields.Float('Weekly Price')
    subscriber_id = fields.Many2one('subscriber.plan', 'Subscriber', ondelete='cascade')
    # student_id is the inverse field for O2M field exam_ids in student
    # ondelete='cascade' will delete all (current model)exam records if (comodel) student record is deleted.
    perc = fields.Float(compute='_calc_perc', string='Percentage(%)', store=True)

 # If you use the decorator api.depends it will be called as soon as you change the fields which are mentioned in the decorator
    @api.depends('month', 'year')
    def _calc_perc(self):
        """
        This method will calculate the percentage of your obtained marks
        ----------------------------------------------------------------
        @param self: object pointer / recordset
        """
        # self is a recordset which can be a blank object
        # or it can contain one or more records
        print("SELF", self)
        # You can iterate self considering the method can be called using multiple records.
        for subtypes in self:
            # NOTE: IT IS MANDATORY TO ASSIGN THE VALUE TO THE FIELD FOR WHICH YOU HAVE CREATED THE COMPUTE METHOD
            perc = 0.0
            print("EXAM", subtypes)
            # Using '.' notation you can access fields and methods of this object.
            print("TOTAL MARKS", subtypes.month)
            # Relational field when accessed gives you the recrodset of the selected value.
            print("SUBJECT", subtypes.type_id)
            print("SUBJECT NAME", subtypes.type_id.sub_name)
            if subtypes.month > 0:
                # NOTE: ALWAYS CHECK THE VALUE WITH WHICH YOU ARE TRYING TO DIVIDE TO AVOID ZERO DIVISION ERROR!!!
                perc = subtypes.year * 100 / subtypes.month
            subtypes.perc = perc