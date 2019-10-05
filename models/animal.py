# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from ast import literal_eval

class Patient(models.Model):
    _name = 'veterinary.Patient'
    image = fields.Binary(
        "Image", attachment=True,
        help="This field holds the image used as image for the product, limited to 1024x1024px.")
    name = fields.Char('Patient Name', required=True)
    microchip_number = fields.Char('Microchip Number',required=True)
    age = fields.Integer('Age', required=True)
    appointment_id = fields.Many2many('veterinary.appointment')
    total_appointment = fields.Char('Total',compute='_total_appointment')
    colour =fields.Selection (
        (('b','B'),('c','C'), ('g','G') ,('other','Other'))
        ,required=True)
    sex =fields.Selection ((
        ('f','F'),('m','M'), ('g','G'))
        ,required=True)
    bread =fields.Selection ((
        ('tb','TB'),('ar','AR'),
        ('wb','WB'),('p','P'),('other','Other'))
        ,required=True,string="Breed & Use")
    partner_id = fields.Many2one('res.partner',string='Owner', required=True)
    evaluation = fields.One2many('veterinary.evaluation','Patient',readonly=True)

    _sql_constraints = [
    ('microchio_uniq', 'unique(microchip_number)', 'Microchip already exists!')
    ]

    @api.multi
    def _total_appointment(self):
        self.total_appointment = len(self.appointment_id)

    def appointment_view(self):
        action = self.env.ref('veterinary.action_appointment_form')
        result = action.read()[0]
        result['domain'] = [('Patients', '=', self.id)]
        return result

class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Partner'
    Patient_picking_id = fields.One2many('veterinary.Patient','partner_id', string="Patient Id")

    def open_Patient(self):
        action = self.env.ref('veterinary.action_Patient_form')
        result = action.read()[0]
        result['domain'] = [('partner_id', '=', self.id)]
        return result
