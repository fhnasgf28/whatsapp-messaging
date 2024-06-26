# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from itertools import groupby
from odoo.exceptions import UserError


class accountMove(models.Model):
    _inherit = 'orderfaz.product'
    _description = 'Orderfaz Product inherit messaging'

    def action_send_whatsapp(self):
        compose_form_id = self.env.ref('whatsapp_messaging.whatsapp_send_message_view_form').id
        ctx = dict(self.env.context)
        message = (
                "Hi" + " " + self.partner_id.name + ',' + '\n' +
                "Here is your invoice" + ' ' + self.user_id.name + ' ' + "amounting" + ' ' + str(
            self.uom_qty) + self.curency_id.symbol + ' ' +
                "from" + self.phone + ".Please remit payment at your earliest convenience. " + '\n'
                + "Please use the following communication for your payment" + ' ' + self.partner_id.name
        )
        ctx.update({
            'default_message': message,
            'default_partner_id': self.partner_id.id,
            'default_mobile': self.partner_id.mobile,
            'default_image_1920': self.partner_id.image_1920,
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
    def check_customer(self, partner_ids):
        partners = groupby(partner_ids)
        return next(partners, True) and not next(partners, False)
    def action_whatsapp_multi(self):
        """Initiate WhatsApp messaging for multiple invoices and open a message
               composition wizard."""

        account_move_ids = self.env['account.move'].browse(self.env.context.get('active_ids'))
        partner_ids = []
        for account_move in account_move_ids:
            partner_ids.append(account_move.partner_id.id)
        partner_check = self.check_customer(partner_ids)
        if partner_check:
            account_move_numbers = account_move_ids.mapped('name')
            account_move_numbers = "\n".join(account_move_numbers)
            compose_form_id = self.env.ref('whatsapp_mail_messaging.whatsapp_send_message_view_form').id
            ctx = dict(self.env.context)
            message = ("Hi" + " " + self.partner_id.name + ',' + '\n' +
                       "Your Orders are" + '\n' + account_move_numbers + ' ' + "is ready for review.Do not hesitate to contact us if "
                                                                               "you have any questions.")
            ctx.update({
                'default_message': message,
                'default_partner_id': account_move_ids[0].partner_id.id,
                'default_mobile': account_move_ids[0].partner_id.mobile,
                'default_image_1920': account_move_ids[0].partner_id.image_1920,
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
        else:
            raise UserError(_(
                'It appears that you have selected orders from multiple'
                ' customers. Please select orders from a single customer.'
            ))
