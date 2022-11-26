from odoo import models, fields


class Clases(models.Model):
    _name = 'wp.clases'
    _description = 'clases'

    titulo = fields.Char(string="Titulo", required=True)
    orden = fields.Integer(string="Orden", required=True)
    descripcion = fields.Char(string="Descripcion", required=True)
    duracion = fields.Datetime("Duracion")
    estado = fields.Selection(
        [('active', 'Activo'),
         ('desactive', 'Inactivo')],
        default='active')

    # relaciones entre tablas
    curso_id = fields.Many2one(comodel_name='wp.cursos', string='Curso')
    contenido_line_ids = fields.One2many('wp.contenido', 'clase_id', string='Contenido')



