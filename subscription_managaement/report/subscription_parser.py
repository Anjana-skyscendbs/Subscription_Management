from odoo import models, fields, api


class SubscriberReport(models.AbstractModel):
    _name = 'report.subscription_managaement.report_subscriber'  # name of your reports
    _description = 'Subscriber Profile Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        print("\n\n\n\n\nDOC IDS", docids)
        print("SELF", self.ids)
        print("CONTEXT", self._context)
        print("DATA", data)
        # docs = self.env['subscription.user'].browse(docids)
        if not docids:
            docids = self._context.get('active_ids')
        docs = self.env['subscription.user'].browse(docids)


        return {
            'doc_ids': docids,
            'doc_model': 'subscription.user',
            'data': data,
            'docs': docs,
            'test': 'TEST VARIABLE',
            'anjum': 'manager',
            'anjana': 'subscriber',
            'get_total_subscriptions': self.get_total_subscriptions,
        }

    @api.model
    def get_total_subscriptions(self, prices):
        total_price = 0.0
        for dtl in prices:
            total_price += dtl.price
        return total_price
