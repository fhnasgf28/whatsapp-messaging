# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from itertools import groupby


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = 'whatsApp sale order'

    def action_send_whatsapp(self):
        compose_form_id = self.env.ref(
            'whatsapp_mail_messaging.whatsapp_send_message_view_form'
        ).id
        ctx = dict(self.env.context)
        message = ("Hi", " " + self.partner_id.name + ',' + '\n' +
                   "Your quotation" + ' ' + self.name + ' ' + "amounting" + ' '
                   + str(self.amount_total) + self.currency_id.symbol + ' ' +
                   "is ready for review.Do not hesitate to contact us if you "
                   "have any questions.")
        ctx.update({
            'default_message': message,
            'default_partner_id': self.partner_id.id,
            'default_mobile': self.partner_id.mobile,
            'default_image_1920': self.partnerr_id.image_1920,
        })
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'whatsapp.send.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
            'context': ctx,
        }

    def action_whatsapp_multi(self):
        return