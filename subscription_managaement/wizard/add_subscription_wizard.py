from odoo import models, fields, api

class AddSubscriptionWizard(models.TransientModel):
    _name = 'add.subscription.wizard'
    _description = 'Add Subscription Wizard'

    user_id = fields.Many2one('subscription.user', string='User', required=True)
    subscription_lines = fields.One2many('add.subscription.wizard.line', 'wizard_id', string='Subscription Lines')

    def action_add_subscriptions(self):
        for wizard in self:
            for line in wizard.subscription_lines:
                self.env['subscription.addsubscription'].create({
                    'user_id': wizard.user_id.id,
                    'sub_type': line.sub_type.id,
                    'recurrence_id': line.recurrence_id.id,
                    'start_date': line.start_date,
                    'price': line.price,
                })
        return {'type': 'ir.actions.act_window_close'}


class AddSubscriptionWizardLine(models.TransientModel):
    _name = 'add.subscription.wizard.line'
    _description = 'Add Subscription Wizard Line'

    wizard_id = fields.Many2one('add.subscription.wizard', string='Wizard')
    sub_type = fields.Many2one('subscription.subtype', string='Subscription Type', required=True)
    recurrence_id = fields.Many2one('subscription.recurrence', string='Plan', required=True)
    start_date = fields.Date(string='Start Date', default=fields.Date.today)
    price = fields.Float(string='Price', required=True)
