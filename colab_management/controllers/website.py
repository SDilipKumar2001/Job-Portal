from odoo import http
from odoo.addons.website.controllers.main import Website
from odoo.addons.portal.controllers.web import Home
from odoo.http import request
from odoo.exceptions import ValidationError
import base64

# BUTTON TYPES ARE GIVEN LIKE type="object" IF INCASE CHANGE IT LIKE type="submit"



   # @http.route()
   # def index(self, **kw):
   #     super(Website, self).index()
   #     job_description_ids =  request.env['hr.job'].search([('is_published', '=', True)])
   #     return http.request.render('website.homepage', {
   #      'job_description_ids' : job_description_ids
   #     })

   # @http.route('/login/website',type="http",auth="public",website=True)
   # def login(self,**kw):
   #    # request.env['hr.applicant'].sudo().create(kw)
   #    return request.render('colab_management.experience_page',{})
   
   # @http.route('/experience/url',type="http",auth="public",website=True)
   # def experience(self,**kw):
   #    # request.env['hr.applicant'].sudo().create(kw)
   #    return request.render('colab_management.candidate_details',{})

   # @http.route('/candidate/details',type="http",auth="public",website=True)
   # def biodata(self,**kw):
   #    # request.env['hr.applicant'].sudo().create(kw)
   #    return request.render('colab_management.company_experience',{})

   # @http.route('/company/experience',type="http",auth="public",website=True)
   # def abroad(self,**kw):
   #    # request.env['hr.applicant'].sudo().create(kw)
   #    return request.render('colab_management.abroad_redirection',{})
   
   # @http.route('/filling/data',type="http",auth="public",website=True)
   # def resume(self,**kw):
   #    # request.env['hr.applicant'].sudo().create(kw)
   #    return request.render('colab_management.updation_resume',{})
   
   # @http.route('/website/update',type="http",auth="public",website=True)
   # def thanks(self,**kw):
   #    # request.env['hr.applicant'].sudo().create(kw)
   #    return request.render('colab_management.applied_thanks',{})




# class Global(PyV8.JSClass):
#     pass

#     with PyV8.JSContext(Global()) as ctxt:
#         the_number = ctxt.eval("var pass_to_python = var id")
class Website(Home):
   @http.route()
   def index(self, **kw):
       super(Website, self).index()
       job_description_ids =  request.env['hr.job'].sudo().search([('is_published', '=', True)])
      #  company_details = request.env['company.details'].search([])
       return http.request.render('website.homepage', {
        'job_description_ids' : job_description_ids,
      #   'company_details' : company_details
       })


     
   @http.route('/first/page/<int:job_description_id>/<int:company_id>',type="http",auth="public",website=True)
   def description(self,job_description_id,company_id,**kw):
      request.session['job_position_id'] = job_description_id
      request.session['company_id'] = company_id
      # raise ValidationError(f"{job_description_id},{company_id}")
      return request.render('colab_management.login_page',{})
       
     
     
   @http.route('/login/website',type="http",auth="public",website=True)
   def login(self,**kw):
      user_name = kw.get('name','')
      login = kw.get('login','')
      pwd = kw.get('password','')
      phone = kw.get('partner_phone','')
      # number = kw.get('sel_groups_1_9_10','')
      request.session['user_name'] = user_name
      request.session['mail'] = login
      request.session['phone'] = phone
      values = {
         'name' : user_name,
         'login' : login,
         'password' : pwd,
      #   'sel_groups_1_9_10' : lambda self: self.env.user
         'sel_groups_1_9_10' : 9,
      }
      # raise ValidationError(number)
      request.env['res.users'].sudo().create(values)
      return request.render('colab_management.experience_page',{})
   
   
   
   # FOR FRESHERS PAGE
   
   
   @http.route('/fresher/url',type="http",auth="public",website=True)
   def fresher(self,**kw):
      # fresher = kw.get('exp')
      # # raise ValidationError(fresher)
      # # request.session['fresher'] = fresher
      # MANY2ONE FIELD RECORD DATAS HAS BEEN TAKEN FROM DATABASE TO THE WEBISTE
      fresher = request.env['hr.recruitment.degree'].sudo().search([])
      company = request.env['company.details'].sudo().search([])
      # language = request.env['programming.language'].sudo().search([])
      job =  request.env['hr.job'].sudo().search([('is_published', '=', True)])
      language = request.env['res.lang'].sudo().search([])
     
      # permit_ids = request.httprequest.form.getlist('known_languages')
      return request.render('colab_management.candidate_fresher',{'fresher':fresher,
                                                                  'company':company,
                                                                  'permit_ids':language,
                                                                  'job':job}) 

   @http.route('/candidate/fresher',type="http",auth="public",website=True)
   def nil_fresher(self,**kw):
      # candidate_name = kw.get('partner_name','')
      
      # client = kw.get('client','')
      # job = kw.get('job_id','')
      gender = kw.get('gender','')
      dob = kw.get('dob','')
      whats = kw.get('whats','')
      address = kw.get('address','')
      # email = kw.get('email_from','')
      mobile = kw.get('partner_mobile','')
      job = kw.get('job_id','')
      h_qualification = kw.get('h_qualification','')
      r_qualification = kw.get('r_qualification','')
      location = kw.get('location','')
      area = kw.get('area_of_interest')
      # gender_bool = kw.get("gender_bool","")
      # strength = kw.get('strength','')
      # weakness = kw.get('weak','')
      #many2many data passing
      known_languages = request.httprequest.form.getlist('known_languages')
      # known_languages = int(kw.get('known_languages'))
      # values.append(known_languages)
      # known_languages = kw.get('known_languages')
         


# BY USING SESSION TO COPY THE DATA AND WE CAN USE IT WHERE WE WANT .
# request.session['partner_name'] = candidate_name ASSIGN IT AS THE BEFORE MENTIONED
# variable = request.session['partner_name'] CALL IT LIKE THIS
      
      # request.session['partner_name'] = candidate_name
      # request.session['job']  = job
      # request.session['client'] = client
      request.session['gender'] = gender
      request.session['dob'] = dob
      request.session['whats'] = whats
      request.session['address'] = address
      # request.session['email'] = email
      request.session['mobile'] = mobile
      request.session['h_qualification'] =  h_qualification
      request.session['r_qualification'] = r_qualification
      request.session['known_languages'] = known_languages
      request.session['location'] = location
      request.session['area']  = area
      # request.session['gender_bool']  = gender_bool
      # request.session['strength'] = strength
      # request.session['weakness'] = weakness
      # raise ValidationError( request.session['gender_bool'])

      return request.render('colab_management.abroad_redirection',{})
   
   

   @http.route('/filling/data',type="http",auth="public",website=True)
   def resume(self,**kw):
      abroad = kw.get('go_abroad','')
      port = kw.get('port','')
      number = kw.get('pass_number','')

      request.session['abroad'] = abroad
      request.session['port'] = port
      request.session['number'] = number 
       
      return request.render('colab_management.updation_resume',{})
  
   @http.route('/website/update',type="http",auth="public",website=True)
   def thanks(self,**kw):


      if kw.get('res',False):
            Attachments = request.env['ir.attachment']
            name = kw.get('res').filename      
            file = kw.get('res')
            attachment = file.read()
            file_decode = base64.b64encode(attachment)
            # attach_file=file_decode.decode('utf-8') 
            attachment_id = Attachments.sudo().create({
                'name':name,
                'res_name': name,
                'type': 'binary',   
                'res_model': 'hr.applicant',
                # 'res_id': 455,
                'website_id': 1,
                'datas' :  file_decode,
                'public':True,
                # 'datas': attachment.encode('base64'),
            }) 
      # if kw.get('other',False):
      #       Attachments = request.env['ir.attachment']
      #       name = kw.get('other').filename      
      #       file = kw.get('other')
      #       attachment = file.read()
      #       file_decode = base64.b64encode(attachment)
      #       # attach_file=file_decode.decode('utf-8') 
      #       attachment_ids = Attachments.sudo().create({
      #           'name':name,
      #           'res_name': name,
      #           'type': 'binary',   
      #           'res_model': 'hr.applicant',
      #           # 'res_id': 455,
      #           'website_id': 1,
      #           'datas' :  file_decode,
      #           'public':True,
      #           # 'datas': attachment.encode('base64'),
      #       }) 
         
      # fresher = request.session['fresher']
      job_position_many2one = request.session['job_position_id']
      company_id_many2one = request.session['company_id']
      partner_name = request.session['user_name'] 
      # client = request.session['client'] 
      # job = request.session['job'] 
      gender = request.session['gender'] 
      dob = request.session['dob'] 
      whats = request.session['whats'] 
      address = request.session['address'] 
      email = request.session['mail']
      mobile = request.session['mobile'] 
      h_qualification = request.session['h_qualification'] 
      r_qualification = request.session['r_qualification'] 
      known_languages = request.session['known_languages']
      location = request.session['location'] 
      # strength = request.session['strength'] 
      # weakness = request.session['weakness'] 
      area = request.session['area']
      abroad = request.session['abroad']
      port = request.session['port']
      number = request.session['number']
      phone = request.session['phone'] 
      # gender_bool = request.session['gender_bool'] 

      values = {
         'exp' :  'fresher',
         'name' :partner_name,
         # 'client' : client,
         # 'job_id' : int(job),
         'client' : int(company_id_many2one),
         'job_id' : int(job_position_many2one),
         'gender' : gender,
         'dob' : dob,
         'whats' : whats,
         'address' : address,
         'email_from' : email,
         'partner_phone' : phone,
         'partner_mobile' : mobile,
         'h_qualification' : h_qualification,
         'r_qualification' : r_qualification,
         "known_languages" : known_languages,
         'location' : location,
         'area_of_interest' : area,
         # 'strength' : strength,
         # 'weak' : weakness,
         'go_abroad' :abroad,
         'port' : port,
         'pass_number' : number,
         'res' : attachment_id,
         # 'other' : attachment_ids,
         'partner_phone' : phone,
         # "gender_bool"   :gender_bool,
      }
      # raise ValidationError(request.session['known_languages'])
      request.env['hr.applicant'].sudo().create(values) 
      return request.render('colab_management.applied_thanks',{})
   


   # @http.route('/candidate/details',type="http",auth="public",website=True)
   # def biodata(self,**kw):
   #    return request.render('colab_management.company_experience',{})


   #FOR EXPERIENCE PAGE
   
   
   @http.route('/experience/url',type="http",auth="public",website=True)
   def experience(self,**kw):
# ERROR EXPERIENCE IS NOT GETTED
      # experience = kw.get('exp')
      # request.session['experience'] = experience
      # # MANY2ONE FIELD RECORD DATAS HAS BEEN TAKEN FROM DATABASE TO THE WEBISTE
      experience = request.env['hr.recruitment.degree'].sudo().search([])
      # job_main = request.env['hr.job'].sudo().search([('is_published', '=', True)])
      job_main = request.env['hr.job'].sudo().search([('is_published', '=', True)])
      company = request.env['company.details'].sudo().search([])
      language = request.env['res.lang'].sudo().search([])
      return request.render('colab_management.candidate_experience',{'experience':experience,
                                                                     'job_main' : job_main,
                                                                     'permit_ids':language,
                                                                     'company' : company})

   @http.route('/candidate/experience',type="http",auth="public",website=True)
   def company_experience(self,**kw):
      # candidate_name_1 = kw.get('partner_name','')
      # company = kw.get('client','')
      # job_1 = kw.get('job_id','')
      gender_1 = kw.get('gender','')
      dob_1 = kw.get('dob','')
      whats_1 = kw.get('whats','')
      address_1 = kw.get('address','')
      # email_1 = kw.get('email_from','')
      mobile_1 = kw.get('partner_mobile','')
      known_languages = request.httprequest.form.getlist('known_languages')
      # known_languages = kw.get('known_languages')
      h_qualification_1 = kw.get('h_qualification','')
      r_qualification_1 = kw.get('r_qualification','')
      location_1 = kw.get('location','')
      area = kw.get('area_of_interest','')
      # strength_1 = kw.get('strength','')
      # weakness_1 = kw.get('weak','')

      # request.session['partner_name_1'] = candidate_name_1
      # request.session['company'] = company
      # request.session['job_id'] = job_1
      request.session['gender_1'] = gender_1
      request.session['dob_1'] = dob_1
      request.session['whats_1'] = whats_1
      request.session['address_1'] = address_1
      # request.session['email_1'] = email_1
      request.session['mobile_1'] = mobile_1
      request.session['known_languages'] = known_languages
      request.session['h_qualification_1'] =  h_qualification_1
      request.session['r_qualification_1'] = r_qualification_1
      request.session['location_1'] = location_1
      request.session['area'] = area
      # request.session['strength_1'] = strength_1
      # request.session['weakness_1'] = weakness_1
      # sym={
      #           'name':main_name,
      #           'partner_name':partner_name,
      #           'gender':gender,
      #           'dob':dob,
      #           'res' : attachment_id,
      #           'other':attachment_ids,
      #       }
      # own=request.env['hr.applicant'].sudo().create(sym) 
      return request.render('colab_management.company_experience',{
                                         
      })

   @http.route('/company/experience',type="http",auth="public",website=True)
   def abroad(self,**kw):
   #USED TO CREATE THE DATA IN ONE2MANY DATAS IN THE MODEL WITH ONLY ONE DATA
      comp_name = request.httprequest.form.getlist('comp_name')
      role = request.httprequest.form.getlist('role')
      change = request.httprequest.form.getlist('change')
      from_field = request.httprequest.form.getlist('from_field')
      to_field = request.httprequest.form.getlist('to_field')
      years = request.httprequest.form.getlist('years')
      can = []
      for i in range(len(comp_name)):
         data = {
            'comp_name': comp_name[i],
            'role': role[i],
            'change': change[i],
            'from_field': from_field[i],
            'to_field': to_field[i],
            'years': years[i]
         }
         can.append(data)
      request.session['one2many_insert'] = can
      # raise ValidationError(request.session['one2many_insert'])
      # comp_name = kw.get('comp_name','')
      # role = kw.get('role','')
      # change = kw.get('change','')
      # from_field = kw.get('from_field','')
      # to_field = kw.get('to_field','')
      # years = kw.get('years','')
      last = kw.get('last','')
      salary_expected = kw.get('salary_expected','')
      information = request.httprequest.form.getlist('information')

      # sub_model=own[0]['id']

      # request.session['comp_name'] = comp_name
      # request.session['role'] = role
      # request.session['change'] = change
      # request.session['from_field'] = from_field
      # request.session['to_field'] = to_field
      # request.session['years'] = years
      request.session['last'] = last
      request.session['salary_expected'] = salary_expected
      request.session['information'] = information

      # model={
      #    'comp_name' : comp_name,
      #    'role' : role,
      #    'change' : change,
      #    'from_field' : from_field,
      #    'to_field' : to_field,
      #    'years' : years,
      #    'last' : last,
      #    'salary_expected' : salary_expected
      #    # 'detail':sub_model,
      # }
      # request.env['hr.applicant.lines'].create(model) 
      return request.render('colab_management.abroad_willing',{})
   
   
   @http.route('/abroad/data',type="http",auth="public",website=True)
   def redirection(self,**kw):
      
      abroad_1 = kw.get('go_abroad','')
      port_1 = kw.get('port','')
      number_1 = kw.get('pass_number','')

      request.session['abroad_will'] = abroad_1
      request.session['port_will'] = port_1
      request.session['number_port'] = number_1 
      # raise ValidationError(request.session['one2many_insert'])
      return request.render('colab_management.resume_attachment',{})

   @http.route('/website/resume',type="http", methods=['POST'],auth="public",website=True)
   def resume_attach(self,**kw):
      # name_list = request.httprequest.form.getlist('name[]')
      # raise ValidationError(name_list)
# https://www.odoo.com/forum/help-1/add-attachement-from-website-118903
# Refer Above Link Of Attachments
      if kw.get('res',False):
            Attachments = request.env['ir.attachment']
            name = kw.get('res').filename      
            file = kw.get('res')
            attachment = file.read()
            file_decode = base64.b64encode(attachment)
            # attach_file=file_decode.decode('utf-8') 
            experience_resume = Attachments.sudo().create({
                'name':name,
                'res_name': name,
                'type': 'binary',   
                'res_model': 'hr.applicant',
                # 'res_id': 455,
                'website_id': 1,
                'datas' :  file_decode,
                'public':True,
                # 'datas': attachment.encode('base64'),
            }) 
      absent = []
      if kw.get('att'):
         image_files = request.httprequest.files.getlist('att')
         # raise ValidationError(image_files)
         for image_file in image_files:
            name = image_file.filename
            attachment = image_file.read()
            file_encoded = base64.b64encode(attachment)
            
            attachment_vals = {
                'name': name,
                'res_name': name,
                'type': 'binary',
                'res_model': 'hr.applicant',  # Update with your model
                'website_id': 1,  # Update with your website ID
                'datas': file_encoded,
                'public': True,
            }
            absent.append( Attachments.sudo().create(attachment_vals))
      # if kw.get('other',False):
      #       Attachments = request.env['ir.attachment']
      #       name = kw.get('other').filename      
      #       file = kw.get('other')
      #       attachment = file.read()
      #       file_decode = base64.b64encode(attachment)
      #       # attach_file=file_decode.decode('utf-8') 
      #       experience_other = Attachments.sudo().create({
      #           'name':name,
      #           'res_name': name,
      #           'type': 'binary',   
      #           'res_model': 'hr.applicant',
      #           # 'res_id': 455,
      #           'website_id': 1,
      #           'datas' :  file_decode,
      #           'public':True,
      #           # 'datas': attachment.encode('base64'),
      #       }) 
         
      # experience = request.session['experience']
      partner_name_exp = request.session['user_name']
      job_position_many2one = request.session['job_position_id']
      company_id_many2one = request.session['company_id']
      gender_exp = request.session['gender_1'] 
      dob_exp = request.session['dob_1'] 
      whats_exp = request.session['whats_1'] 
      address_exp = request.session['address_1'] 
      email_exp = request.session['mail'] 
      mobile_exp = request.session['mobile_1'] 
      known_languages = request.session['known_languages']
      h_qualification_exp = request.session['h_qualification_1'] 
      r_qualification_exp = request.session['r_qualification_1'] 
      location_exp = request.session['location_1'] 
      area = request.session['area']
      # strength_exp = request.session['strength_1'] 
      # weakness_exp = request.session['weakness_1'] 
      abroad_exp = request.session['abroad_will']
      port_exp = request.session['port_will']
      number_exp = request.session['number_port']
      # comp_name = request.session['comp_name']
      # role = request.session['role']
      # change = request.session['change']
      # from_field = request.session['from_field']
      # to_field = request.session['to_field']
      # years = request.session['years']
      last = request.session['last']

      salary_expected = request.session['salary_expected']
      phone = request.session['phone']
      information = request.session['information']
      values = {
         # BEFORE
         # 'exp' :  experience,
         # AFTER 
         #I GAVE IT STATICALLY
            'exp' :  'experience',
            'name' :partner_name_exp,
            'client' : int(company_id_many2one),
            'job_id' : int(job_position_many2one),
            'gender' : gender_exp,
            'dob' : dob_exp,
            'whats' : whats_exp,
            # 'job_id' : int(apply),
            'address' : address_exp,
            'email_from' : email_exp,
            'partner_phone' : phone,
            'partner_mobile' : mobile_exp,
            "known_languages" : known_languages,
            'h_qualification' : h_qualification_exp,
            'r_qualification' : r_qualification_exp,
            'location' : location_exp,
            'area_of_interest' : area,
            # 'strength' : strength_exp,
            # 'weak' : weakness_exp,
            'go_abroad' :abroad_exp,
            'port' : port_exp,
            'pass_number' : number_exp,
            'res' : experience_resume,
            # 'other' : [(6, 0, [absent.id for absent in absent])],
            # 'other' : experience_other,
            'last' : last,
            'expected' : salary_expected,
            "information":information,
         }
      if absent:
         values = {
         # BEFORE
         # 'exp' :  experience,
         # AFTER 
         #I GAVE IT STATICALLY
            'exp' :  'experience',
            'name' :partner_name_exp,
            'client' : int(company_id_many2one),
            'job_id' : int(job_position_many2one),
            'gender' : gender_exp,
            'dob' : dob_exp,
            'whats' : whats_exp,
            # 'job_id' : int(apply),
            'address' : address_exp,
            'email_from' : email_exp,
            'partner_phone' : phone,
            'partner_mobile' : mobile_exp,
            "known_languages" : known_languages,
            'h_qualification' : h_qualification_exp,
            'r_qualification' : r_qualification_exp,
            'location' : location_exp,
            'area_of_interest' : area,
            # 'strength' : strength_exp,
            # 'weak' : weakness_exp,
            'go_abroad' :abroad_exp,
            'port' : port_exp,
            'pass_number' : number_exp,
            'res' : experience_resume,
            'other' : [(6, 0, [absent.id for absent in absent])],
            # 'other' : experience_other,
            'last' : last,
            'expected' : salary_expected,
            "information":information,
         }
         
      # request.env['hr.applicant'].sudo().create(values) 
      own = request.env['hr.applicant'].sudo().create(values)
      one2many_experience = request.session['one2many_insert']
      sub_model=own[0]['id']
      for i in range(len(one2many_experience)):
         one2many_experience[i]['detail'] = sub_model
      for rec in  one2many_experience:
         # model={
         #    'comp_name' : comp_name[rec],
         #    'role' : role,
         #    'change' : change,
         #    'from_field' : from_field,
         #    'to_field' : to_field,
         #    'years' : years,
         #    'detail':sub_model,
         # }
      # raise ValidationError(sub_model)
         request.env['hr.applicant.lines'].sudo().create(rec)
      return request.render('colab_management.applied_thanks',{})

   # @http.route('/school/card', methods=['POST', 'GET'], csrf=False, type='http', auth="user", website=True)
   # def print_id(self, **kw):[0]['id']
   #    student_id = kw['stud_id']
   #    if student_id:
   #       pdf = request.env['report'].sudo().get_pdf([student_id], 'colab_management.colab_management.candidate_summary', data=None)
   #       pdfhttpheaders = [('Content-Type', 'application/pdf'), ('Content-Length', len(pdf))]
   #       return request.make_response(pdf, headers=pdfhttpheaders)
   #    else:
   #       return request.redirect('/')

   # @http.route('/report/new/', methods=['POST', 'GET'], csrf=False, type='http', auth="user", website=True)
   # def print_id(self, **kw):
   #    pdf, _ = request.env.ref('colab_management.Action_Name').sudo().render_qweb_pdf([int(purchase_id)])
   #    pdfhttpheaders = [('Content-Type', 'application/pdf'), ('Content-Length', len(pdf)),('Content-Disposition', 'catalogue' + '.pdf;')]
   #    return request.make_response(pdf, headers=pdfhttpheaders)

















   # @http.route('/company/experience',type="http",auth="public",website=True)
   # def biodata(self,**kw):
   #    # request.env['hr.applicant'].sudo().create(kw)
   #    return request.render('colab_management.company_experience',{})

# from odoo.addons.portal.controllers.web import Home
# from odoo import http
# from odoo.http import request
# class WebsiteSort(Home):
#    @http.route()
#    def index(self, **kw):
#        super(WebsiteSort, self).index()
#        website_product_ids = request.env['product.template'].search([('is_published', '=', True)])
#        return request.render('website.homepage', {
#            'website_product_ids': website_product_ids
#        })


