from odoo import fields,models,api
from datetime import timedelta


class AddSubscription(models.Model):
    _name ='subscription.addsubscription'
    _description = 'Add Subscription'

    type_id = fields.Many2one('subscription.type', 'Subscription', required=True)
    plan_id = fields.Many2one('subscription.plan', 'Plan', required=True)
    price_depend = fields.Float(compute='_compute_price_depend', string='Price')
    start_date = fields.Date(string='Start Date',default =fields.Date.today())
    expire_date = fields.Date(compute='_compute_price_depend', string='Expire Date')
    user_id =fields.Many2one('subscription.user', 'User', ondelete='cascade')



    @api.depends('type_id', 'plan_id','start_date','expire_date')
    def _compute_price_depend(self):
        for user in self:
            if user.type_id and user.plan_id:
                plan_code = user.plan_id.code.lower()
                if plan_code == 'monthly':
                    user.price_depend = user.type_id.monthly_price
                elif plan_code == 'daily':
                    user.price_depend = user.type_id.daily_price
                elif plan_code == 'weekly':
                    user.price_depend = user.type_id.weekly_price
                elif plan_code == 'yearly':
                    user.price_depend = user.type_id.yearly_price

                else:
                    user.total_price = total
                    user.price_depend = 0.0
            else:
                user.price_depend = 0.0


#  user.expire_date = user.start_date + timedelta(days=30)
# user.expire_date = user.start_date + timedelta(days=7)
# user.expire_date = user.start_date + timedelta(days=365)