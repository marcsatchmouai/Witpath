from odoo import models, fields, api


class Cursos(models.Model):
    _name = 'wp.cursos'
    _description = 'cursos'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    image = fields.Binary(string="Imagen")
    nombre = fields.Char(string="Nombre", required=True, tracking=True)
    titulo = fields.Char(string="Titulo", required=True)
    subtitulo = fields.Char(string="Subtitulo", required=True)
    tema = fields.Char(string="Tema", required=True)
    descripcion = fields.Char(string="Descripcion", required=True)
    fecha_inicio = fields.Date(string='Fecha de inicio')
    fecha_fin = fields.Date(string='Fecha de finalizacion')
    dias_cursado = fields.Char(string="Dias de cursado")
    horario_inicio = fields.Float(string="Horario de inicio")
    horario_finalizacion = fields.Float(string="Horario de finalizacion")
    state = fields.Selection([('activo', 'Activo'), ('inactivo', 'Inactivo')], default='activo')
    precio = fields.Float(string="Precio")

    # relaciones entre tablas
    clase_line_ids = fields.One2many('wp.clases', 'curso_id', 'Clases')
    alumno_line_ids = fields.One2many('wp.alumnos', 'curso_id', 'Alumnos')

    def boton_activar(self):
        print('PRUEBA CLICK ACTIVAR')

    # restricciones sql
    _sql_constraints = [('orden_uniq', 'unique(nombre)', 'El nombre ya existe')]
