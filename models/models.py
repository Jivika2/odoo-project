#-*- coding: utf-8 -*-

from odoo import models, fields, api


class project_mode(models.Model):
    # _name = 'project.project'
    # _description = 'project_mode.project_mode'
    _inherit="project.project"
    custom_J=fields.Char()
    laxmi=fields.Char(string="LAXMI")
    money=fields.Monetary()
    num=fields.Integer()
    

    # name = fields.Char()
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
