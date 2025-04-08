# -*- coding: utf-8 -*-
# from odoo import http


# class MiModuloPersonal(http.Controller):
#     @http.route('/mi_modulo_personal/mi_modulo_personal', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mi_modulo_personal/mi_modulo_personal/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mi_modulo_personal.listing', {
#             'root': '/mi_modulo_personal/mi_modulo_personal',
#             'objects': http.request.env['mi_modulo_personal.mi_modulo_personal'].search([]),
#         })

#     @http.route('/mi_modulo_personal/mi_modulo_personal/objects/<model("mi_modulo_personal.mi_modulo_personal"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mi_modulo_personal.object', {
#             'object': obj
#         })

