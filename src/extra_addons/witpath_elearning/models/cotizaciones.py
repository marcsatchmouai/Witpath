from odoo import models, fields, api
from datetime import datetime, timedelta

class Cotizaciones(models.Model):
    _name = 'wp.cotizaciones'
    _description = 'cotizaciones'

    fecha_emision = fields.Datetime('Fecha emision')
    fecha_inicio = fields.Datetime('Fecha de inicio')
    fecha_aceptacion = fields.Datetime('Fecha de aceptacion')
    fecha_fin = fields.Datetime('Fecha de finalizacion')
    state = fields.Selection(
        [('pendiente', 'Pendiente'),
         ('aceptada', 'Aceptada'),
         ('vencida', 'Vencida'),
         ('cancelada', 'Cancelada')],
        default='pendiente')
    cantidad_cursos = fields.Integer('Cantidad Cursos')
    cantidad_alumnos = fields.Integer('Cantidad Alumnos')
    importe = fields.Float('Importe')
    iva = fields.Float('IVA')
    descuento = fields.Float('Descuento')

    # relaciones entre tablas
    cliente = fields.Many2one(comodel_name='wp.clientes', string='Cliente')
    cursos = fields.Many2many(comodel_name='wp.cursos', string='Cursos')

    # Funciones
    @api.onchange("fecha_aceptacion")
    def _onchange_fecha_aceptacion(self):
        vencimiento = self.fecha_emision + timedelta(days=10)
        if self.fecha_aceptacion <= vencimiento:
            self.state = "aceptada"
        else:
            self.state = "vencida"
