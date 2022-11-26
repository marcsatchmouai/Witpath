from odoo import models, fields, api


class Contenido(models.Model):
    _name = 'wp.contenido'
    _description = 'contenido'

    orden = fields.Integer(string="Orden", required=True)
    titulo = fields.Char(string="Titulo", required=True)
    duracion = fields.Datetime(string="Duracion")
    formato = fields.Selection(
        [('pdf', 'Documento'),
         ('pptx', 'Presentacion'),
         ('docx', 'Evaluacion'),
         ('avi', 'Video'),
         ('docx', 'Actividad')],
        default='pdf')
    estado = fields.Selection(
        [('activo', 'Activo'),
         ('inactivo', 'Inactivo')],
        default='activo')
    descripcion = fields.Char(string="Descripcion")

    # relaciones entre tablas
    clase_id = fields.Many2one(comodel_name='wp.clases', string='Clase')
