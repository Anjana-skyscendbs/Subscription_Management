
from odoo import models, fields, api

from datetime import date


class SubscriptionCloseWizard(models.TransientModel):
    _name = 'subscription.close.wizard'
    _description = 'Subscription Close Wizard'


    user_id = fields.Many2one('subscription.user','User')
    close_reason = fields.Many2one('subscription.package.stop', string='Close Reason')
    # closed_by = fields.Many2one('res.users', string='Closed By')
    closed_by = fields.Reference([('subscription.user', ' Subscribers'),
                            ('res.users', 'Users'),
                            ('res.partner', 'Contacts')],'Closed By')
    close_date = fields.Date(string='Closed On', default=lambda self: fields.Date.today())
    active = fields.Boolean('Active', help='This field is used to activate or deactivate a record', default=True)

    def button_submit(self):
        # today = date.today()
        # for record in self:
        #     if record.close_date and record.close_date <= today:
        #         record.active = False
        #     else:
        #         record.active = True

        user_obj = self.env['subscription.user']
        print("SELF CONTEXT,#########", self._context)
        print("ENV CONTEXT,#########", self.env.context)
        if self.user_id.ids:
            user = self.user_id
        else:
            user = user_obj.browse(self._context.get('active_id'))
        user.write({'active': self.active})