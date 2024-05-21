from odoo import fields,models,api


class SubscriptionType(models.Model):
    _name = 'subscription.type'
    _description = 'Types'

    name = fields.Char('Name', required=True)
    code = fields.Char('Code', required=True)

    def name_get(self):
        """
        Overridden name_get() to display name and code both
        ---------------------------------------------------
        @param self: object pointer
        return : A list of tuple containing id and string
        """
        sub_list = []
        for sub in self:
            std_str = ''
            if sub.code:
                std_str += '[' + sub.code + '] '
            std_str += sub.name
            sub_list.append((sub.id,std_str))
        return sub_list












