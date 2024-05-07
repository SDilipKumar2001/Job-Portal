from datetime import datetime,timedelta
import requests
import ast
def create_crm_record(self):
        base_url = "https://mapi.indiamart.com/wservce/crm/crmListing/v2/"
        glusr_crm_key = "mRyzFbtl5HjATfeo53ON7liKq1LMlA=="
        end_time = datetime.now()
        start_time = end_time - timedelta(days=7)

        params = {
            "glusr_crm_key": glusr_crm_key,
            "start_time": start_time.strftime('%Y-%m-%d %H:%M:%S'),
            "end_time": end_time.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        response = requests.get(base_url, params=params)
        
        if response.status_code == 200:
            try:
                data = response.json()
                indiamart_integration = self.env['indiamart.intergration'].search([], limit=1)
                if indiamart_integration:
                    indiamart_integration.write({'reference': str(data.get('RESPONSE'))})
                
                indiamart_orm = self.env['indiamart.intergration'].search([], limit=1)
                if indiamart_orm.reference:
                    records_sample = ast.literal_eval(indiamart_orm.reference)
                    
                    for rec in records_sample:
                        state_search = self.env['res.country.state'].search([('name', 'ilike', rec['SENDER_STATE'])], limit=1)
                        query_time = datetime.strptime(rec['QUERY_TIME'], '%Y-%m-%d %H:%M:%S').date()
                        values = {
                            'crm_date': query_time,
                            'first_name': rec['SENDER_NAME'],
                            'phones': rec['SENDER_MOBILE'],
                            'emails': rec['SENDER_EMAIL'],
                            'name': rec['SUBJECT'],
                            'partner_name': rec['SENDER_COMPANY'],
                            'street': rec['SENDER_ADDRESS'],
                            'city': rec['SENDER_CITY'],
                            'state_id': state_search.id if state_search else False,
                            'zip': rec['SENDER_PINCODE'],
                            'description': rec['QUERY_MESSAGE'],
                            'indiamart_record': True,
                            'stage_id': 1,
                            "sale_person": 11,
                        }
                        if not self.env['crm.lead'].search([('name', '=', rec['SUBJECT']), '|', ('active', '=', False), ('active', '=', True)]):
                            self.env['crm.lead'].create(values)
            except Exception as e:
                # Handle exceptions or log errors
                pass
        else:
            # Handle API request errors
            pass