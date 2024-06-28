from odoo import models, fields, api


class subscriber_analysis(models.Model):

    _name = 'subscriber.analysis'
    _auto = False

    # The fields have to be defined same as used in query except id.
    name = fields.Char('Subscriber Name', translate=True)
    age = fields.Integer('Age')

    @api.model
    def init(self):
        self.env.cr.execute("""create or replace view subscriber_analysis as (
            SELECT su.id,
                   su.name,
                   su.age
            FROM subscription_user su) 
        """)