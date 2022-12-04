from odoo import models, fields, api


class CotizacionesLines(models.Model):
    _name = 'wp.cotizaciones_detalle'
    _description = 'lineas de cotizaciones'

    cantidad = fields.Integer('Cantidad', required=True)
    curso_id = fields.Many2one(comodel_name='wp.cursos', string='Curso', required=True)
    importe_unitario = fields.Float('Importe Unitario', required=True)
    subtotal = fields.Float('Subtotal')

    cotizacion_id = fields.Many2one(comodel_name='wp.cotizaciones', string='Cotizacion', required=True)

