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

class product_template(models.Model):
        _inherit = 'product.template'

	@api.multi
	@api.model
	def compute_website_published(self):
		products = self.search([('sale_ok','=',True)])
		for product in products:
			product.website_published = product.website_published_v2 and (product.qty_available > 0)

	website_published_v2 = fields.Boolean('Website Published')

