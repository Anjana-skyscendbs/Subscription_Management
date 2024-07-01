from odoo import models, fields


class SubscriptionPackageStopReason(models.Model):
    _name = "subscription.package.stop"
    _description = "Subscription Package Stop Reason"
    _order = 'sequence'

    sequence = fields.Integer(help="Determine the display order", index=True,
                              string='Sequence')
    name = fields.Char(string='Reason', required=True)
