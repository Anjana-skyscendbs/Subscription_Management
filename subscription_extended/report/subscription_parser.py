from odoo import models, api


class SubscriberReport(models.AbstractModel):
    _inherit = 'report.subscription_managaement.report_subscriber'

    @api.model
    def _get_report_values(self, docids, data=None):
        res = super()._get_report_values(docids, data=data)
        res.update({
            'inherit_variable': 'Inherited Variable'
        })
        return res