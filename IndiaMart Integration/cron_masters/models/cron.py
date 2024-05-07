from odoo import api,fields,models,http
from openerp.exceptions import ValidationError
import json
import requests
from datetime import datetime,timedelta

class cronInherit(models.Model):
    _name = "cron.crm.lead"
    _rec_name = 'key_id'
    
    key_id = fields.Char(string="Key")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    
    def crm_record_creation(self):
        base_url = "https://mapi.indiamart.com/wservce/crm/crmListing/v2/"
        orm_search = self.search([],limit=1)
        glusr_crm_key = orm_search.key_id
        end_time = datetime.now()
        new_end_time = end_time + timedelta(hours=5, minutes=30)
        formatted_end_time = new_end_time.strftime('%d-%b-%Y %H:%M:%S')
        start_time = end_time - timedelta(days=6)
        st = start_time.replace(hour=0, minute=0, second=0)
        formatted_start_time = st.strftime('%d-%b-%Y %H:%M:%S')
        # raise ValidationError(formatted_end_time)
        params = {
            "glusr_crm_key": glusr_crm_key,
            "start_time": formatted_start_time,
            "end_time": formatted_end_time
        }

        api_url = base_url + "?" + "&".join([f"{key}={value}" for key, value in params.items()])
        
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            json_data = json.dumps(data)
            response_data = data.get("RESPONSE")
            # raise ValidationError(str(response_data))

            for rec in response_data :
                state_search = self.env['res.country.state'].search([('name','ilike',rec['SENDER_STATE'])],limit=1)
                # raise ValidationError(rec['QUERY_TIME'])
                values={
                    'query_date' : rec['QUERY_TIME'],
                    'contact_name' : rec['SENDER_NAME'],
                    'mobile' : rec['SENDER_MOBILE'],
                    'email_from' :rec['SENDER_EMAIL'],
                    'name' : rec['SUBJECT'],
                    'partner_name' : rec['SENDER_COMPANY'],
                    'street' : rec['SENDER_ADDRESS'],
                    'city' : rec['SENDER_CITY'],
                    'state_id' : state_search.id,
                    'zip' : rec['SENDER_PINCODE'],
                    'message' : rec['QUERY_MESSAGE'],
                    'product_requested' : rec['QUERY_PRODUCT_NAME']
                }
                
                # if self.env['crm.lead'].search([('name','ilike',rec['SUBJECT'])]) :
                #     pass
                # else:
                crm_create = self.env['crm.lead'].create(values)
            # return json_data
        else:
            error_msg = f"Error {response.status_code}: Failed to fetch data from the API."
            return http.Response(status=500, content_type='application/json', body=error_msg)
        

                                                                        # OR
        
        
    # def create_crm_record(self):
    #     base_url = "https://mapi.indiamart.com/wservce/crm/crmListing/v2/"
    #     glusr_crm_key = "mRyzFb5v4nrETfei7nWY/F2GolvN"
    #     end_time = datetime.now().strftime("%d-%b-%Y")
    #     end_time_obj = datetime.strptime(end_time, "%d-%b-%Y")
    #     start_time_demo = end_time_obj - timedelta(days=6)
    #     start_time = start_time_demo.strftime("%d-%b-%Y")

    #     params = {
    #         "glusr_crm_key": glusr_crm_key,
    #         "start_time": start_time,
    #         "end_time": end_time
    #     }
        
    #     response = requests.get(base_url, params=params)
    #     if response.status_code == 200:
    #             data = response.json()
    #             indiamart_integration = self.env['indiamart.intergration'].search([], limit=1)
    #             if indiamart_integration:
    #                 indiamart_integration.write({'reference': str(data.get('RESPONSE'))})
    #             indiamart_orm = self.env['indiamart.intergration'].search([], limit=1)
    #             if indiamart_orm.reference:
    #                 records_sample = ast.literal_eval(indiamart_orm.reference)
                    
    #                 for rec in records_sample:
    #                     state_search = self.env['res.country.state'].search([('name', 'ilike', rec['SENDER_STATE'])], limit=1)
    #                     query_time = datetime.strptime(rec['QUERY_TIME'], '%Y-%m-%d %H:%M:%S').date()
    #                     values = {
    #                         'crm_date': query_time,
    #                         'first_name': rec['SENDER_NAME'],
    #                         'phones': rec['SENDER_MOBILE'],
    #                         'emails': rec['SENDER_EMAIL'],
    #                         'name': rec['SUBJECT'],
    #                         'partner_name': rec['SENDER_COMPANY'],
    #                         'street': rec['SENDER_ADDRESS'],
    #                         'city': rec['SENDER_CITY'],
    #                         'state_id': state_search.id if state_search else False,
    #                         'zip': rec['SENDER_PINCODE'],
    #                         'description': rec['QUERY_MESSAGE'],
    #                         'indiamart_record': True,
    #                         'stage_id': 1,
    #                         "sale_person": 11,
    #                     }
    #                     if not self.env['crm.lead'].search([('name', '=', rec['SUBJECT']), '|', ('active', '=', False), ('active', '=', True)]):
    #                         self.env['crm.lead'].create(values)
    #     else:
    #         raise ValidationError(response.status_code)