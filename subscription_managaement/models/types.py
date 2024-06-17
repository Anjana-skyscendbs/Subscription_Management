from odoo import fields,models,api


class SubscriptionType(models.Model):
    _name = 'subscription.type'
    _description = 'Types'

    name = fields.Char('Name', required=True)
    code = fields.Char('Code', required=True)
    # color = fields.Integer('Color')

    def name_get(self):
        """
        Overridden name_get() to display name and code both
        ---------------------------------------------------
        @param self: object pointer
        return : A list of tuple containing id and string
        """
        # todo 9. Override name_get method and display two fields rather than just name in the many2one field.
        sub_list = []
        print("SUB_LIST",sub_list)
        for sub in self:
            std_str = ''
            if sub.code:
                std_str += '[' + sub.code + '] '
            std_str += sub.name
            st = sub_list.append((sub.id,std_str))
            print("ST",st)
        return sub_list

    # todo 11.Override name_create method to add additional fields for creating records.
    @api.model
    # def name_create(self, name):
    #     vals = {
    #         'name': name,
    #         'code': name[:3].upper()
    #     }
    #     subtype = self.create(vals)
    #     return subtype.name_get()[0]

    def name_create(self,name):
        print("Self ",self)
        print("Subscription Name  ",name)
        rtn = self.create({'name':name})
        print("RTN ",rtn)
        print("rtn.name_get()[0]",rtn.name_get()[0])
        return rtn.name_get()[0]












