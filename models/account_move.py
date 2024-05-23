# -*- coding: utf-8 -*-

from odoo import models, fields, api


class accountMove(models.Model):
    _inherit = 'account.move'
    _description = 'whatsapp_messaging.whatsapp_messaging'

    def action_send_whatsapp(self):
        compose_form_id = self.env.ref('whatsapp_messaging.whatsapp_send_message_view_form').id
        ctx = dict(self.env.context)
        message = (
                "Hi" + " " + self.partner_id.name + ',' + '\n' +
                "Here is your invoice" + ' ' + self.name + ' ' + "amounting" + ' ' + str(
            self.amount_total) + self.currency_id.symbol + ' ' +
                "from" + self.company_id.name + ".Please remit payment at your earliest convenience. " + '\n'
                + "Please use the following communication for your payment" + ' ' + self.name
        )
        ctx.update({
            'default_message': message,
            'default_partner_id': self.partner_id.id,
            'default_mobile': self.partner_id.mobile,
            'default_image_1920': self.partner_id.image_920,
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
