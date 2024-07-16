from odoo import models, fields, api, _ , Command
from odoo.exceptions import ValidationError,UserError
import re

from datetime import date


class Subscriber(models.Model):
    _name = 'subscription.user'
    _description = 'Create User'
    _auto = True
    _inherit=['mail.thread','mail.activity.mixin']
    # todo 19.Add an SQL constraint to add a unique constraint on a single field.
    #  20. Add an SQL constraint to add a unique constraint on a combination of two fields.
    #  21. Add an SQL constraint to add a check constraint to check the value of a field.
    #  26. Add an SQL constraint to check a field’s value is not greater than a specific number.
    _sql_constraints = [
        # ('check_age', 'check(age>=18)', 'Age Must be 18 Above '),
        ('unique_phone', 'unique (phone,email)','The phone number and email should be different')
        # ('unique_phone', 'unique (phone)','The phone number should be different')
    ]

    _order = 'sequence'


# todo exercise 3 9. Add a character field and an integer field. When there is a value in the character field the integer field should be mandatory else readonly.

    name = fields.Char(string='Name', required=True, index=True, translate=True, track_visibility="always")#
    age = fields.Integer('Age',group_operator='avg',attrs="{'required': [('name', '!=', False)]}")

    # todo 10.Add a boolean field and a text field. Put the text field in a separate page. Now
    #  when the boolean field is checked then the page should be visible else it should be invisible.

    active = fields.Boolean('Active', help='This field is used to activate or deactivate a record', default=True)
    notes = fields.Text('Notes',attrs="{'invisible': [('active', '=', False)]}")
    birthdate = fields.Date('Birthdate')
    # start_timestamp = fields.Datetime('Start Date')

    gender = fields.Selection(selection=[('male', 'Male'),
                                         ('female', 'Female')], string='Gender')
    user_code = fields.Char('User Code', size=4)
    password = fields.Char('Password')
    email = fields.Char('Email')
    phone = fields.Char('Phone')
    photo = fields.Image('Photo')
    template = fields.Html('Template')
    recurrence_id = fields.Many2many('subscription.recurrence', string='Recurrence Period')
    ref = fields.Reference([('subscription.user', ' Subscribers'),
                            ('res.users', 'Users'),
                            ('res.partner', 'Contacts')], 'Reference')
    document = fields.Binary('Document')
    file_name = fields.Char('File Name')
    color = fields.Integer('Color')
    partner =fields.Many2one('res.users', 'Partners')

    state = fields.Selection([('applied', 'Applied'),
                              ('pending', 'Pending'),
                              ('draft', 'Draft'),
                              ('done', 'Done'),
                              ('left', 'Left')], 'State',compute='_compute_state', default='applied')

    type_id = fields.Many2one('subscription.type', 'Subscription',store = True)#,domain=[('name','=','Streaming Service')]
    sub_type_ids = fields.One2many('subscription.addsubscription', 'user_id', 'Subscriptions',ondelete='cascade',)

    @api.depends('sub_type_ids.expire_date')
    def _compute_state(self):
        today = date.today()
        for record in self:
            if any(child.expire_date and child.expire_date <= today for child in record.sub_type_ids):
                record.state = 'left'
            elif any(child.expire_date for child in record.sub_type_ids):
                record.state = 'done'
            else:
                record.state = 'draft'

    sequence = fields.Integer('Sequence')
    # reg_no = fields.Char('Reg No', copy=False,readonly=True,default=lambda self: self._get_sequence(),required =True,index=True)#default=lambda self: self._get_sequence(),
    reg_no = fields.Char('Reg No', copy=False)#default=lambda self: self._get_sequence(),

    parent_id = fields.Many2one('subscription.user', 'Manager')
    child_ids = fields.One2many('subscription.user', 'parent_id', 'Subordinates')
    parent_path = fields.Char('Parent Path', index=True)
    priority = fields.Selection([(str(ele), str(ele)) for ele in range(6)], 'Priority')

    user_id = fields.Many2one('res.users','User')



    total_subscription_price = fields.Float(string='Total Price',
                                            compute='_compute_total_subscription_price', store=True,group_operator='avg')

    payment_mode = fields.Selection([('cash', 'Cash'),
                              ('digital', 'Digital Payments'),
                              ('debit', 'Debit Card'),
                              ('credit', 'Credit Card')], 'Payment Mode', default='cash')



    @api.model
    def _default_type_id(self):
        # Get the default subscription type based on some condition
        default_type = self.env['subscription.type'].search([('is_default', '=', True)], limit=1)
        return default_type.id if default_type else False
    #
    # @api.model
    # def default_get(self, fields_list):
    #     res = super(Subscriber, self).default_get(fields_list)
    #     if 'type_id' in fields_list:
    #         res['type_id'] = self._default_type_id()
    #     return res



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
        #  13.Print the current language of the system.
        #   14.Print the name of the current company.
        #   15.Print the name of the Current User
        #   16.Get the context from Environment
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
# todo exercise 3 17.Get the recordset of the form view which you have created for your model.
        records = self.env['subscription.user'].search([])
        print("Print Records ID",records)
# todo exercise 3 18.Get the value of all predefined fields for a recordset containing one or more records without using the ORM methods.
        for user in self:
            mt_dt = user.get_metadata()
            print("MT DT Predefined Fields", mt_dt)

# todo exercise 3 19. Filter the existing recordset with a condition. The condition should contain a field and a value.

        # Filter the recordset based on a condition
        filtered_records = records.filtered(lambda r: r.age > 25)
        print("filtered_records ID", filtered_records)

        # # Filter the recordset based on a condition using domain syntax
        # domain_filtered_records = records.filtered(domain=[('age', '>', 25)])
        # print("domain_filtered_records ID", domain_filtered_records)
# todo exercise 3 20. Filter an existing record on a field such that if only the records which do have a value in the field should be displayed.
        # Filter the recordset to display only records with a value in the 'active' field
        with_value_records = records.filtered(lambda r: bool(r.active))
        print("with_value_records ID", with_value_records)
# todo exercise 3 21. From a recordset get two fields character and integer such that the result would
#  contain a single value which will be a concatenation of two fields mentioned
#  above. For e.g. If you’re taking name and age it should be ‘Amar-25’.
        # Get the concatenated value of 'name' and 'age' fields
        result = [f"{r.name}-{r.age}" for r in records]
        print("result name-age", result)
# todo exercise 3 22. From a recordset get a list of values in a specific field.
        # Get a list of values in the 'name' field
        field_values = records.mapped('name')
        print("result field_values list ", field_values)

# todo exercise 3 23. Sort a recordset in a descending order with a field other than name. The action
#  should be performed on a recordset only.

        # Sort the recordset in descending order by the 'name' field
        sort_by_name = records.sorted(key='name', reverse=True)
        print("SORT BY NAME",sort_by_name)

        female_records = records.filtered(lambda r: r.gender == 'female')
        male_records = records.filtered(lambda r:r.gender=='male')
        print("FEMALE RECORDS", female_records)
        print("MALE RECORDS", male_records)
# todo exercise3 25. Get the union, intersection and difference of two recordsets.
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

    def open_one2many(self):
        self.ensure_one()
        return {
            'name': 'One2Many Records',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'subscription.addsubscription',
            'domain': [('user_id', '=', self.id)],
            'context': {},
        }

    def action_confirm(self):
        self.state = 'draft'

    # @api.onchange('active')
    # def _onchange_active(self):
    #     if not self.active:
    #         self.notes = "This record is currently inactive."
    #     else:
    #         self.notes = "


    @api.onchange('name', 'email')
    def _onchange_generate_user_code(self):
        if self.name and self.email:
            self.user_code = (self.name[:2] + self.email[:2]).upper()


    # @api.onchange('birthdate')
    # def _onchange_birthdate(self):
    #     if self.birthdate:
    #         today = date.today()
    #         self.age = today.year - self.birthdate.year - (
    #                     (today.month, today.day) < (self.birthdate.month, self.birthdate.day))

    @api.constrains('email')
    def _check_email(self):
        for record in self:
            if record.email and not re.match(r"[^@]+@[^@]+\.[^@]+", record.email):
                raise ValidationError(_("Invalid email format."))

    # todo exercise 3 26. Add a button on the form view when you click on this button it will create a
#  record on a new model which does not have a relation with the current model.

    def create_rec(self):
        """
        This is a button method which is used to demonstrate create() method.
        ---------------------------------------------------------------------
        @param self: object pointer
        """
        vals1 = {
            'name': 'lalit',
            'active': True,
            'age': 22,
            'birthdate': '2001-04-01',
            'type_id': 2,
            'gender': 'male',
            # 0 is used for creation
            # (0,0,{}) used to create record in O2M field
            'sub_type_ids': [
                (0, 0, {
                    'sub_type': 2,
                    'recurrence_id': 3,
                    'price': 200
                }),
                # Instead of 0,0 you can use the Command.create method.
                # (Command.create(<vals_dict>))
                (
                    Command.create({
                    'sub_type': 1,
                    'recurrence_id': 2,
                    'price': 400
                })),
                (0, 0, {
                    'sub_type': 2,
                    'recurrence_id': 1,
                    'price': 300
                })
            ],

        }
        vals2 = {
            'name': 'Anjum',
            'active': True,
            'age': 29,
            'birthdate': '1994-05-17',
            'type_id': 2,
            'gender': 'female',

        }
        vals_lst = [vals1, vals2]
        # Creating record in the same object
        new_stds = self.create(vals_lst)
        print("STDS", new_stds)

        return {
            'effect':{
                'fadeout':'slow',
                'type':'rainbow_man',
                'message':'Record has been Created Sucessfully'
            }
        }

# todo exercise 3 28. Add a button on the form view. When you click this button it should update a
#  field’s value of the current record.

    def update_rec(self):
        vals = {
            'age':30,
            'type_id':1,
            'name':'Dolly',
            'gender': 'female',
            'type_id': 4,
            'sub_type_ids': [
            # (0,0,{'sub_type':3,'price':200}),
            #  (Command.create({'sub_type':3,'price':200,'recurrence_id':})),
            # (1,2,{'sub_type':2})
            #  (Command.update(2,{'sub_type':1})),
            #  (2,18),
            #  (Command.delete(3)),
            #  (3,19)
            #  (Command.unlink(2))
            #  (4,19)
            #  (Command.link(2)),
            #  (5,0,0)
            #  (Command.clear()),
            #  (6,0,[1,2,3])
            #  (6,0,[1,3])
            (Command.set([20, 21, 23, 24]))
            #  (4,1),(4,2),(4,3)
        ]

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

# todo exercise 3 34.Fetch 15 records from a model skipping first 5 records based on a condition and it should be sorted by name.
    def search_rec(self):
        all_users = self.search([])
        # When you pass a blank domain it will return all the records.
        print("ALL USERS",all_users)
        # When you pass offset it will skip no of records from the result todo 38. Get all the records with specific fields without passing the domain. Sort the
        # records by name.
        offset_5_users = self.search([], offset=5 ,limit=3 ,order='name asc')
        print("SKIP 5 RECORDS and LIMIT 3 record show", offset_5_users)
        # records = self.env['subscription.user'].search([], order='name asc')
        # # print("USERS", records)


        ### search_count todo exercise 3 35. Fetch the no of records based on a condition with and without using search method.
        no_of_users = self.search_count([])
        print("TOTAL USERS", no_of_users)
        # todo exercise 3 36. Get the no of records based on a condition.37. Get a list of dictionary for records which will be of records which you will get
        #   based on some condition. NOTE: This needs to be done without using search or
        # read method.
        no_of_female_users = self.search_count([('gender', '=', 'female')])
        print("FEMALE USERS", no_of_female_users)

        return {
            'effect': {
                'fadeout': 'slow',
                'type': 'rainbow_man',
                'message': 'Record has been Search Sucessfully'
            }
        }
    def copy_rec(self):
        default = {
            'name': self.name + ' (copy)',
            'email': False,
            'state': 'applied',
        }
        new_rec = self.copy(default=default)
        print("\nNEW REC",new_rec)


    # todo exercise 4 8. Override unlink() method to avoid deletion if it’s not in the first state of the state field.
    # @api.model
    # def unlink(self, vals):
    #     res = super(Subscriber, self).unlink()
    #     for vals in self:
    #         if vals.active == 'active':
    #             raise UserError(_("Record cannot be deleted, it is an active state"))
    #         else:
    #             return res
    #     return res


    @api.constrains('age')
    def val_age(self):
        for record in self:
            if record.age <=18:
                raise ValidationError(_('The age must be above than 18 years'))


# todo Excersice :4 Question :1 Override create method to create a record in another model.

    # @api.model
    # def create(self, vals):
    #     # Create the record in current model
    #     record = super(Subscriber, self).create(vals)
    #
    #     # Create a related record in other model
    #     other_model_vals = {
    #         'name': 'Subscription Main',
    #         'code': 'SM'
    #     }
    #     other_record = self.env['subscription.type'].create(other_model_vals)
    #
    #     # Optionally, you can link the related record to the original record
    #     record.type_id = other_record.id
    #
    #     return record

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


    # todo Exercise 2. Override create method to add additional field values before creating the record.
    @api.model
    # def create(self, vals):
    #     res = super(Subscriber, self).create(vals)
    #     if vals.get('gender') == 'male':
    #         res['name'] = "Mr." + res['name']
    #         print("res['name']--", res['name'])
    #     elif vals.get('gender') == 'female':
    #         res['name'] = "Ms." + res['name']
    #         print("res['name']--", res['name'])
    #     else:
    #         return res
        # if not vals.get('sub_type_ids'):
        #     raise ValidationError(_("PLease fill the one2many field"))
        # else:
        #     return res
    #     return res
        # print("Hello")
        # print("self : - ", self,"res : -",res,"vals :-",vals)

    # todo exercise 4. Override write() method to update the records.
    # def write(self, vals):
    #     if vals.get('name'):
    #         vals['user_code'] = vals['name'][:4].upper()
    #     return super().write(vals)

    # def unlink(self):
    #     if self.state == 'applied':
    #         raise ValidationError(("Do not Deleted"))
    #     return super(Subscriber, self).unlink()


    # todo exercise 4 15.Add an onchange method for a field where it will update values of two other  fields.

    @api.onchange('gender','age')
    def onchange_gender(self):
        """
        Onchange method to set default age for male and female
        ------------------------------------------------------
        """
        for user in self:
            ages = 0
            print("ages ",ages)
            if user.gender == 'female':
                ages = 18
                print("Age",ages)
            elif user.gender == 'male':
                ages = 21
                print("Age", ages)
            user.age = ages

    # todo exercise 4 16.Add an onchange method for multiple fields to update another field’s value.
    #  NOTE: Here the same method should be called when you change any of the fields.

    # @api.onchange('name', 'gender', 'active')
    # def _onchange_fields(self):
    #     if self.name and self.gender and self.active:
    #         self.total_subscription_price = 100.0
    #     else:
    #         self.total_subscription_price = 0.0


    # todo exercise 4 18. If there is no value passed raise a warning in an onchnage method.
    # @api.onchange('phone')
    # def _onchange_phone(self):
    #     if not self.phone:
    #         warning = {
    #             'title': 'Warning!',
    #             'message': 'Please enter a value for Phone Number',
    #         }
    #         return {'warning': warning}


    # todo exercise 4 23. Create a Sequence for an object and fetch the sequence as default value to a field.

    @api.model
    # def _get_sequence(self):
    #     sequence_obj = self.env['ir.sequence']
    #     sequence = sequence_obj.next_by_code('subscription.user.sequence')
    #     print("sequnce===================================================================",sequence)
    #     return sequence


    # todo exercise 4 24. Create a sequence and assign it on creation of the record.

    # @api.model
    # def create(self, vals):
    #     if vals.get('reg_no', '/') == '/':
    #         sequence_obj = self.env['ir.sequence']
    #         vals['reg_no'] = sequence_obj.next_by_code('subscription.user.sequence')
    #     return super(Subscriber, self).create(vals)

    # todo exercise 4 25. Create a sequence and assign it’s value on a button click.

    def assign_sequence(self):
        sequence_obj = self.env['ir.sequence']
        self.reg_no = sequence_obj.next_by_code('subscription.user.sequence')




    # @api.model
    # def search(self, args, offset=0, limit=None, order=None, count=False):
    #     args = ['|', ('active', '=', False), ('active', '=', True)] + args
    #     return super().search(args, offset=offset, limit=limit, order=order, count=count)


    # def unlink(self):
    #     if self.sub_type_ids:
    #        raise ValidationError("You can not delete with subscription !")
    #     return super().unlink()


    # todo 6. Override copy() method to remove one of the existing fields and add another value.
    # def copy(self, default=None):
    #     default = dict(default or {})
    #
    #     # Remove an existing field from the default values
    #     if 'phone' in default:
    #         del default['phone']
    #
    #     # Add a new value to the default values
    #     default['name'] = 'Copy'
    #
    #     copied_partner = super(Subscriber, self).copy(default)
    #     return copied_partner


    # todo exercise 4 7. Override copy() method and have the state field not copied and bring back to the
    #  fiirst state in the selection.
    # def copy(self, default=None):
    #     default = dict(default or {})
    #
    #     # Reset the state field to the first state in the selection
    #     default['state'] = 'draft'
    #
    #     copied_partner = super(Subscriber, self).copy(default)
    #     return copied_partner


    @api.model
    # def create(self,values):
    #     print("Values of create Method",values)
    #     print("Self ",self)
    #     rtn =super(Subscriber,self).create(values)
    #     print("Return Statement ",rtn)
    #     return rtn
    #
    # def create(self,values):
    #     print("Before edit values ",values)
    #     values["active"] = True
    #     print("After edit values",values)
    #     rtn = super(Subscriber, self).create(values)
    #     return rtn


    # todo excercise 4 12.Override default_get method to add default fields when the record is created.

    def default_get(self,fields_list=[]):
        print("fields list",fields_list)
        rtn =super(Subscriber,self).default_get(fields_list)
        print("Before Edit ",rtn)
        rtn['active'] = True
        rtn['name'] = 'aenna g'
        rtn['email'] ='dafdaanajana75@gmail.com'
        print("return statement " ,rtn)
        return rtn





    def browse_rec(self):
        """
        This si a button's method used to demonstrate browse() method
        """
        user_rec = self.browse(2)
        print("\nUSER REC--------------------------",user_rec)

        user_dict = user_rec.read(
            ['name', 'age', 'type_id', 'sub_type_ids'], load='_classic_read')
        print("USER DICCT----------------------", user_dict)
# todo exercise 3 40. Get a recordset of the user who created the record.
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