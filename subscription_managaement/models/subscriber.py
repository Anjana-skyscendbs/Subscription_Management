from odoo import models, fields,api


class Subscriber(models.Model):
    _name = 'subscription.user'
    _description = 'Users'
    _auto = True
    # _order = 'sequence'

    name = fields.Char(string='Name', required=True, index=True, translate=True)
    age = fields.Integer('Age', default=18, group_operator='avg')
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

    state = fields.Selection([('applied', 'Applied'),
                              ('draft', 'Draft'),
                              ('done', 'Done'),
                              ('left', 'Left')], 'State', default='applied')
    plan_id = fields.Many2one('subscription.plan', 'Plan' ,domain=[('name','=','Monthly')])
    type_ids = fields.One2many('subscription.addsubscription', 'user_id', 'Subscriptions')
    service_ids = fields.Many2many('subscription.service', string='Services')
    sequence = fields.Integer('Sequence')


    total_subscription_price = fields.Float(string='Total Price',
                                            compute='_compute_total_subscription_price', store=True)

    @api.depends('type_ids.price_depend')
    def _compute_total_subscription_price(self):
        for user in self:
            user.total_subscription_price = sum(subscription.price_depend for subscription in user.type_ids)

        """
                This method will calculate multiple fields.
                -------------------------------------------
                @param self : object pointer / recordset
                """
        print("SELF", self)
        # You can not access any fields from a recordset which contains multiple records
        # print("SELF NAME", self.name) # This will raise singleton error
        # filtered is used to filter the records
        # It can be called only with recrodset containing records
        # You can use either jsut the field name in filtered which will check value eexisting or not.
        # In below case it will return records which have active set.
        active_records = self.filtered('active')
        print("ACTIVE RECORDS", active_records)
        # The scond way is using lambda where you can use proper conditions to filter records.
        female_records = active_records.filtered(lambda r: r.gender == 'female')
        male_records = active_records.filtered(lambda r: r.gender == 'male')
        print("FEMALE RECORDS", female_records)
        print("MALE RECORDS", male_records)

        # Mapped is used to map field values from records and return in a list.
        active_records_name = active_records.mapped('name')
        print("ACTIVE NAMES", active_records_name)

        activ_name_age = active_records.mapped(lambda r: str(r.name) + "," + str(r.age))
        print("ACITVE NAME AGE", activ_name_age)

        # sorted() is used to sort the records
        sort_by_age = active_records.sorted(key='age')
        print("SORT BY AGE", sort_by_age)

        sort_by_name = active_records.sorted(key='name', reverse=True)
        print("SORT BY NAME", sort_by_name)

        # RECORDSET OPERATIONS
        # using in you can check whether a record exists in a recordset or not.
        # works with a single record and not multiple records
        res = female_records in active_records
        print("RES", res)
        for fr in female_records:
            print("FR IN ACT", fr in active_records)

        res = female_records not in active_records
        print("RES", res)

        # < is used to check subset
        print("SUBSET", female_records < active_records)
        # <= is used to check either subset or same set
        print("SUB OR SAME1", male_records <= active_records)
        print("SUB OR SAME 2", active_records <= active_records)

        # > is used to check superset
        print("SUPER", active_records > female_records)
        # >= is used to check superset or same set
        print("SUPER OR SAME 1", active_records >= male_records)
        print("SUPER OR SAME 2", active_records >= active_records)

        print("UNION", male_records | female_records)
        print("INTERSECTION", male_records & active_records)
        print("DIFF", active_records - female_records)

        for user in self:
            # You can access the fields using '.'.
            # Normal field will directly give the value of th
            #
            # e field
            print("NORMAL FIELD", user.name)
            # Relational fields will always give you a recordset.
            # M2O/Ref field will give you single record recordset
            # O2M/M2M will give you multiple records recordset.
            print("M2O FIELD", user.plan_id.name)
            # IF there's a single record you can access the field with multiple '.' referecnes.
            print("O2M FIELD", user.type_ids)
            # If there are multiple records you can not access the field directly.
            # print("EXAM FIELD",student.exam_ids.total_marks) # This will raise an error of singleton
            for subscription in user.type_ids:
                print("Subscription", subscription, subscription.price_depend)
                print("Subscription Name", subscription.type_id.name)
            print("M2M FIELD", user.service_ids)
            # print("REF FUELD", user.ref)
            # total = 0.0
            # total_obt = 0.0
            # You can use index in the recordset but if and only if there is a record
            if user.type_ids:
                print("O@M EXAM SUBSCRIPTION", user.type_ids[0].type_id.name)

            # ensure_one() is used to validate a single record
            user.ensure_one()  # NO ERROR
            # student.exam_ids.ensure_one() # ERROR

            # get_metadata() gives you the pre-defined fields / magic fields
            # It returns a dictionary containing id, create_date, create_uid, write_date, write_uid
            mt_dt = user.get_metadata()
            print("MT DT", mt_dt)



    def print_user(self):
        """
        This is a method of the button to demonstrate the usage of button
        -----------------------------------------------------------------
        @param self: object pointer / recordset
        """
        # TODO: Future development
        print("PRINT")
        print("SELFFFFFF", self)
        print("ENVIRONMENT", self.env)
        print("ENVIRONEMTN  ATTRS", dir(self.env))
        print("ARGS", self.env.args)
        print("CURSOR", self.env.cr)
        print("UID", self.env.uid)
        print("USER", self.env.user)
        print("CONTEXT",self.env.context)
        print("COMPANY",self.env.company)
        print("COMPANIES", self.env.companies)
        print("LANG", self.env.lang)

        subj_obj = self.env['subscription.type']
        print("SUBJ OBJ",subj_obj)
        std_obj = self.env['subscription.plan']
        print("STD OBJ", std_obj)


        form_view_user = self.env.ref('subscription.view_user_form')
        print("FORM VIEW USER", form_view_user)

    def create_rec(self):
        """
        This is a button method which is used to demonstrate create() method.
        ---------------------------------------------------------------------
        @param self: object pointer
        """
        vals1 = {
            'name':'janvi',
            'active':True,
            'age':22,
            'birthdate':'2001-04-01',
            # 'plan_id':2,
            'gender':'female'
        }
        vals2 = {
            'name': 'manoj',
            'active': True,
            'age': 29,
            'birthdate': '1994-05-17',
            # 'plan_id': 2,
            'gender': 'male '
        }
        vals_lst = [vals1,vals2]
        # Creating record in the same object
        new_users = self.create(vals_lst)
        print("USERS", new_users)

