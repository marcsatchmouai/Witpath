from odoo import models, fields, api


class Alumnos(models.Model):
    _name = 'wp.alumnos'
    _description = 'alumnos'

    legajo = fields.Char(string="Legajo", required=True)
    nombre = fields.Char(string="Nombre", required=True)
    apellido = fields.Char(string="Apellido", required=True)
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento", required=True)
    grado = fields.Char(string="Grado")
    division = fields.Char(string="Division")
    turno = fields.Char(string="Turno")
    institucion = fields.Char(string="Institucion", required=True)
    estado = fields.Selection(
        [('activo', 'Activo'),
         ('inactivo', 'Inactivo')],
        default='activo')

    # relaciones entre tablas
    cliente_id = fields.Many2one(comodel_name='wp.clientes', string='Cliente')
    curso_id = fields.Many2one(comodel_name='wp.cursos', string='Curso')


