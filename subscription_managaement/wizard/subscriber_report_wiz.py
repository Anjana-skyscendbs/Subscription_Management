from odoo import models, fields


class StudentReportWizard(models.TransientModel):
    _name = 'subscriber.report.wiz'

    type_id = fields.Many2one('subscription.type', 'Subscription')#,domain=[('name','=','Streaming Service')]

    def print_report(self):

        user_obj = self.env['subscription.user']
        users = user_obj.search([('type_id', '=', self.type_id.ids)])
        data = {}
        data['form'] = self.read()[0]
        if not users:
            #TODO: Raise a Validation Error
            pass
        return self.env.ref('subscription_managaement.action_report_subscriber').report_action(users, data=data)


