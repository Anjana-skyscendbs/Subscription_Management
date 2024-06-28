from odoo import models, fields, api,_
from odoo.exceptions import ValidationError,UserError
import re


class SubscriptionUser(models.Model):
    # If you use only _inherit it will add / modify in to existing
    _inherit = 'subscription.user'

    height = fields.Float('Height(cm)')
    weight = fields.Float('Weight(kg)')
    blood_group = fields.Char('Blood Group')
    extra_notes = fields.Html('Extra Notes')

    # Redefine the existing field with a new attribute
    phone = fields.Char(string="Phone", track_visibility='always')

    def print_user(self):
        # this is overridden method of print user
        super().print_user()
        print("##################################### NEW METHOD")

    # @api.onchange('name', 'email', 'phone')
    # def _onchange_generate_user_code(self):
    #     # Call the inherited method
    #     # super()._onchange_generate_user_code()
    #     print("##################################### NEW METHOD onchange")
    #     # Additional logic using the new field (phone)
    #     if self.phone:
    #         # Append the last two digits of the phone number to the user code
    #         phone_suffix = ''.join(filter(str.isdigit, self.phone))[-2:]
    #         print("phone_suffix ", phone_suffix)
    #         self.user_code = (self.user_code or '') + phone_suffix
    #         print("user code",self.user_code)



    @api.constrains('email', 'user_code')
    def _check_email_and_user_code(self):
        for record in self:
            # Email validation
            if record.email:
                if not re.match(r"[^@]+@[^@]+\.[^@]+", record.email):
                    raise ValidationError(_("Invalid email format."))

                # Additional logic: Check if email domain matches user_code
                email_domain = record.email.split('@')[1]
                if record.user_code and not record.user_code.lower() in email_domain.lower():
                    raise ValidationError(_("User code must be part of the email domain."))

            # User code validation
            if record.user_code:
                if len(record.user_code) != 4 or not record.user_code.isalnum():
                    raise ValidationError(_("User Code must be 4 alphanumeric characters."))

    def check_orm(self):
        # Store the original method in a variable
        original_check_orm = super(SubscriptionUser, self).check_orm

        # Call the original method
        result = original_check_orm()

        # Additional functionality
        self._additional_orm_checks()

        # Combine the results
        if isinstance(result, dict) and 'effect' in result:
            result['effect']['message'] = 'Print and Additional Checks Successful'
        else:
            result = {
                'effect': {
                    'fadeout': 'slow',
                    'type': 'rainbow_man',
                    'message': 'Print and Additional Checks Successful'
                }
            }

        return result

    def _additional_orm_checks(self):
        # New functionality
        active_users = self.env['subscription.user'].search_count([('active', '=', True)])
        print("Active Users Count: ", active_users)

        recent_users = self.env['subscription.user'].search([('create_date', '>=', fields.Date.today())], limit=5)
        print("Recent Users:")
        for user in recent_users:
            print(f"Name: {user.name}, Created on: {user.create_date}")

        # Example of using read_group
        group_data = self.env['subscription.user'].read_group(
            [('age', '!=', False)],
            fields=['gender', 'age:avg'],
            groupby=['gender']
        )
        print("Average Age by Gender:")
        for data in group_data:
            print(f"Gender: {data['gender']}, Average Age: {data['age']}")

    state = fields.Selection([
        ('applied', 'Applied'),
        ('pending', 'Pending'),
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('left', 'Left'),
        ('renew', 'Renew')  # New state added
    ], 'State', compute='_compute_state', default='applied', store=True)

    def action_renew(self):
        for record in self:
            record.state = 'renew'

    def action_draft(self):
        for record in self:
            if record.state in ['applied', 'pending', 'done', 'left', 'renew']:
                record.state = 'draft'

    def action_apply(self):
        for record in self:
            if record.state in ['draft', 'renew']:
                record.state = 'applied'

    def action_done(self):
        for record in self:
            if record.state in ['applied', 'pending', 'renew']:
                record.state = 'done'

    def action_left(self):
        for record in self:
            if record.state in ['applied', 'pending', 'done', 'renew']:
                record.state = 'left'

    @api.depends('state')
    def _compute_state(self):
        for record in self:
            if record.state == 'renew':
                pass




