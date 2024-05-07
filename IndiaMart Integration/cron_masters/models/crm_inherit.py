from odoo import api,fields,models


class crmproduct(models.Model):
    _inherit = 'crm.lead'

    product_requested = fields.Char(string="Product Requested")
    query_date = fields.Datetime(string="Date")
    message = fields.Html(string="Message")