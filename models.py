# -*- coding: utf-8 -*-

from openerp import tools, models, fields, api, _
from openerp.osv import osv
from openerp.exceptions import except_orm, ValidationError
from StringIO import StringIO
import urllib2, httplib, urlparse, gzip, requests, json
import openerp.addons.decimal_precision as dp
import logging
import datetime
import time
from openerp.fields import Date as newdate
from datetime import datetime,date,timedelta

class payment_transaction(models.Model):
        _inherit = 'payment.transaction'

	@api.model
	def create(self, vals):
		vals['partner_country_id'] = 255
        	res = super(payment_transaction, self).create(vals)
        	return res

	partner_country_id = fields.Many2one('res.country', 'Country', required=False)



class res_partner(models.Model):
        _inherit = 'res.partner'

	@api.model
	def create(self, vals):
		vals['country_id'] = 255
		vals['state_id'] = 98
        	res = super(res_partner, self).create(vals)
        	return res

class product_template(models.Model):
        _inherit = 'product.template'

	@api.multi
	@api.model
	def compute_website_published(self):
		products = self.search([('sale_ok','=',True)])
		for product in products:
			product.website_published = product.website_published_v2 and (product.qty_available > 0)

	website_published_v2 = fields.Boolean('Website Published')

