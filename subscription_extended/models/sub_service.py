from odoo import models, fields, api


class SubService(models.Model):
    # For Delegate Inheritance _inherits can be used.
    # The _inehrits takes a dictionary.
    # The key will be the name of the model.
    # The value will be an M2O field for the same model in current model.
    _inherits= {'subscription.service': 'service_id'}
    _name = 'subscription.sub.service'

    # The M2O field for the parent model for delegation.
    # It must have the required=True and ondelete='cascade'
    service_id = fields.Many2one('subscription.service', 'Service', required=True, ondelete='cascade')
    sub_ser_name = fields.Char('Sub Service Name')
    sub_ser_code = fields.Char('Sub Service Code')



class SubService2(models.Model):
    # For Delegate Inheritance delegate=True can also be used.
    _name = 'subscription.sub.service2'

    # The M2O field for the parent model for delegation.
    # It will have delegate=True instead of _inherits
    # It must have the required=True and ondelete='cascade'
    service_id = fields.Many2one('subscription.service',
                                  'Service',
                                  delegate=True,
                                  required=True,
                                  ondelete='cascade')
    sub_ser_name = fields.Char('Sub Service Name')
    sub_ser_code = fields.Char('Sub Service Code')