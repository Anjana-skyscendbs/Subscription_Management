from odoo import fields,models,api


class SubscriptionType(models.Model):
    _name = 'subscription.type'
    _description = 'Types'

    name = fields.Char('Name', required=True)
    code = fields.Char('Code', required=True)
    daily_price = fields.Float('Daily Price', required=True)
    weekly_price = fields.Float(compute ='_calc_weekly_price',string ='Weekly Price ', required=True)
    monthly_price = fields.Float(compute ='_calc_weekly_price',string ='Monthly Price with 20 %', required=True)
    yearly_price = fields.Float(compute ='_calc_weekly_price',string ='Yearly Price with 30 %', required=True)

    @api.depends('weekly_price','daily_price','monthly_price','yearly_price')
    def _calc_weekly_price(self):
        for price in self:
            price.weekly_price = price.daily_price * 7
            monthly_calc = price.daily_price * 30
            discount = monthly_calc * 20 /100
            price.monthly_price = monthly_calc - discount
            yearly_calc = price.daily_price * 365
            discount = yearly_calc * 30 / 100
            price.yearly_price = yearly_calc - discount












