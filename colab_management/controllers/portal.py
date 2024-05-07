from odoo import http
from odoo.http import request
from odoo.exceptions import ValidationError
from odoo.addons.portal.controllers.portal import CustomerPortal


# PORTAL MENUS ARE PRESENT AFTER THAT ARCHIVE THE UNWANTED RECORDS AND IT WILL NEVER DISPALY IN THE PORTAL MENU
# 1) Setting>>Technical>>UserInterface>>Views
# 2) filter "inerithed view" column to "my portal"
# 3) filter "view type" column  to "Qweb"




# WHAT HAPPENS WHEN THE PORTAL MENU CLICKED SHORTLY CALLED MENUITEM ACTION
class Customer(CustomerPortal):
    @http.route(['/my/job_portal', '/my/job_portal/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_job(self, **kw):
        default= request.env.uid
        jobs=http.request.env['res.users'].search([('id','=',default)])
        val = jobs.name
        vals = jobs.login
        login_user=http.request.env['hr.applicant'].search([('email_from','=',vals)])
        # login_user=http.request.env['hr.applicant'].search([('name','=',val)])
        # vals = jobs.login
        # email=http.request.env['hr.applicant'].search(['email_from','=',vals])
        # raise ValidationError(email)
        # partner=request.env['hr.job']
        return request.render("colab_management.portal_job_application",{
            'jobs':login_user,
# This is used to pass because for give the menu name in the top near home button in portal
            'page_name' : 'job',
        })

        
    @http.route('/candidate/pdf/<path:candidate_name>/<int:candidate_id>', methods=['POST', 'GET'], csrf=False, type='http', auth="user", website=True)
    def print_id(self,candidate_name,candidate_id, **kw):
        if candidate_id:
            pdf = request.env.ref('colab_management.report_candidate_summary').sudo()._render_qweb_pdf([candidate_id])[0]
            pdfhttpheaders = [('Content-Type', 'application/pdf'), ('Content-Length', len(pdf))]
            filename = f"{candidate_name}'s_Application.pdf"
            pdfhttpheaders.append(('Content-Disposition', f'attachment; filename={filename}'))
            return request.make_response(pdf, headers=pdfhttpheaders)
        else:
            return request.redirect('/')
        
    @http.route('/my/job_portal/status/<model("hr.applicant"):jobs>/',type="http",auth="user",website=True)
    def my_application_portal(self,job):
        return http.request.render("colab_management.status",{'job':job})
# page=1,date_begin=None, date_end=None,

# TO COUNT THE RECORDS PRESENTED IN THE WEB APP
class CustomerPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super(CustomerPortal,self)._prepare_home_portal_values(counters)
        # count_job= http.request.env['hr.applicant'].search_count([])
        default= request.env.uid
        jobs=http.request.env['res.users'].search([('id','=',default)])
        val = jobs.name
        vals = jobs.login
        if 'count_job' in counters:
            login_user=http.request.env['hr.applicant'].search_count([('email_from','=',vals)])
            values.update({
                'count_job':login_user,
            })
        return values