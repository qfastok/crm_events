# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CRMEventData(models.Model):
    _name = 'crm.event.data'

    event_data_id = fields.Many2one('system.event', 'Event data id',
                                    readonly=True, delegate=True)
    old_user_id = fields.Many2one('res.users', string='Old User',
                                  readonly=True)
    new_user_id = fields.Many2one('res.users', string='New User',
                                  readonly=True)
    old_stage_id = fields.Many2one('crm.stage', string='Old Stage',
                                   readonly=True)
    new_stage_id = fields.Many2one('crm.stage', string='New Stage',
                                   readonly=True)
