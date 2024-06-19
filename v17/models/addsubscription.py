from odoo import fields,models,api
from dateutil.relativedelta import relativedelta


class AddSubscription(models.Model):
    _name ='subscription.addsubscription'
    _description = 'Add Subscription'

    # type_id = fields.Many2one('subscription.type', 'Subscription')#  required=True

    #
    service =fields.Many2one('subscription.service','Subscription Type')
    # print(service.type_id,"============================")

    plan_id = fields.Many2one('subscription.plan', 'Plan')# , required=True
    start_date = fields.Date(string='Start Date',default =fields.Date.today())
    expire_date = fields.Date(string='Expire Date',compute='_compute_expire_date', store=True)
    currency_id = fields.Many2one('res.currency', 'Currency')
    price = fields.Monetary(currency_field='currency_id', string='Price')
    user_id = fields.Many2one('subscription.user', 'User', ondelete='cascade')

    @api.depends('plan_id', 'start_date')
    def _compute_expire_date(self):
        for rec in self:
            if rec.plan_id.code == 'MH':
                rec.expire_date = rec.start_date + relativedelta(months=1)
            elif rec.plan_id.code == 'QH':
                rec.expire_date = rec.start_date + relativedelta(months=3)
            elif rec.plan_id.code == 'WH':
                rec.expire_date = rec.start_date + relativedelta(weeks=1)
            elif rec.plan_id.code == 'WH2':
                rec.expire_date = rec.start_date + relativedelta(weeks=2)
            elif rec.plan_id.code == 'YH':
                rec.expire_date = rec.start_date + relativedelta(years=1)
            elif rec.plan_id.code == 'YH3':
                rec.expire_date = rec.start_date + relativedelta(years=3)
            elif rec.plan_id.code == 'YH5':
                rec.expire_date = rec.start_date + relativedelta(years=5)
            else:
                rec.expire_date = False

    @api.model
    def _expired_subscriptions(self):
        today = date.today()
        expired_subscriptions = self.env['subscription.addsubscription'].search([
            ('expire_date', '<', today)
        ])
        return expired_subscriptions

    is_expired = fields.Boolean(compute='_compute_is_expired', search='_search_is_expired')

    @api.depends('expire_date')
    def _compute_is_expired(self):
        today = date.today()
        for rec in self:
            rec.is_expired = rec.expire_date and rec.expire_date < today

    def _search_is_expired(self, operator, value):
        expired_subscriptions = self._expired_subscriptions()
        if operator == '=':
            return [('id', 'in', expired_subscriptions.ids)] if value else [('id', 'not in', expired_subscriptions.ids)]
        else:
            return [('id', 'not in', expired_subscriptions.ids)] if value else [('id', 'in', expired_subscriptions.ids)]




    # todo 10.Override name_search method to search with both the fields which are displayed in many2one field.
    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        print("Name : -", name)
        print("Args : -", args)
        print("Operator : -", operator)
        print("Limit : - ", limit)
        if name:
            records = self.search(['|', '|', '|', ('name', operator, name), ('unit', operator, name),
                                   ('code', operator, name), ('duration', operator, name)])
            return records.name_get()
        return self.search([('name', operator, name)] + args, limit=limit).name_get()

    def name_create(self, name):
        print("Self ", self)
        print("Subscription Name  ", name)
        rtn = self.create({'name': name})
        print("RTN ", rtn)
        print("rtn.name_get()[0]", rtn.name_get()[0])
        return rtn.name_get()[0]







    # price = fields.Float('Price')
    # month_price = fields.Float('Monthly Price')
    # quarterly_price = fields.Float('Quarterly Price')
    # week_price = fields.Float('Weekly Price')
    # week_2_price = fields.Float('2 Weekly Price')
    # year_price = fields.Float('Yearly Price')
    # year_3_price = fields.Float('3 Yearly Price')
    # year_5_price = fields.Float('5 Yearly Price')


# 1. type_id(subscription)many2one
# 2. subscription(sub type)many2one
# 2. plan_id(month ,yearly)many2many
# 3.start date
# 4. end date
# 5. price depend one plan
# if select multiple plan than add multiple price
# 6.add price base of plan
# 7.month price
# weekly
# quartly
# 2 week
# 1 year
# 3 year
# 5 year




    # @api.depends('type_id', 'plan_id')
    # def _compute_price_depend(self):
    #     for user in self:
    #         if user.type_id and user.plan_id:
    #             plan_code = user.plan_id.code.lower()
    #             if plan_code == 'MH':
    #                 user.price_depend = user.type_id.monthly_price
    #             elif plan_code == 'daily':
    #                 user.price_depend = user.type_id.daily_price
    #             elif plan_code == 'weekly':
    #                 user.price_depend = user.type_id.weekly_price
    #             elif plan_code == 'yearly':
    #                 user.price_depend = user.type_id.yearly_price
    #
    #             else:
#                     # user.total_price = total
#                     user.price_depend = 0.0
#             else:
#                 user.price_depend = 0.0
#
#
#
    def add_rec(self):
        vals1 = {
            'service':3,
            'plan_id':7
        }
            # 0 is used for creation
            # (0,0,{}) used to create record in O2M field
        vals_lst = [vals1]
        # Creating record in the same object
        new_users = self.create(vals_lst)
        print("USERS", new_users)
        return {
            'effect': {
                'fadeout': 'slow',
                'type': 'rainbow_man',
                'message': 'Record has been Added Sucessfully'
            }
        }

    def remove_all_records(self):
        self.unlink()
        return True
#
#
#
# #  user.expire_date = user.start_date + timedelta(days=30)
# user.expire_date = user.start_date + timedelta(days=7)
# user.expire_date = user.start_date + timedelta(days=365)