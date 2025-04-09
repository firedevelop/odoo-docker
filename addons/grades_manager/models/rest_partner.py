from odoo import models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_teacher = fields.Boolean(string='Is teacher')
