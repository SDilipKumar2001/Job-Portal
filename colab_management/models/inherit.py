from odoo import fields,models,api
from datetime import datetime
from odoo.exceptions import ValidationError
from datetime import datetime
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta 



AVAILABLE_PRIORITIES = [
    ('0', 'Poor'),
    ('1', 'Normal'),
    ('2', 'Good'),
    ('3', 'Very Good'),
    ('4','Excellent'),
    ('5','Wonderful')
]


class inheritance(models.Model):
    _inherit ="hr.job"

    experience = fields.Char(string="Experience Required")
    salary=fields.Char(string="Salary")
    location = fields.Char(string="Company Location")
    skills = fields.Text(string="Skills Required")
    country = fields.Many2one('res.country',string="Country")
    no_of_hired_employee = fields.Integer(string="Hired Employees")
    no_of_recruitment = fields.Integer(string="Number of Candidates Required")
    application_sended = fields.Integer(string="Application Sended")
    application_received = fields.Integer(string="Application Received")
    
    #fields for form settings in boolean
    description_bool= fields.Boolean(string = "Show Description")
    experience_bool = fields.Boolean(string="Show Experience")
    salary_bool=fields.Boolean(string=" Show Salary")
    location_bool = fields.Boolean(string=" Show Company Location")
    skills_bool = fields.Boolean(string=" Show Skills Required")
    country_bool = fields.Boolean(string="Show Country")
    no_of_hired_employee_bool = fields.Boolean(string=" show No Hired Employees")
    no_of_recruitment_bool = fields.Boolean(string=" Show Number of Candidates Required")
    application_sended_bool = fields.Boolean(string=" Show Application Sended")
    application_received_bool = fields.Boolean(string=" Show Application Received")

    expected_sal_bool = fields.Boolean(string=" Show Expected Salary")
    last_sal_bool = fields.Boolean(string=" Show Last Drawn Salary")
    h_qualification_bool =  fields.Boolean(string=" Show Highest Qualification")
    r_qualification_bool =  fields.Boolean(string=" Show Required Qualification")
    area_of_intrest_bool = fields.Boolean(string=" Show Area of Intrest Qualification")
    known_lang_bool = fields.Boolean(string=" Show known languages")
    resume_bool = fields.Boolean(string=" Show Resume")
    other_bool = fields.Boolean(string=" Show Other Application")


    

    gender_bool = fields.Boolean(string = "Show Gender", default=True )
    dob_bool = fields.Boolean(string = "Show DOB")
    whats_bool = fields.Boolean(string = "Show Whatsapp")
    address_bool = fields.Boolean(string = "Show Address")
    email_from_bool = fields.Boolean(string = "Show Email")
    partner_phone_bool = fields.Boolean(string = "Show Phone")
    partner_mobile_bool = fields.Boolean(string = "Show Mobile")
    go_abroad_bool = fields.Boolean(string = "Show Go Abroad")
    port_bool = fields.Boolean(string = "Show Passport Available")
    pass_number_bool = fields.Boolean(string = "Show Passport Number")
    


    # required_candidates = fields.Integer(string=" Total Number of Candidates ")
    # @api.depends('no_of_recruitment')
    # def total_exp(self):
    #     self.required_candidates = self.no_of_recruitment
    # @api.onchange('location')
    # def change(self):
    #     self.location = "canada"
    def button_for_graph(self):
        return {
           'name': (' graph view'), 
           'view_mode': 'graph', 
           'res_model': 'hr.job', 
           'type': 'ir.actions.act_window', 
           }
    def button_for_pivot(self):
        return {
           'name': (' pivot view'), 
           'view_mode': 'pivot', 
           'res_model': 'hr.job', 
           'type': 'ir.actions.act_window', 
           }

   



class inherit(models.Model):

    _inherit="hr.applicant"
# THIS IS MANY2MANY FIELD BUT WE HERE USED 2 SAME MANY2MANY FIELD(ir.attachment) IN THE SAME MODEL 
# SO WE CREATE THE MANY2MANY LIKE THIS.

    res= fields.Many2many(comodel_name="ir.attachment", 
                                relation="m2m_resume", 
                                column1="m2m_id",
                                column2="attachment_id",
                                string="Resume")

    other =fields.Many2many(comodel_name="ir.attachment", relation="m2m_other", 
                                column1="m2m_id", column2="attachment_id",string="Other Certification")
    
    # CHAR FIELD
    name=fields.Char(string="Candidate Name",required=True)
    whats=fields.Char(string="Whatsapp Number")
    location=fields.Char(string="Location Preference")
    area_of_interest = fields.Char(string="Area of Interest")
    pass_number=fields.Char(string="Passport Number")
    cal_exp=fields.Char(string="Net Experience",compute="find")
    
    # CREATING THE REFERENCE NUMBER 
    reference_no = fields.Char(string='Applicant reference',readonly=True)
    
    # MANY2ONE FIELD
    client=fields.Many2one('company.details',string="Client Id",required=True)
    h_qualification=fields.Many2one('hr.recruitment.degree',string="Highest Qualification")

    # MANY2MANY FIELD
    known_languages = fields.Many2many('res.lang',string="Languages Known")
    
    # SELECTION FIELD
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender',required=True)
    go_abroad=fields.Selection([('yes','Yes'),('no','No')],string="Willing to go Abroad")
    port=fields.Selection([('yes','Yes'),('no','No')],string="Passport Available")
    exp=fields.Selection(string="Experience",selection=[('experience', 'Experience'), ('fresher', 'Fresher')])
    
    # SELECTION FIELD WITH WIDGET IS GIVEN AS STAR
    message = fields.Selection(AVAILABLE_PRIORITIES, "Candidate Rating", default='0') 
    
    # DATE FIELE
    dob=fields.Date(string="DOB")
    
    # TEXT FIELD
    address=fields.Text(string="Address")
    r_qualification=fields.Text(string="Related Qualification")

    # MONETARY FIELD
    company_id = fields.Many2one('res.company',string="Company",default=lambda self:self.env.company)
    currency_id = fields.Many2one('res.currency',related='company_id.currency_id')
    expected=fields.Monetary(string="Expected Salary")
    last=fields.Monetary(string="Last Drawn Salary")

    
    # INTEGER FIELD
    net=fields.Integer(string="Total Net Experience")
    

    # ONE2MANY FIELD
    information=fields.One2many('hr.applicant.lines','detail',string="Experience Details")
    # YOU CAN USE THE mode=kanban IN THE ONE2MANY FIELD TO GET THE DATA IN THE VIEW OF KANapiBAN
    
    # CREATING THE REFERENCE NUMBER
    @api.model
    def create(self, val):
      if val.get('reference_no', ('New')) == ('New'):
         val['reference_no'] = self.env['ir.sequence'].next_by_code('hr.applicant') or ('New')
         res = super(inherit, self).create(val)
         return res 

    # WHEN THE COMPANY NAME(i.e client field) HAS BEEN SELECTED ONLY ITS COMPANY'S JOB POSITION ONLY DISPLAYED 
    # IN THE MANY2ONE FIELD(i.e job_id field)

    @api.onchange('client')
    def time_slot_master(self):
        val=[]
        for i in self:
            data_2= self.env['hr.job'].search([('client','=',i.client.id)])
            for m in data_2:
                val.append(m.id)
            return {'domain':{'job_id':[('id','=',val)]}}

    # CALCULATE THE SUM OF ALL INTEGER VALUES IN THE ONE2MANY FIELD(calculation) FIELD 
    # AND SAVE IT IN THE (net) FIELD

    @api.onchange('information')
    def total_exp(self):
        val=[]
        for k in self:
            for n in k.information:
                val.append(n.calculation)
            k.net = sum(val) 

    # CONVERT THE TOTAL NO OF DAYS IN THE (net) FIELD INTO {year,weeks,days} FORMAT AND SAVE IT IN THE (cal_exp) FIELD
    @api.depends('net')
    def find(self):
        for i in self:
            number_of_days = i.net
            DAYS_IN_WEEK = 7
            year = int(number_of_days / 365)
            weeks = int((number_of_days % 365) / DAYS_IN_WEEK)
            days = ((number_of_days % 365) % DAYS_IN_WEEK)
            self.cal_exp = str(year)+ "y" +" "+str(weeks) + "w" +" "+ str(days) + "d"  


# ONE2MANY MODEL
class candidate_exp(models.Model):
    _name='hr.applicant.lines'
    _description='Appointment Lines'

    detail=fields.Many2one('hr.applicant',string="Candidate")

    comp_name=fields.Char(string="Company Name")
    role=fields.Char(string="Recent Role in The Company")
    change=fields.Char(string="Reason For Change")  
    from_field=fields.Date(string="From")
    to_field=fields.Date(string="To")
    years=fields.Char(string="Experience")
    calculation=fields.Integer(string="Datetime")

# CALCULATING YEAR,MONTH,DAY DIFFERENCE BETWEEN TWO DATES.
    @api.onchange('from_field','to_field','years')
    def onchange_age(self):
           if self.from_field and self.to_field:
                d1 = datetime.strptime(str(self.from_field),'%Y-%m-%d')
                d2 = datetime.strptime(str(self.to_field),'%Y-%m-%d')
                delta = relativedelta(d2, d1)
                self.years= str(delta.years )+ "y" +" "+str( delta.months) + "m" +" "+ str(delta.days) + "d"

    @api.onchange('from_field', 'to_field','years')
    def calculate_date(self):
        if self.from_field and self.to_field:
            d1=datetime.strptime(str(self.from_field),'%Y-%m-%d') 
            d2=datetime.strptime(str(self.to_field),'%Y-%m-%d')
            d3=d2-d1
            self.calculation=str(d3.days)

    # @api.depends('from_field','to_field')
    # def onchange_ages(self):
    #     for i in self :
    #         # if self.from_field and self.to_field:
    #         d1 = datetime.strptime(i.from_field)
    #         d2 = datetime.strptime(i.to_field)
    #         delta = relativedelta(d2, d1)
    #         self.calculation=delta
            # self.calculation = str(delta.years )+ "y" +" "+str( delta.months) + "m" +" "+ str(delta.days) + "d"
    
    # @api.onchange('years')
    # def onchange_age(self):
    #         if self.years:
    #             d1 = datetime.strptime(self.years)
                # d2 = datetime.strptime(str(self.to_field),'%Y-%m-%d')
                # delta = relativedelta(d2, d1)
                # self.years = str(delta.years )+ "y" +" "+str( delta.months) + "m" +" "+ str(delta.days) + "d"
   
    # @api.onchange('information')
    # def total_job_application(self):
    #     for v in self:
    #         no_of_recruitment = self.env['hr.applicant.lines'].search([('years')])
    #         count = 0
    #         for i in no_of_recruitment:
    #             count += i.no_of_recruitment
    #         v.net = count 

# CREATING THE NEW FIELD IN THE EXISTING MODEL USING THE inherit
class job_position(models.Model):
    _inherit="hr.job"
    client=fields.Many2one('company.details',string="Client Id",required=True)
    target=fields.Date(string="Target Date")

class portal_name_unique(models.Model):
    _inherit="res.users"
    _sql_constraints = [('name_uniq', 'UNIQUE (name)',  'You can not have two users with the same name !')]



#CREATING THE POPUP BOX WHEN THE STAGE OF THE RECORD IS CHANGED    
    # @api.onchange('stage_id')
    # def onchange_template_id(self):
    #     return {'value':{},'warning':{'title':'warning','message':'The Stage of the Record is Changed'}}

#AUTOMATIC CALCULATION OF THE DATE FIELD USIND ADDITION (FIELD NAME=net).
#   1} @api.onchange('information')
    # def total_exp(self):
    #     val=[]
    #     for k in self:
    #         for n in k.information:
    #             val.append(n.years)
    #             k.net = sum(val) 
    

#   2} @api.onchange('information')
    # def total_exp(self):
    #     val=[]
    #     for k in self:
    #         for n in k.information:
    #             val.append(n.years)
    #             # k.net = sum(val)
    #             a=sum(val)
    #     k.net = a/365 +'months'

 #  3}@api.depends('information')
    # def _amount_all(self):
    #     for order in self:
    #         net = 0.0
    #         for line in order.information:
    #             net += line.years
    #         order.update({
    #             'net': net,
    #         }) 

# CALCULATING THE DATE DIFFERENCE BETWEEN TWO DATES.
    # @api.onchange('from_field', 'to_field','years')
    # def calculate_date(self):
    #     if self.from_field and self.to_field:
    #         d1=datetime.strptime(str(self.from_field),'%Y-%m-%d') 
    #         d2=datetime.strptime(str(self.to_field),'%Y-%m-%d')
    #         d3=d2-d1
    #         self.years=str(d3.days)

# CALCULATING MONTH DIFFERENCE BETWEEN TWO DATES.
    # @api.onchange('from_field','to_field','years')
    # def onchange_age(self):
    #         if self.from_field and self.to_field:
    #            d1=datetime.strptime(str(self.from_field),'%Y-%m-%d') 
    #            d2=datetime.strptime(str(self.to_field),'%Y-%m-%d')
    #            self.years = (d2.year - d1.year) * 12 + (d2.month - d1.month)

# CONVERTING THE NUMBER OF (days) INTO (years,months,days) FORMAT
#     @api.depends('net')
#     def find(self):
#         for i in self:
#             number_of_days = i.net
#             years = number_of_days // 365
#             months = (number_of_days - years *365) // 30
#             days = (number_of_days - years * 365 - months*30)
#             self.cal_exp = str(years)+ "y" +" "+str(months) + "m" +" "+ str(days) + "d" 