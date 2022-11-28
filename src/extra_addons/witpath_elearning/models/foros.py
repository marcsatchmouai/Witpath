from odoo import models, fields, api


class Foros(models.Model):
    _name = 'wp.foros'
    _description = 'foros'

    orden = fields.Integer(string="Orden", required=True)
    titulo = fields.Char(string="Titulo", required=True)
    estado = fields.Selection(
        [('activo', 'Activo'),
         ('inactivo', 'Inactivo')],
        default='activo')
    descripcion = fields.Char(string="Descripcion", required=True)
    cantidad_mensajes = fields.Integer(string='Cantidad de Mensajes')

    # relaciones entre tablas
    clase = fields.Many2one(comodel_name='wp.clases', string='Clase')
    curso_id = fields.Many2one(comodel_name='wp.cursos', string='Curso')

    # restricciones sql
    _sql_constraints = [('orden_uniq', 'unique(orden)', 'El numero de orden ya existe')]
