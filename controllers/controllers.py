# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectMode(http.Controller):
#     @http.route('/project_mode/project_mode', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_mode/project_mode/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_mode.listing', {
#             'root': '/project_mode/project_mode',
#             'objects': http.request.env['project_mode.project_mode'].search([]),
#         })

#     @http.route('/project_mode/project_mode/objects/<model("project_mode.project_mode"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_mode.object', {
#             'object': obj
#         })
