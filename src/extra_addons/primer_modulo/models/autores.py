from odoo import models, fields


# Creando un modelo (tabla de la base de datos) a partir de una clase
class Autores(models.Model):
    _name = 'autores'  # nombre de la tabla que se va a generar
    _rec_name = "last_name"
    _description = 'autores'

    name = fields.Char(string="Nombre", required=True)  # nombre del campo
    last_name = fields.Char(string="Apellido")
