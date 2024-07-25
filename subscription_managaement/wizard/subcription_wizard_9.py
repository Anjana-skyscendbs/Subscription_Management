from odoo import models, fields, api

class SubscriptionWizard(models.TransientModel):
    _name = 'subscription.wizard'
    _description = 'Subscription Wizard'

    user_id = fields.Many2one('subscription.user', string='User')
    recurrence_id = fields.Many2many('subscription.recurrence', string='Recurrence Period')
    subscription_ids = fields.Many2many('subscription.addsubscription', string='Subscriptions')

    # @api.model
    def default_get(self, fields):
        res = super(SubscriptionWizard, self).default_get(fields)
        active_id = self.env.context.get('active_id')
        if active_id:
            user = self.env['subscription.user'].browse(active_id)
            res['user_id'] = user.id
            res['subscription_ids'] = [(6, 0, user.sub_type_ids.ids)]
        return res

    def action_open_subscriptions(self):
        self.ensure_one()
        if len(self.subscription_ids) == 1:
            # Open form view for single record
            return {
                'name': 'Subscription',
                'type': 'ir.actions.act_window',
                'res_model': 'subscription.addsubscription',
                'res_id': self.subscription_ids.id,
                'view_mode': 'form',
                'view_type': 'form',
                'target': 'current',
            }
        else:
            # Open tree view for multiple records
            return {
                'name': 'Subscriptions',
                'type': 'ir.actions.act_window',
                'res_model': 'subscription.addsubscription',
                'domain': [('id', 'in', self.subscription_ids.ids)],
                'view_mode': 'tree,form',
                'view_type': 'form',
                'target': 'current',
            }