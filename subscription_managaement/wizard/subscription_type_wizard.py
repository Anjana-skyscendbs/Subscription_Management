from odoo import models, fields, api

class SubscriptionTypeWizard(models.TransientModel):
    _name = 'subscription.type.wizard'
    _description = 'Subscription Type Wizard'

    type_id = fields.Many2one('subscription.type', string='Subscription Type', required=True)

    def action_find_matching_records(self):
        matching_records = self.env['subscription.user'].search([('type_id', '=', self.type_id.id)])
        return {
            'name': 'Matching Subscribers',
            'type': 'ir.actions.act_window',
            'res_model': 'subscription.user',
            'view_mode': 'tree,form',
            'domain': [('id', 'in', matching_records.ids)],
        }