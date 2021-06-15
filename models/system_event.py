# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SystemEvent(models.Model):
    _name = 'system.event'
    _rec_name = 'id'

    event_model_id = fields.Many2one('crm.lead', 'Event Model id',
                                     readonly=True)


class Lead(models.Model):
    _inherit = 'crm.lead'

    @api.model_create_multi
    def create(self, vals_list):
        crm_lead_data = self.env['crm.event.data'].sudo()
        res = super(Lead, self).create(vals_list)
        for rec in res:
            crm_lead_data.create({
                'event_model_id': rec.id
            })
        return res

    def write(self, vals):
        old_user = self.user_id.id
        old_stage = self.stage_id.id
        res = super(Lead, self).write(vals)
        changes = {}
        crm_lead_data = self.env['crm.event.data'].sudo()
        if 'user_id' in vals:
            changes['old_user_id'] = old_user
            changes['new_user_id'] = vals['user_id']
        if 'stage_id' in vals:
            changes['old_stage_id'] = old_stage
            changes['new_stage_id'] = vals['stage_id']
        if changes:
            changes['event_data_id'] = self.env['system.event'].id
            crm_lead_data.create(changes)

        return res
