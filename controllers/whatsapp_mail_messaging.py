# -*- coding: utf-8 -*-
# from odoo import http


# class WhatsappMessaging(http.Controller):
#     @http.route('/whatsapp_messaging/whatsapp_messaging', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/whatsapp_messaging/whatsapp_messaging/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('whatsapp_messaging.listing', {
#             'root': '/whatsapp_messaging/whatsapp_messaging',
#             'objects': http.request.env['whatsapp_messaging.whatsapp_messaging'].search([]),
#         })

#     @http.route('/whatsapp_messaging/whatsapp_messaging/objects/<model("whatsapp_messaging.whatsapp_messaging"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('whatsapp_messaging.object', {
#             'object': obj
#         })

