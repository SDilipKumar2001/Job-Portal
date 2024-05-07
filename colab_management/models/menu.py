from odoo import api,models,fields
from odoo.exceptions import ValidationError

class company(models.Model):
# CREATING THE NEW MODEL
    _name = "company.details"
    _rec_name = "name"
    _inherit = ['mail.thread'] 
    _register= True
    _description = "Company Name"
    SELECTION = [
            ('char','Char'),
            ('text','Text'),
            ('boolean','Boolean'),
            ('binary','Binary'),
            ('float','Float'),
            ('integer','Integer'),
            ('date','Date'),
            ('datetime','Datetime'),
            ('html','Html'),
            ('selection','Selection'),
            ('many2one','Many2one'),
            ('many2many','Many2many'),
        ]
# CHAR FIELD
    name = fields.Char(string="Company Name",required=True)
    address = fields.Char(string = "Address")
    mob_nos = fields.Char(string ="Phone No")
    email = fields.Char(string="Email",required=True)
    # recruiter = fields.Many2one('res.users',string = "User Name",default=lambda self: self.env.user)
    
    # partner_name = fields.Many2one('res.partner', readonly = True, string="Customer",compute='orm_self')
    # @api.depends('name')
    # def orm_self(self):
    #     orm = self.env['res.partner'].search([('name','=',self.name)])
    #     self.partner_name = orm   
    partner_name = fields.Many2one('res.partner', readonly = True, string="Customer")
    
    company_type = fields.Many2one('company.type',string="Company Type")
    ein_number = fields.Char(string="EIN Number")
    vendor = fields.Boolean(string='Vendor')
    pass_through = fields.Boolean(string='Pass Through')
    imp_partner = fields.Boolean(string='Implementation Partner')
    end_client_pass = fields.Boolean(string='End Client')
    referral = fields.Boolean(string='Referral')
    document_upload = fields.One2many('document.upload','document_id',string='Documents',ondelete='cascade')
    accountant_information = fields.One2many('accountant.details','accountant_id',string='Accountant Details',ondelete='cascade')
    
    
    # type_selection = fields.Selection([('direct','Direct'),('sub_contract','')])

#SMART BUTTON CREATION
    no_of_recruitment  = fields.Integer(" Total Job vacancy",compute = "total_job_application")#new button
    total_job_position = fields.Integer("Total Job Position",compute = "appplication_data")
    tot_job_application =  fields.Integer("Total Job Application" ,compute ="hr_recruitment" )
    selected_count =  fields.Integer("Selected Count " ,compute ="selected_count_total" )


# VENDOR DETAILS
    vendor_id = fields.Char(string="ID")
    vendor_name = fields.Many2one('res.partner',string='Name')
    duns_number = fields.Char(string="DUNS Number")
    vendor_address = fields.Text(string='Address')
    vendor_website = fields.Char(string="Website")
    vendor_contact_email = fields.Char(string="Email")
    vendor_contact_phone = fields.Char(string="Phone")
    vendor_ceo = fields.Char(string="CEO Details")
    last_updated_on = fields.Date(string="Last updated")
    v_auth_person = fields.Char(string="Authorized Person")
    v_auth_email = fields.Char(string="Authorized Email")
    v_auth_phone = fields.Char(string="Authorized Phone")
    coi_expiry = fields.Date(string="COI Expiry Date")
    wc_expiry = fields.Date(string="WC Expiry")
    ach_selection = fields.Selection([('yes','Yes'),('no','No')],string="ACH")
    w9_selection = fields.Selection([('yes','Yes'),('no','No')],string="W9")
    addendum_link = fields.Char(string="Addendum Link")
    mailing_address = fields.Text(string="Mailing Address")
    permanent_notes = fields.Text(string="Permanent Notes")
    comments = fields.Text(string="COMMENTS")
    vendor_status = fields.Selection([('pending','Pending'),('on-bording','On-Boarding'),('in-active','In-Active')],string="STATUS",default="pending")
    payment_process = fields.Char(string="Payment Process")
    

    
    
#DOCUMENT INFORMATION
    pending_documents = fields.Char(string="Pending Documents")
#END CLIENT PAGE
    client_name = fields.Char(string="Client Name")
    client_address = fields.Text(string="Client Address")
    client_location = fields.Char(string="Client Location")
    msp_fee = fields.Char(string="MSP fee")
    background_fee = fields.Char(string="Background Fee")
    end_client = fields.Selection([('yes','Yes'),('no','No')],string="End Client")
#IF END CLIENT NO THE BELOW DETAILS WANT TO SHOW:
    boarding_website = fields.Char(string="On Boarding Website")
    payment_terms = fields.Many2one('account.payment.term',string='Payment Terms')
    management_name = fields.Char(string="Management Name")
    management_email = fields.Char(string="Management Email")
    management_contact = fields.Char(string="Management Contact Number")
    accounting_name = fields.Char(string="Accounting Name")
    accounting_email = fields.Char(string="Accounting Email")
    accounting_contact = fields.Char(string="Accounting Contact Number")
    supporting_name = fields.Char(string="Supporting Name")
    supporting_email = fields.Char(string="Supporting Email")
    supporting_contact = fields.Char(string="Supporting Contact Number")

#Creating New Fields
    model_id = fields.Char(string='Model Name',default =lambda self : self._context.get('active_model'))
          # raise ValidationError(orm)
    field_name = fields.Char(string="Field Name",default="x_")
# BINARY WIDGET
    widget = fields.Selection([('image','Image')],string="Binary Image")
# SELECTION WIDGET AND ITS VALUES
    selection_field = fields.Char(string="Selection Options")
    widget_selection = fields.Selection([('radio','Radio'),('priority','Priority')],string="Selection Widget")
#MANY2ONE WIDGET
    ref_model_id = fields.Many2one('ir.model', string='Model', index=True)
    widget_many2one = fields.Selection([('selection','Selection')],string="Many2one Selection")
#MANY2MANY WIDGET
    widget_many2many = fields.Selection([('binary','Binary'),('many2many_tags','Many2many Tags')],string="Many2many Selection")
#BASIC FIELD 
    field_description = fields.Text(string='Field Description')
    data_type = fields.Selection(SELECTION,string="Field Type")
    original_name = fields.Char(string="Demo Name") 
        
    @api.onchange('name')
    def change_name(self):
        self.original_name = self.name

          
#     @api.constrains('data_type')
#     def insert_fields(self):
#         orm_search_model = self.env['ir.model'].search([('model','=','company.details')])
#         # id_name = self.orm_search_model
#         # raise ValidationError(orm_search_model.id)
#         self.env['ir.model.fields'].sudo().create({
#             'name': self.field_name,
#             'field_description': self.field_description,
#             'model_id':  orm_search_model.id,
#             'ttype': self.data_type,
#             'relation': self.ref_model_id.model,

#             'selection': self.selection_field,
#         })
#         inherit_form_view_name = self.name + self.field_name
#         xml_id = "colab_management.colab_view_form_id"
#         inherit_id = self.env.ref(xml_id)
# #IN HERE THE attrs INVISIBLE THE name and original_name HAS BEEN USED FOR INVISIBLE THE FIELD TO THE ANOTHER COMPANY
#         arch_base = '''<?xml version="1.0"?>
#                         <data>
#                             <field name="duns_number" position="after">
#                                 <field name="%s" attrs="{'invisible': [('name','!=','%s')]}"/>
#                             </field>
#                         </data>''' % (
#                                     # self.position_field.name,
#                                     # self.position, 
#                                     self.field_name,
#                                     self.original_name)
#         if self.widget:
#             arch_base = '''<?xml version="1.0"?>
#                         <data>
#                             <field name="duns_number" position="after">
#                                 <field name="%s" widget="%s" attrs="{'invisible': [('name','!=','%s')]}"/>
#                             </field>
#                         </data>''' % (
#                                     # self.position_field.name,
#                                     # self.position, 
#                                     self.field_name,self.widget,
#                                     self.original_name)
#         if self.widget_selection:
#             arch_base = '''<?xml version="1.0"?>
#                         <data>
#                             <field name="duns_number" position="after">
#                                 <field name="%s" widget="%s" attrs="{'invisible': [('name','!=','%s')]}"/>
#                             </field>
#                         </data>''' % (
#                                     # self.position_field.name,
#                                     # self.position, 
#                                     self.field_name,self.widget_selection,
#                                     self.original_name)
#         if self.widget_many2one:
#             arch_base = '''<?xml version="1.0"?>
#                         <data>
#                             <field name="duns_number" position="after">
#                                 <field name="%s" widget="%s" attrs="{'invisible': [('name','!=','%s')]}"/>
#                             </field>
#                         </data>''' % (
#                                     # self.position_field.name,
#                                     # self.position, 
#                                     self.field_name,self.widget_many2one,
#                                     self.original_name)
                    
#         if self.widget_many2many:
#             arch_base = '''<?xml version="1.0"?>
#                         <data>
#                             <field name="duns_number" position="after">
#                                 <field name="%s" widget="%s" attrs="{'invisible': [('name','!=','%s')]}"/>
#                             </field>
#                         </data>''' % (
#                                     # self.position_field.name,
#                                     # self.position, 
#                                     self.field_name,self.widget_many2many,
#                                     self.original_name)
#         self.env['ir.ui.view'].sudo().create({
#             'name': inherit_form_view_name,
#             'type': 'form',
#             'model': "company.details",
#             'mode': 'extension',
#             'inherit_id': inherit_id.id,
#             'arch_base': arch_base,
#             'active': True
#         })
    def onhold_button(self):
        self.vendor_status = 'on-bording'

    def unapproved(self):
        self.vendor_status = 'pending'

    def inactive(self):
        self.vendor_status = 'in-active'
#create function in res.users and write in res.partner
    @api.model
    def create(self, vals):
        result = super(company, self).create(vals)
        data_users = {
            'name':result.name,
            'login':result.email
        }
        user_create = self.env['res.users'].create(data_users)
        # raise ValidationError(user_create.partner_id.id)
        partner_id = user_create.partner_id.id
        data =  self.env['res.partner'].search([('id', '=', partner_id)])
        # for record in data:
        if result.mob_nos and result.email and result.address:
            data.write({"phone":result.mob_nos,"email":result.email,"street":result.address})
        else:
            pass
        return result
# SMART BUTTON CREATION
    def job_position(self):
      
            return {
            'type': 'ir.actions.act_window',
            'name': 'job positions',
            'view_mode': 'tree,form,kanban',
            'res_model': 'hr.job',
            'domain': [('client','=',self._origin.id)]
        }


    def appplication_data(self):
        for v in self:
            v.total_job_position = self.env['hr.job'].search_count([('client','=',v._origin.id)])



    def hr_application(self):
            return {
            'type': 'ir.actions.act_window',
            'name': 'Application',
            'view_mode': 'tree,form,kanban',
            'res_model': 'hr.applicant',
            'domain': [('client','=',self._origin.id)],
            'context': {'group_by': ['job_id']}
        }


    def hr_recruitment(self):
        for v in self:
            v.tot_job_application = self.env['hr.applicant'].search_count([('client','=',v._origin.id)])

    
    def select_count(self):
            return {
            'type': 'ir.actions.act_window',
            'name': 'Selected',
            'view_mode': 'tree,form,kanban',
            'res_model': 'hr.applicant',
            'domain': [('client','=',self._origin.id),('stage_id.id','=','9')],
            'context': {'group_by': ['job_id']}
        }


    def selected_count_total(self):
        for v in self:
            v.selected_count = self.env['hr.applicant'].search_count([('client','=',self._origin.id),('stage_id.id','=','9')])
    
    # button return total job  count
    def job_application_total(self):
        
        return {
            'type': 'ir.actions.act_window',
            'name': 'Application',
            'view_mode': 'tree,form',
            'res_model': 'hr.job',
            'domain':[('client','=',self._origin.id)],
            'context': {'filter': ['no_of_recruitment']}
        }

    #compute the total job application
    def total_job_application(self):
        for v in self:
            no_of_recruitment = self.env['hr.job'].search([('client','=',v._origin.id)])
            count = 0
            for i in no_of_recruitment:
                count += i.no_of_recruitment
            v.no_of_recruitment = count     


# CREATING THE NEW FIELD IN THE EXISTING MODEL USING THE inherit
class company_inherit_with_job(models.Model):
    _inherit='hr.job'
    company_name = fields.Many2one('company.details',string="Company Name")
    all_application_count = fields.Integer(store=False)
    total_application = fields.Integer(string="Applictation",compute='application_data')
    candidate_selected = fields.Integer(string="Candidate Seleted",compute="selected_candidate")

    def selected_candidate(self):
        for rec in self:
            rec.candidate_selected = self.env['hr.applicant'].search_count([('stage_id.id','=','9'),('job_id','=',rec._origin.id)])

    def total_selected_candidate(self):
        return{
            'type': 'ir.actions.act_window',
            'name': 'Selected',
            'view_mode': 'tree,form,kanban',
            'res_model': 'hr.applicant',
            'domain': [('job_id','=',self._origin.id),('stage_id.id','=','9')],
        }

    def application_data(self):
        for v in self:
            v.total_application = self.env['hr.applicant'].search_count([('job_id','=',v._origin.id)])


    
    def application_type(self):
            return {
            'type': 'ir.actions.act_window',
            'name': 'Application',
            'view_mode': 'tree,form,kanban',
            'res_model': 'hr.applicant',
            'domain': [('job_id','=',self._origin.id)],
            'context': {'group_by': ['job_id']}
        }
    # tot_job_application =  fields.Integer("Job Vacancy" ,compute ="hr_recruitment" )
    # selected_count =  fields.Integer("Selected" ,compute ="selected_count_total" )

    # def select_count(self):
    #         return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Company',
    #         'view_mode': 'tree,form',
    #         'res_model': 'hr.job',
    #         'domain': [('client','=',self._origin.id),('job_id','=',self._origin.id)],
    #         # 'context': {'group_by': ['job_id']}
    #     }
    # def company_unique(self):
    #     for v in self:
    #         v.all_application_count = self.env['hr.applicant'].search_count([('client','=',self._origin.id),('job_id','=',self._origin.id)])

# CREATING THE NEW MODEL
class language(models.Model):
    _name = 'programming.language'
    _rec_name = 'language' 
    language = fields.Char(string="Language")

class companyType(models.Model):    
    _name = 'company.type'
    _rec_name = 'company_type' 
    company_type = fields.Char(string="Company Type")
    

class clientPosition(models.Model):    
    _name = 'client.position'
    _rec_name = 'name' 
    name = fields.Char(string="Name")
    

class documentmasters(models.Model):    
    _name = 'document.master'
    _rec_name = 'name' 
    name = fields.Char(string="Name")
 
class DocumentUpload(models.Model):
    _name = 'document.upload'
    _rec_name = 'document_master'
    
    document_id = fields.Many2one('company.details',string="Document Id")
    document_master = fields.Many2one('document.master',string="Document Name")
    name = fields.Char(string="Document Name")
    expiry_date = fields.Date(string="Expiry Date")
    upload_document = fields.Many2many('ir.attachment',string="Documents Attachment")
    document_status = fields.Selection([('pending','Pending'),('complete','Complete')],string="Documents Status")
    
class AccountantDetails(models.Model):
    _name = 'accountant.details'
    _rec_name = 'account_name'
    
    accountant_id = fields.Many2one('company.details',string="Accountant Id")
    account_name = fields.Char(string=" Contact Name")
    account_email = fields.Char(string=" Contact Email")
    account_contact_no = fields.Char(string=" Contact No")
    client_position = fields.Many2one('client.position',string="Client Positions")
    project_master_id = fields.Many2one('project.master',string="Client")
    
    
class project_master(models.Model):
    _name = 'project.master'
    _rec_name = 'company_name'
 #Company Creation PAge   
    company_name = fields.Many2one('company.details',string="Company Name")
    vendor = fields.Boolean(string='Vendor')
    pass_through = fields.Boolean(string='Pass Through')
    imp_partner = fields.Boolean(string='Implementation Partner')
    end_client_pass = fields.Boolean(string='End Client')
    referral = fields.Boolean(string='Referral')
    project_name = fields.Char(string="Project Name")
#END CLIENT PAGE
    client_name = fields.Char(string="Client Name")
    client_address = fields.Text(string="Client Address")
    client_location = fields.Char(string="Client Location")
    msp_fee = fields.Char(string="MSP fee")
    background_fee = fields.Char(string="Background Fee")
    end_client = fields.Selection([('yes','Yes'),('no','No')],string="End Client")
#IF END CLIENT NO THE BELOW DETAILS WANT TO SHOW:
    boarding_website = fields.Char(string="On Boarding Website")
    payment_terms = fields.Many2one('account.payment.term',string='Payment Terms')
    management_name = fields.Char(string="Management Name")
    management_email = fields.Char(string="Management Email")
    management_contact = fields.Char(string="Management Contact Number")
    accounting_name = fields.Char(string="Accounting Name")
    accounting_email = fields.Char(string="Accounting Email")
    accounting_contact = fields.Char(string="Accounting Contact Number")
    supporting_name = fields.Char(string="Supporting Name")
    supporting_email = fields.Char(string="Supporting Email")
    supporting_contact = fields.Char(string="Supporting Contact Number")
    client_position = fields.Many2one('client.position',string="Client Positions")
    auth_person = fields.Char(string="Authorized Person")
    auth_email = fields.Char(string="Authorized Email")
    auth_phone = fields.Char(string="Authorized Phone")
    coi_expiry = fields.Date(string="COI Expiry Date")
    wc_expiry = fields.Date(string="WC Expiry")
    ach_selection = fields.Selection([('yes','Yes'),('no','No')],string="ACH")
    w9_selection = fields.Selection([('yes','Yes'),('no','No')],string="W9")
    addendum_link = fields.Char(string="Addendum Link")
    mailing_address = fields.Text(string="Mailing Address")
    permanent_notes = fields.Text(string="Permanent Notes")
    comments = fields.Text(string="COMMENTS")
    vendor_status = fields.Selection([('in-active','In-Active'),('on-bording','On-Boarding'),('pending','Pending')],string="STATUS")
    payment_process = fields.Char(string="Payment Process")
    client_postion_line = fields.One2many('accountant.details','project_master_id',string='Client Position',ondelete='cascade')
    end_client_postion_line = fields.One2many('accountant.details','project_master_id',string='End Client Position',ondelete='cascade')    

    comment_master_line = fields.One2many('comment.line','comment_new',string='Comments',ondelete='cascade')    

class comment_line(models.Model):
    _name = 'comment.line'
    _rec_name = 'user_name'
    
    user_name = fields.Many2one('res.users',string=" Users",default=lambda self: self.env.user,tracking=True)
    comment_name = fields.Text(string=" Comments")
    date_time = fields.Datetime(string=" Update Date",default=lambda self: fields.Datetime.now().strftime('%Y-%m-%d %H:%M'))
    
    comment_new = fields.Many2one('project.master',string="Client")