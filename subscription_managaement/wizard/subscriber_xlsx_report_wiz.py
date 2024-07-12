
from odoo import models, fields, api
import xlsxwriter
import base64
from datetime import datetime



class SubscriptionxlsxWizard(models.TransientModel):
    _name = 'subscriber.xlsx.report.wiz'
    _description = 'Subscriber XLSX Report'


    user_id = fields.Many2one('subscription.user','User')
    # date_time = datetime.datetime.strptime('2013-01-23', '%Y-%m-%d')

    def button_submit(self):
        attachment_obj = self.env['ir.attachment']
        workbook = xlsxwriter.Workbook('/tmp/subscriber.xlsx')
        bold_format = workbook.add_format({'bold': True, 'border': True, 'align': 'center', 'font_color': 'black', 'bg_color': '#fffbed'})
        title_format = workbook.add_format({'bold': True, 'border': True, 'align': 'center',  'bg_color': '#f2eee4'})
        header_format = workbook.add_format({'bold': True, 'border': True, 'align': 'center','font_size': 20,'font_color': 'light blue'})
        date_style = workbook.add_format({'num_format': 'dd-mm-yyyy'})

        for subscriber in self.user_id:
            # if subscriber.user_id:
            #     sheet.merge_range(f"A{row}:F{row}", subscriber.name, bold_format)
            # for sub in subscriber.user_id:
            sheet = workbook.add_worksheet('Subscriber XLSX Report')
            sheet.merge_range(0, 0, 0, 8,  'Subscriber XLSX Report', header_format)
            sheet.write(3,0,'Name', title_format)
            sheet.write(3,2,subscriber.name)
            sheet.write(4,0, 'Age', title_format)
            sheet.write(4,2, subscriber.age)
            sheet.write(5,0, 'Birthdate', title_format)
            sheet.write_datetime(5,2, subscriber.birthdate,date_style)
            sheet.write(3,5, 'Phone', title_format)
            sheet.write(3,7, subscriber.phone)
            sheet.write(4,5, 'Gender', title_format)
            sheet.write(4,7, subscriber.gender)
            sheet.write(5,5, 'Email', title_format)
            sheet.write(5,7, subscriber.email)
            sheet.write(8, 0, 'Subscription',title_format)
            sheet.write(8, 1, 'Recurrence ',title_format)
            sheet.write(8, 2, 'Start Date',title_format)
            sheet.write(8, 3, 'Expire Date',title_format)
            # sheet.write(8, 4, 'Price',title_format)


            row = 9
            for user in subscriber.sub_type_ids:
                sheet.write(row, 0, user.sub_type.name)
                sheet.write(row, 1, user.recurrence_id.name)
                sheet.write_datetime(row, 2, user.start_date, date_style)
                sheet.write_datetime(row, 3, user.expire_date, date_style)
                # sheet.write(row, 4, price.price)
            #     row += 1
            # sheet.write(row, 0, 'Total Price: $',bold_format)
            # sheet.write(row, 1, subscriber.total_subscription_price)

        print("jashcadsjkdvjks")



        workbook.close()
        f1 = open('/tmp/subscriber.xlsx', 'rb')
        # Read the data
        xlsx_data = f1.read()
        # encode it using base64
        buf = base64.b64encode(xlsx_data)
        # create a record of attachment
        doc = attachment_obj.create({'name': '%s.xlsx' % ('Subscriber Report'),
                                     'datas': buf,
                                     'res_model': 'subscriber.xlsx.report.wiz',
                                     'store_fname': '%s.xlsx' % ('Subscriber Report'), })
        # Return a URL Action of attachment record
        return {'type': 'ir.actions.act_url',
                'url': 'web/content/%s?download=true' % (doc.id),
                'target': 'current'
                }







