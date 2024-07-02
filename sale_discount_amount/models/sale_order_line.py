from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    discount_amount = fields.Monetary(string='Discount Amount', compute='_compute_discount_amount', store=True)

    @api.depends('price_unit', 'product_uom_qty', 'discount')
    def _compute_discount_amount(self):
        for line in self:
            line.discount_amount = (line.price_unit * line.product_uom_qty * line.discount) / 100

    @api.onchange('discount')
    def _onchange_discount(self):
        if self.discount:
            self.discount_amount = (self.price_unit * self.product_uom_qty * self.discount) / 100

    def _prepare_invoice_line(self, **optional_values):
        res = super(SaleOrderLine, self)._prepare_invoice_line(**optional_values)
        res['discount_amount'] = self.discount_amount
        return res
