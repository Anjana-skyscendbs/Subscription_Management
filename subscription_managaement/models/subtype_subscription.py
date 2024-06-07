from odoo import fields,models


class SubscriptionServices(models.Model):
    _name = 'subscription.subtype'
    _description = 'SUb type of Subscription'

    name = fields.Char('Name')
    recurrence_id = fields.Many2many('subscription.recurrence',string='Recurrence Period')
    type_id = fields.Many2one('subscription.type', ' Subscription Type')










    # plan_ids = fields.Many2many('subscription.s', string='Services',ondelete='restrict')
    # plan_ids = fields.Many2many('subscription.subtype', 'sub_ser_rel','sub_id','ser_id',string='Services', ondelete='restrict')

    # currency_id = fields.Many2one('res.currency', 'Currency')
    # # price = fields.(currency_field='currency_id', string='Price Amount')
    # daily_price = fields.Monetary('Daily Price', currency_field='currency_id', required=True)
    # weekly_price = fields.Monetary(compute='_calc_weekly_price', currency_field='currency_id', string='Weekly Price ',
    #                                required=True)
    # monthly_price = fields.Monetary(compute='_calc_weekly_price', currency_field='currency_id',
    #                                 string='Monthly Price with 20 %', required=True)
    # yearly_price = fields.Monetary(compute='_calc_weekly_price', currency_field='currency_id',
    #                                string='Yearly Price with 30 %', required=True)
    #
    # @api.depends('weekly_price', 'daily_price', 'monthly_price', 'yearly_price')
    # def _calc_weekly_price(self):
    #     for price in self:
    #         price.weekly_price = price.daily_price * 7
    #         monthly_calc = price.daily_price * 30
    #         discount = monthly_calc * 20 / 100
    #         price.monthly_price = monthly_calc - discount
    #         yearly_calc = price.daily_price * 365
    #         discount = yearly_calc * 30 / 100
    #         price.yearly_price = yearly_calc - discount
