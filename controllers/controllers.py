# -*- coding: utf-8 -*-
from odoo import http

# class KumoriDemo(http.Controller):
#     @http.route('/kumori_demo/kumori_demo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kumori_demo/kumori_demo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kumori_demo.listing', {
#             'root': '/kumori_demo/kumori_demo',
#             'objects': http.request.env['kumori_demo.kumori_demo'].search([]),
#         })

#     @http.route('/kumori_demo/kumori_demo/objects/<model("kumori_demo.kumori_demo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kumori_demo.object', {
#             'object': obj
#         })