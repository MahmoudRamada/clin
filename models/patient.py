# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from ast import literal_eval

class Patient(models.Model):
    _name = 'veterinary.patient'
    image = fields.Binary(
        "Image", attachment=True,
        help="This field holds the image used as image for the product, limited to 1024x1024px.")
    name = fields.Char('patient Name', required=True)
    seriai_number = fields.Char('ID Number',required=True)
    age = fields.Integer('Age', required=True)
    appointment_id = fields.Many2many('veterinary.appointment')
    total_appointment = fields.Char('Total',compute='_total_appointment')
    colour =fields.Selection (
        (('b','B'),('c','C'), ('g','G') ,('other','Other'))
        ,required=True)
    sex =fields.Selection ((
        ('f','F'),('m','M'))
        ,required=True)
    case =fields.Selection ((
        ('tb','TB'),('ar','AR'),
        ('wb','WB'),('p','P'),('other','Other'))
        ,required=True,string="Case")
    partner_id = fields.Many2one('res.partner',string='Owner', required=True)
    evaluation = fields.One2many('veterinary.evaluation','patient',readonly=True)

    _sql_constraints = [
    ('microchio_uniq', 'unique(seriai_number)', 'Microchip already exists!')
    ]

    @api.multi
    def _total_appointment(self):
        self.total_appointment = len(self.appointment_id)

    def appointment_view(self):
        action = self.env.ref('veterinary.action_appointment_form')
        result = action.read()[0]
        result['domain'] = [('patients', '=', self.id)]
        return result

class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Partner'
    patient_picking_id = fields.One2many('veterinary.patient','partner_id', string="patient Id")

    def open_patient(self):
        action = self.env.ref('veterinary.action_patient_form')
        result = action.read()[0]
        result['domain'] = [('partner_id', '=', self.id)]
        return result
