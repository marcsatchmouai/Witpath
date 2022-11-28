from odoo import models, fields, api


class Cotizaciones(models.Model):
    _name = 'wp.cotizaciones'
    _description = 'cotizaciones'

    fecha_emision = fields.Date('Fecha emision')
    fecha_inicio = fields.Date('Fecha de inicio')
    fecha_aceptacion = fields.Date('Fecha de aceptacion')
    fecha_fin = fields.Date('Fecha de finalizacion')
    estado = fields.Selection(
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



