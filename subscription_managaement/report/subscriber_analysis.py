from odoo import models, fields, api


class subscriber_analysis(models.Model):

    _name = 'subscriber.analysis'
    _auto = False

    # The fields have to be defined same as used in query except id.
    name = fields.Char('Subscriber Name', translate=True)
    age = fields.Integer('Age')

    type_id = fields.Many2one('subscription.type', 'Subscription',store = True)
    start_date = fields.Date(string='Start Date', default=fields.Date.today())
    expire_date = fields.Date(string='Expire Date')#, compute='_compute_expire_date'
    currency_id = fields.Many2one('res.currency', 'Currency')
    price = fields.Monetary(currency_field='currency_id', string='Price')

    service = fields.Many2one('subscription.service', 'Subscription Type')
    # print(service.type_id,"============================")

    plan_id = fields.Many2one('subscription.plan', 'Plan')
    user_id = fields.Many2one('subscription.user', 'User', ondelete='cascade')

    @api.model
    def init(self):
        self.env.cr.execute("""create or replace view subscriber_analysis as (
            SELECT su.id,
                   su.name,
                   su.age,
                   su.type_id,
                   sa.plan_id,
                   sa.service,
                   sa.start_date,
                   sa.expire_date,
                   sa.currency_id,
                   sa.price
             FROM subscription_user su,subscription_addsubscription sa
             WHERE su.id = sa.user_id) 
        """)

        # self.env.cr.execute("""create or replace view student_analysis as (
        #             SELECT ex.id,
        #                    st.name,
        #                    st.age,
        #                    st.standard_id,
        #                    ex.subject_id,
        #                    ex.total_marks,
        #                    ex.min_marks,
        #                    ex.obt_marks,
        #                    ex.perc
        #             FROM school_student st, school_exam ex
        #             WHERE st.id = ex.student_id)
        #         """)