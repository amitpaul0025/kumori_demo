# -*- coding: utf-8 -*-

from odoo import models, fields, api

class kumoriRequest(models.Model):
    _name = 'kumori.request'
    _description = 'Kumori Request'

    name = fields.Char(string="Request", required="true")
    date_from = fields.Datetime(string="Starting Date", default=fields.Datetime.now())
    date_to = fields.Datetime(string="End Date", required="false")
    employee_id = fields.Many2one(comodel_name="hr.employee", string="Employee", required="true")
    car_id = fields.Many2one(comodel_name="fleet.vehicle", string="Car", required="true")
    


    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     self.value2 = float(self.value) / 100