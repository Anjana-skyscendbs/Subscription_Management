from odoo import models, fields, api, _
from odoo.exceptions import ValidationError,UserError


class Subscriber(models.Model):
    _name = 'subscription.user'
    _description = 'Create User'
    _auto = True
    _inherit=['mail.thread','mail.activity.mixin']
    # _order = 'sequence'

    name = fields.Char(string='Name',  track_visibility="always")#required=True, index=True, translate=True,
    age = fields.Integer('Age',group_operator='avg')# ,compute='_compute_int_field'
    active = fields.Boolean('Active', help='This field is used to activate or deactivate a record', default=True)
    notes = fields.Text('Notes')
    birthdate = fields.Date('Birthdate')
    # timestamp = fields.Datetime('Start Date')
    gender = fields.Selection(selection=[('male', 'Male'),
                                         ('female', 'Female')], string='Gender')
    user_code = fields.Char('User Code', size=4)
    password = fields.Char('Password')
    email = fields.Char('Email')
    phone = fields.Char('Phone')
    photo = fields.Image('Photo')
    ref = fields.Reference([('subscription.user', ' Subscribers'),
                            ('res.users', 'Users'),
                            ('res.partner', 'Contacts')], 'Reference')
    document = fields.Binary('Document')
    file_name = fields.Char('File Name')

    state = fields.Selection([('applied', 'Applied'),
                              ('pending', 'Pending'),
                              ('draft', 'Draft'),
                              ('done', 'Done'),
                              ('left', 'Left')], 'State', default='applied')
    type_id = fields.Many2one('subscription.type', 'Subscription')#,domain=[('name','=','Streaming Service')]
    sub_type_ids = fields.One2many('subscription.addsubscription', 'user_id', 'Subscriptions',ondelete='cascade')
    # service_ids = fields.Many2many('subscription.service', string='Services',ondelete='restrict')
    service_ids = fields.Many2many('subscription.service', 'sub_ser_rel','sub_id','ser_id',string='Services', ondelete='restrict')


    sequence = fields.Integer('Sequence')
    parent_id = fields.Many2one('subscription.user', 'Manager')
    child_ids = fields.One2many('subscription.user', 'parent_id', 'Subordinates')



    total_subscription_price = fields.Float(string='Total Price',
                                            compute='_compute_total_subscription_price', store=True)

    # @api.depends('name')
    # def _compute_int_field(self):
    #     for record in self:
    #         if record.name:
    #             record.age = record.age or False
    #         else:
    #             record.age = False





    @api.depends('sub_type_ids.price')
    def _compute_total_subscription_price(self):
        for user in self:
            user.total_subscription_price = sum(subscription.price for subscription in user.sub_type_ids)

    def print_user(self):
        """
        This is a method of the button to demonstrate the usage of button
        -----------------------------------------------------------------
        @param self: object pointer / recordset
        """
        # TODO: Future development
        print("PRINT")
        print("SELF : -", self)
        print("ENVIRONMENT : -", self.env)
        print("ENVIRONMENT  ATTRS : -", dir(self.env))
        print("ARGS : -", self.env.args)
        print("CURSOR : -", self.env.cr)
        print("UID : -", self.env.uid)
        print("USER : -", self.env.user)
        print("CONTEXT : -",self.env.context)
        print("COMPANY : -",self.env.company)
        print("COMPANIES : -", self.env.companies)
        print("LANG : -", self.env.lang)

        records = self.env['subscription.user'].search([])
        print("Print Records ID",records)

        for user in self:
            mt_dt = user.get_metadata()
            print("MT DT Predefined Fields", mt_dt)

        # Filter the recordset based on a condition
        filtered_records = records.filtered(lambda r: r.age > 25)
        print("filtered_records ID", filtered_records)

        # # Filter the recordset based on a condition using domain syntax
        # domain_filtered_records = records.filtered(domain=[('age', '>', 25)])
        # print("domain_filtered_records ID", domain_filtered_records)

        # Filter the recordset to display only records with a value in the 'active' field
        with_value_records = records.filtered(lambda r: bool(r.active))
        print("with_value_records ID", with_value_records)

        # Get the concatenated value of 'name' and 'age' fields
        result = [f"{r.name}-{r.age}" for r in records]
        print("result name-age", result)

        # Get a list of values in the 'name' field
        field_values = records.mapped('name')
        print("result field_values list ", field_values)

        # Sort the recordset in descending order by the 'name' field
        sort_by_name = records.sorted(key='name', reverse=True)
        print("SORT BY NAME",sort_by_name)

        female_records = records.filtered(lambda r: r.gender == 'female')
        male_records = records.filtered(lambda r:r.gender=='male')
        print("FEMALE RECORDS", female_records)
        print("MALE RECORDS", male_records)

        print("UNION",male_records | female_records)
        print("INTERSECTION",male_records & records)
        print("DIFFERENCE", records - female_records)





        return {
            'effect': {
                'fadeout': 'slow',
                'type': 'rainbow_man',
                'message': 'Print ENV Sucessfully'
            }
        }



    def create_rec(self):
        """
        This is a button method which is used to demonstrate create() method.
        ---------------------------------------------------------------------
        @param self: object pointer
        """

        other_model= self.env['subscription.plan']
        other_model.create({
            'name': 'anjana',
            'code': 'AN'

        })


        vals1 = {
            'name':'Nirupa',
            'active':True,
            'age':22,
            'birthdate':'2001-04-01',
            'type_id':5,
            'gender':'female'
        }
        vals2 = {
            'name': 'lila',
            'active': True,
            'age': 29,
            'birthdate': '1994-05-17',
            'type_id': 5,
            'gender': 'female'
        }
        vals_lst = [vals1,vals2]
        # Creating record in the same object
        new_users = self.create(vals_lst)
        print("USERS", new_users)
        return {
            'effect':{
                'fadeout':'slow',
                'type':'rainbow_man',
                'message':'Record has been Created Sucessfully'
            }
        }



    def update_rec(self):
        """
        Button's method to demonstrate write() method
        """
        vals = {
            'age':30,
            'type_id':4,
            'name':'Dol'

        }
        res = self.write(vals)
        print("RES",res)

        return {
            'effect': {
                'fadeout': 'slow',
                'type': 'rainbow_man',
                'message': 'Record has been Updated Sucessfully'
            }
        }


    def search_rec(self):
        all_users = self.search([])
        # When you pass a blank domain it will return all the records.
        print("ALL USERS",all_users)
        # When you pass offset it will skip no of records from the result
        offset_5_users = self.search([], offset=5 ,limit=3 ,order='name asc')
        print("SKIP 5 RECORDS and LIMIT 3 record show", offset_5_users)
        # records = self.env['subscription.user'].search([], order='name asc')
        # # print("USERS", records)


        ### search_count
        no_of_users = self.search_count([])
        print("TOTAL USERS", no_of_users)
        no_of_female_users = self.search_count([('gender', '=', 'female')])
        print("FEMALE USERS", no_of_female_users)

        return {
            'effect': {
                'fadeout': 'slow',
                'type': 'rainbow_man',
                'message': 'Record has been Search Sucessfully'
            }
        }



    @api.constrains('age')
    def val_age(self):
        for record in self:
            if record.age <=18:
                raise ValidationError(_('The age must be above than 18 years'))

    @api.model
    def unlink(self,vals):
        res = super(Subscriber, self).unlink()
        for vals in self:
            if vals.active == 'active':
                    raise UserError(_("Record cannot be deleted, it is an active state"))
            else:
                return res
        return res



    # @api.model
    # def create(self, vals):
    #     res = super(Subscriber, self).create(vals)
    #     if not vals.get('type_ids'):
    #         raise ValidationError(_("PLease fill the one2many field"))
    #     else:
    #         return res
    #
    #     return res
    #
    #     if vals.get('gender') == 'male':
    #         res['name'] = "Mr." + res['name']
    #         print("res['name']--", res['name'])
    #     elif vals.get('gender') == 'female':
    #         res['name'] = "Ms." + res['name']
    #         print("res['name']--", res['name'])
    #     else:
    #         return res
    #     print("Hello")
    #     print("self : - ", self,"res : -",res,"vals :-",vals)



    def browse_rec(self):
        """
        This si a button's method used to demonstrate browse() method
        """
        user_rec = self.browse(2)
        print("\nUSER REC--------------------------",user_rec)

        user_dict = user_rec.read(
            ['name', 'age', 'type_id', 'sub_type_ids'], load='_classic_read')
        print("USER DICCT----------------------", user_dict)

        record = self.env['subscription.user'].browse(3)
        creator_user = record.create_uid
        print(f"Record created by: {creator_user.name}")

        return {
            'effect': {
                'fadeout': 'slow',
                'type': 'rainbow_man',
                'message': 'Print BROWSE Sucessfully'
            }
        }


    # ORM Method
    def check_orm(self):
        search_var = self.env['subscription.user'].search([('gender','=','male')])
        print("Search Var ---------- ",search_var)
        for rec in search_var:
            print("Name ----" ,rec.name,"Gender --",rec.gender)

        search_count = self.env['subscription.user'].search_count([('gender', '=', 'female')])
        print("Search Var Count ---------- ", search_count)

        # browse = self.env['subscription.user'].browse(60)
        # print("Browse ID ---------- ", browse,"Name -",browse.name,"Age -",browse.age)
        stu_rec = self.browse(60)
        print("\nUSER REC--------------------------", stu_rec)
        stu_dict = stu_rec.read(
            ['name', 'age', 'type_id', 'sub_type_ids'], load='_classic_read')
        print("USER DICCT::::----------------", stu_dict)

        ref = self.env.ref('subscription_managaement.view_user_form')
        print("Reference:::---------- ", ref.type,"Name reference ---",ref.name)

        # browse_id=self.env['subscription.user'].browse(31)
        # browse_id.write({
        #     "name":"Kiran Chavda",
        #     "age":27
        # })
        # browse_id.copy()
        # browse_id.unlink(31)



        return {
            'effect': {
                'fadeout': 'slow',
                'type': 'rainbow_man',
                'message': 'Print Sucessfully'
            }
        }


    # name_get () deprecated in odoo 17 