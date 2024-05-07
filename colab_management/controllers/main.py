from distutils.filelist import findall
from requests import Session
from odoo import http
import odoo.http as http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.addons.portal.controllers.portal import pager as portal_pager, CustomerPortal
from odoo.addons.website.controllers.main import Website
from odoo.exceptions import ValidationError
import base64
import xml.etree.ElementTree as ET



# class employee(http.Controller):
# # This controller is used to loading the page when you clicking on the menu button.
#     @http.route('/website_job',type="http",auth="public",website=True)
#     def apply_job(self,**kw):
       
#         return http.request.render('colab_management.application_page',{})


#     @http.route('/website/page1',type="http",auth="public",website=True)
#     def job_page(self,**kw): 
        
#         main_name=kw.get('name',False)

#         syk={
#             'name':main_name,
#         }
#         # first = request.env['hr.applicant'].create(syk)
#         return request.render('colab_management.redirect_page2',{})
          
        


#     @http.route('/filling/biodata',type="http",auth="public",website=True)
#     def create_new(self,**kw): 
#         # experience=kw.get('exp',False)
#         main_name=kw.get('name',False)
#         partner_name=kw.get('partner_name',False)
#         gender=kw.get('gender',False)
#         dob=kw.get('dob',False) 
#         sym={   
#                 'name':main_name,
#                 'partner_name':partner_name,
#                 'gender':gender,
#                 'dob':dob,
#                 # 'res' : attachment_id,
#                 # 'other':attachment_ids,
#             }
#         request.env['hr.applicant'].sudo().create(sym)
#         return request.render('colab_management.applied_thanks',{})


# TO TAKE THE MANY2ONE DATAS FROM DATABASE TO WEBSITE
# PYTHON CODE:
# @http.route('/website_job',type="http",auth="public",website=True)
# def apply_job(self,**kw):
#         many2one_connect = request.env['many2one_module_name'].sudo().search([])
#         return http.request.render('colab_management.application_page',{'many2one_connect':many2one_connect})

# XML CODE:
# <div class="form-group">
# <label for="field_name" class="control-label">Administrator</label>
# <select name="field_name" class="form-control link-style">
#     <t t-foreach="many2one_connect" t-as="connect">
#         <option t-esc="connect.name" t-att-value="connect.id"/>
#     </t>
# </select>
# </div>


    # @http.route('/website_job',type="http",auth="public",website=True,csrf=False)
    # def apply_job(self,**kw):
    #     # values = super(CustomerPortal, self).apply_job()
    #     return http.request.render('colab_management.survey_form_template')

    

class CustomerPortal(http.Controller):
    @http.route('/website_job',type="http",auth="public",website=True)
    def apply_job(self,**kw):       
        return http.request.render('colab_management.application_page',{})

    # @http.route('/website/steel',type="http",auth="public",website=True)
    # def maintain(self,**kw):
        
    #     collect=request.env['hr.applicant'].sudo().search([])
    #     return request.render("colab_management.retrive_data",{
           
    #         'collect':collect
    #     })

    @http.route('/website/page1',type="http",auth="public",website=True)
    def job_page(self,**kw):
        exp = kw.get('exp','')
        name = kw.get('name','')
        request.session['exp_candi'] = exp
        request.session['name_candi'] = name
        job_main = request.env['hr.job'].sudo().search([('is_published', '=', True)])
        return request.render('colab_management.direct_redirection',{'job_main':job_main})

    @http.route('/fill/experience',type="http",auth="public",website=True)

    #TO ATTACH THE PDF IN THE WEBSITE WE USE THE { enctype="multipart/form-data" } METHOD HAS TO BEEN 
    # USED IN THE form TAG IN XML FILE 

    def thanks(self,**kw):
        if kw.get('res',False):
            Attachments = request.env['ir.attachment']
            name = kw.get('res').filename      
            file = kw.get('res')
            attachment = file.read()
            file_decode = base64.b64encode(attachment)
            attachment_id = Attachments.sudo().create({
                'name':name,
                'res_name': name,
                'type': 'binary',
                'res_model': 'hr.applicant',
                'website_id': 1,
                'datas' :  file_decode,
                'public':True,
            })

        
        exp = request.session['exp_candi']
        name = request.session['name_candi']
        job_id=request.session['job_name']
       
        # wax = []
        # tree = ET.parse('from_field')
        # root = tree.getroot()

        # for vehicle in root.findall('vehicle'):
        #     id = vehicle.get('from_field')
        #     wax.append(id)
    #    from_field = 
        
        values = {
            'exp' : exp,
            'name' : name,
        }

        # own = request.env['hr.applicant'].create(values)
        # sub = own[0]['id']
        # sub = own.id

        # number = kw.get('numberArray')
        from_field = kw.get('from_field') 
        to_field = kw.get('to_field')
        # raise ValidationError(from_field)

        gen = {
            'from_field' : from_field,
            'to_field' : to_field,
            # 'detail' : sub,
        }
        qon = request.env['hr.applicant.lines'].create(gen)
        values_1 = {
            'job_id' : qon,
        }
        request.env['hr.applicant.lines'].create(values_1)
        # http.request.env['hr.applicant'].sudo().browse(kw.get('id')).write(
        #     {
        #         'partner_name': kw.get('partner_name'),
        #         'dob' : kw.get('dob')
        #     })
        # lines = [(0,self.first.id, {
        #     'partner_name': partner_name,
        #     'dob': dob,
        # })]


        # main = self.env['hr.applicant'].search([], limit=1)
        # main.partner_name ="dilip"
        # main.write({'partner_name' : 'dilip'}) 
        # values.update= {
        #     'partner_name': partner_name,
        #     'dob':dob,
        #     'gender':gender

        # }
        # attach =request.env['hr.applicant'].sudo().browse(int(self.create_applicant)).write(values)
        # raise ValidationError(values)
       
        return http.request.render('colab_management.applied_thanks',{})
       


# This controller is used to loading the page when you clicking on the menu button.
    @http.route('/website_job',type="http",auth="public",website=True)
    def apply_job(self,**kw):
        return http.request.render('colab_management.application_page',{})


    # @http.route('/website/page1',type="http",auth="public",website=True)
    # def job_page(self,**kw): 
    #     return request.render('colab_management.redirect_page2',{})


    # @http.route('/filling/biodata',type="http",auth="public",website=True)
    # def page_job(self,**kw):
    #     return request.render('colab_management.direct_redirection',{})

    # @http.route('/fill/experience',type="http",auth="public",website=True)
    # def exp_job(self,**kw):
    #     return request.render('colab_management.abroad_redirection',{})

    # @http.route('/filling/data',type="http",auth="public",website=True)
    # def abroad_data(self,**kw):
    #     return request.render('colab_management.updation_resume',{})    

    # @http.route('/website/next',type="http",auth="public",website=True)
    # def create_new(self,**kw): 
    #     return request.render('colab_management.applied_thanks',{})

# class employee(http.Controller):

        # main_name=kw.get('name',False)
        # partner_name=kw.get('partner_name',False)
        # gender=kw.get('gender',False)
        # dob=kw.get('dob',False) 
        # sym={
        #         'name':main_name,
        #         'partner_name':partner_name,
        #         'gender':gender,
        #         'dob':dob,
        #         # 'res' : attachment_id,
        #         # 'other':attachment_ids,
        #     }
        # request.env['hr.applicant'].sudo().create(sym)
# # This controller is used to loading the page when you clicking on the menu button.
#     @http.route('/website_job',type="http",auth="public",website=True)
#     def extract_data(self,**kw):        

#         return http.request.render('colab_management.application_page',{}) 

#     @http.route('/website/page1',type="http",auth="public",website=True)
#     def create_new(self,**kw):
#         # own=request.env['hr.applicant'].sudo().create(sym)
        

        
        
#         # comp_name=request.httprequest.form.getlist('comp_name')
#         # # raise ValidationError(len(comp))
#         # # comp=json.loads(kw['comp_name'])
#         # # data = ast.literal_eval(comp)
#         # # role=kw.get('role','')
#         # # change=kw.get('change','')

#         # sub_model=own[0]['id']
#         # lines = [(0, 0, {
#         #     'comp_name': comp_name,
#         #     'detail': sub_model,
#         # }) for comp_name in zip(comp_name)]

#         # for i in range(1):
#         # for i,j,k in zip(comp,role,change):
#         # for i in enumerate(comp):
#         # for i in comp:
#         #     model={
#         #             'comp_name':str(comp),
#         #             # 'role':j,
#         #             # 'change':k,
#         #             'detail':sub_model,
#         #             }
#         # product_line.append((0,0,model))
#         # product_line.append[(0,0,{comp}), (0,0,{sub_model})]
#         # request.env['hr.applicant.lines'].create(lines)
#         # # request.env['hr.applicant.lines'].create(product_line)
#         # return request.render('colab_management.applied_thanks',{})

#         main_name=kw.get('name',False)
#         partner_name=kw.get('partner_name',False)
#         gender=kw.get('gender',False)
#         dob=kw.get('dob',False)
             

#         #CREATE AN ATTACHMENT   
#         # if kw.get('res',False):
#         Attachments = request.env['ir.attachment']
#         name = kw.get('res').filename      
#         file = kw.get('res')
#         attachment = file.read()
#         file_decode = base64.b64encode(attachment)
#         # attach_file=file_decode.decode('utf-8') 
#         attachment_id = Attachments.sudo().create({
#             'name':name,
#             'res_name': name,
#             'type': 'binary',   
#             'res_model': 'hr.applicant',
#             # 'res_id': 455,
#             'website_id': 1,
#             'datas' :  file_decode,
#             'public':True,
#             # 'datas': attachment.encode('base64'),
#         })
            

#         # if kw.get('other',False):
#         Attachments = request.env['ir.attachment']
#         names = kw.get('other').filename      
#         file = kw.get('other')
#         attachment = file.read()
#         file_decode = base64.b64encode(attachment)
#         # attach_file=file_decode.decode('utf-8') 
#         attachment_ids = Attachments.sudo().create({
#             'name':names,
#             'res_name': names,
#             'type': 'binary',   
#             'res_model': 'hr.applicant',
#             # 'res_id': 455,
#             'website_id': 1,
#             'datas' :  file_decode,
#             'public':True,
#             # 'datas': attachment.encode('base64'),
#         }) 
            
       
#         sym={
#                 'name':main_name,
#                 'partner_name':partner_name,
#                 'gender':gender,
#                 'dob':dob,
#                 'res' : attachment_id,
#                 'other':attachment_ids,
#             }
#         own=request.env['hr.applicant'].sudo().create(sym) 

#         # 'res' : attachment_id,
#         #             'other':attachment_ids,
    
#         #USED TO CREATE THE DATA IN ONE2MANY DATAS IN THE MODEL WITH ONLY ONE DATA 
#         comp_name=kw.get('comp_name','')
#         role=kw.get('role','')
#         change=kw.get('change','')
#         from_field=kw.get('from_field','')
#         to_field=kw.get('to_field','')
#         years=kw.get('years','')
#         sub_model=own[0]['id']
#         model={
#             'comp_name':comp_name,
#             'role':role,
#             'change':change,
#             'from_field':from_field,
#             'to_field':to_field,
#             'years':years,
#             'detail':sub_model,
#         }
#         request.env['hr.applicant.lines'].create(model) 
         

            

#         # request.env['hr.applicant'].browse(own.id).write({'res':attachment_id.id})
#         return request.render('colab_management.applied_thanks',{})
        # return request.render('colab_management.applied_thanks')




    # @http.route('/website/page1',type="http",auth="public",website=True)
    # def create_new(self,**kw):
        
    #     request.env['hr.applicant'].sudo().create(kw)  
    #     return request.render('colab_management.applied_thanks',{})
            
   
           
        
       # comp_name=kw.get('comp_name','')
        # role=kw.get('role','')
        # change=kw.get('change','')

        # var=request.env['hr.applicant'].sudo().create(kw)  
        # vs=var[0]['id'] 
        # sym={
        #     'comp_name':comp_name,
        #     'role':role,
        #     'change':change,
        #     'details':vs,
        #     }


    # CREATE THE DATA OR RECORDS IN THE ODOO MODEL USING GET METHOD
    # @http.route('/website/page1',type="http",auth="public",website=True)
    # def create_new(self,**kw):

    #     name=kw.get('name',False)
    #     partner_name=kw.get('comp_name',False)
    #     gender=kw.get('gender',False)
    #     dob=kw.get('dob',False)
    #     sym={
    #         'name':name,
    #         'partner_name':partner_name,
    #         'gender':gender,
    #         'dob':dob,
    #     }
        
       
    #     request.env['hr.applicant'].sudo().create(sym)

    #     return request.render('colab_management.applied_thanks',{})
       
       

################new








    # @http.route('/website/page1',type="http",auth="public",website=True)
    # def applying_jobs(self,**kw):
    #     request.env['hr.applicant'].sudo().create(kw)   
    #     return request.render('colab_management.applied_thanks',{})
        # raise ValidationError(self)

       
        # request.env['hr.applicant'].sudo().create(kw)
           
    # @http.route('/website/page1',type="http",auth="public",website=True)
    # def applying_jobs(self,**kw):
    #     res=kw.get('res', '')
    #     name=kw.get('name','')
    #     request.env['hr.applicant'].sudo().create({
    #         'name':name,
    #         'res':res,
    #     })
    #     request.env['hr.applicant'].sudo().browse(223).write({'weak': type(name)})
    #     return http.request.render('colab_management.applied_thanks',{}) 


# @http.route('/website/page1',type="http",auth="public",website=True)
# def applying_jobs(self,**kw):
#     request.env['hr.applicant'].sudo().create(kw)  
#     return http.request.render('colab_management.applied_thanks',{})
            # return request.render("modulename.template_to_render", value)
        # name = kw.get('name')
        # var = {
        #     'name': name,
        #     'type': 'binary', 
        #     'datas':res,
            # 'store_fname': name,

        # 'res_model': self._name,
            # 'res_id':10,
            # 'mimetype': 'application/pdf',
            # 'public': True,
    # }
        # attach = request.env['ir.attachment'].sudo().create(var)
        # if attach:
        #     pdf_id = attach.id
        # request.env['hr.applicant'].sudo().create({'name': name,'res':res})

       







                                                                                #THIS CODE IS USED TO TAKE THE MANY2ONE FIELDS TO WEBSITE
                                                                                # job_rec=request.env['hr.job'].sudo().search([])
                                                                                # type_rec=request.env['hr.recruitment.degree'].sudo().search([])
                                                                                #THE FIRST TWO IS MANY2ONE FIELD AND ONE IS USED TO ASSIGN THE DEFAULT FIELD IN WEBSITE TO FIELDS 
                                                                                # return http.request.render('colab_management.application_page',{'job_rec':job_rec,
                                                                                #                                                                              'type_rec':type_rec,
                                                                                #                                                                               'availability':'2002-07-15'})


                                                                                # raise ValidationError("not found")

                                                                                # res_if= request.env['ir.attachment'].sudo().create([('res')])    
                                                                                # res=[[6,True,[2315]]]
                                                                                # raise ValidationError(d)


                                                                                # @http.route('/website/page1',type="http",auth="public",website=True)
                                                                                # def job_page(self,**kw):
                                                                                #     request.env['hr.applicant'].sudo().create(kw)   
                                                                                #     return request.render('colab_management.redirect_page2',{})



   
    
   
   
   
   
   
   
   
   
   
    # @http.route('/website/next',type="http",auth="public",website=True)
    # def apply_job(self,**kw):
    #     return request.render('colab_management.page_redirection',{})


    # @http.route('/website/next',type="http",auth="public",website=True)
    # def page_job(self,**kw):
    #         return request.render('colab_management.page_redirection',{})


    
    
    # This controller is used to creating the records in the whole back-end in odoo database.
    # @http.route('/create/application',type='http',auth='public',website=True)
    # def create_new(self,**kw):
    #     request.env['hr.applicant'].sudo().create(kw)   
    #     return request.render('colab_management.applied_thanks',{})
   
    
    
   
    # this code is used to add the same data in more than one menus in the same model
    # data_adding={
    #     'name': kw.get('partner_name')
    # }
    # request.env['hr.applicant'].sudo().create(data_adding)

    # def function(self,**kw):  
    #     fh = open("imageToSave.png", "wb")
    #     fh.write(img_data.decode('base64'))
    #     fh.close()

    # # or, more concisely using with statement
    # with open("imageToSave.png", "wb") as fh:
    #     fh.write(img_data.decode('base64'))
    

# THIS CODE IS USED TO RETRIVE THE DATA FROM THE ODOO TO THE DATABASE
# from odoo import http
# from odoo.http import request
# class implement(http.Controller):
#     @http.route('/website/steel',type="http",auth="public",website=True)
#     def maintain(self,**kw):
#         patient=request.env['hr.applicant'].sudo().search(['state','in',['stage_id',]])
#         collect=request.env['hr.applicant'].sudo().search([])
#         # return request.render("colab_management.retrive_data",{
#         #     'patient':patient,
#         #     'collect':collect
#         # })
#         return request.render("colab_management.retrive_data",{
#             'patient':patient,
#             'collect':collect
#         })


# THIS CODE IS USED TO WHEN YOU ENTER INTO THE JOB PORTAL WHAT MUST BE DISPLAY.
# +++++++class Customer(CustomerPortal):
#     @http.route(['/my/job_portal', '/my/job_portal/page/<int:page>'], type='http', auth="user", website=True)
#     def portal_my_job(self, **kw):
#         jobs=http.request.env['hr.applicant'].search([])
#         # partner=request.env['hr.job']
#         # domain=[]

#         # stage=request.env['stage_id']
#         # domain=[]
#         # if date_begin and date_end:
#         #     domain += [('create_date', '>', date_begin), ('create_date', '<=', date_end)]
#         # values.update({
#         #     # 'date': date_begin,
#         #     'partner':partner,
#         #     # 'stage':stage,
#         #     'default_url':'/my/job_portal',
#         # })
#         return request.render("colab_management.portal_job_application",{
#             'jobs':jobs,
#         })

# # page=1,date_begin=None, date_end=None,


# class CustomerPortal(CustomerPortal):

#     def _prepare_home_portal_values(self, counters):
#         values = super()._prepare_home_portal_values(counters)
#         if 'count_job' in counters:
#             values['count_job'] = request.env['hr.applicant'].search_count([])
#             count_job= request.env['hr.applicant'].search_count([])
#             values.update({
#                 'count_job':count_job,
#             })
#         return values

   
        #     ('state', 'in', ['purchase', 'done', 'cancel'])
        # ]) if request.env['purchase.order'].check_access_rights('read', raise_exception='') else 0
