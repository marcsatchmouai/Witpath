from odoo import models, fields, api


class Contratos(models.Model):
    _name = 'wp.contratos'
    _description = 'contratos'

    fecha_inicio = fields.Date('Fecha de inicio')
    fecha_fin = fields.Date('Fecha de finalizacion')
    cantidad_alumnos = fields.Integer('Cantidad Alumnos')
    importe = fields.Float('Importe')

    # relaciones entre tablas
    cliente_id = fields.Many2one(comodel_name='wp.clientes', string='Cliente')
    cotizacion_id = fields.Many2one(comodel_name='wp.cotizaciones', string='Cotizacion')

