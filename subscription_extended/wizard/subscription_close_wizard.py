
from odoo import models, fields, api

# from datetime import date


class SubscriptionCloseWizard(models.TransientModel):
    _inherit = 'subscription.close.wizard'
    _description = 'Subscription Close Wizard'

    height = fields.Float('Height')
    weight = fields.Float('Weight')
    phone = fields.Char('Phone')

    def button_submit(self):
        # today = date.today()
        # for record in self:
        #     if record.close_date and record.close_date <= today:
        #         record.active = False
        #     else:
        #         record.active = True

        user_obj = self.env['subscription.user']
        super().button_submit()
        print("SELF CONTEXT,#########", self._context)
        print("ENV CONTEXT,#########", self.env.context)
        if self.user_id.ids:
            user = self.user_id
        else:
            user = user_obj.browse(self._context.get('active_ids'))
        user.write({'height': self.height,
            'weight': self.weight,
            'phone' :self.phone})