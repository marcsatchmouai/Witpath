from odoo import models, fields, api


class Cotizaciones_lines(models.Model):
    _name = 'wp.cotizaciones_lines'
    _description = 'lineas de cotizaciones'

    cantidad = fields.Integer('Cantidad', required=True)
    curso_id = fields.Many2one(comodel_name='wp.cursos', string='Curso', required=True)
    importe_unitario = fields.Float('Importe Unitario', required=True)
    subtotal = fields.Float('Subtotal')

