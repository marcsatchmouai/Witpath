from odoo import models, fields, api


# Creando un modelo (tabla de la base de datos) a partir de una clase
class Libros(models.Model):
    _name = 'libros'  # nombre de la tabla que se va a generar
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'libros'

    supervisor_id = fields.Many2one(comodel_name='hr.employee', string="Supervisor")
    name = fields.Char(string="Nombre del libro", required=True, tracking=True)  # nombre del campo
    editorial = fields.Char(string="Editorial", required=True)
    isbn = fields.Char(string="ISBN", required=True)
    autor_id = fields.Many2one(comodel_name="autores", string="Autor", required=True)
    lastname_autor = fields.Char(related="autor_id.last_name", string="Apellido del Autor")
    image = fields.Binary(string="Imagen")
    categoria_id = fields.Many2one(comodel_name="categoria.libro", required=True)
    state = fields.Selection([('draft', 'Borrador'), ('published', 'Publicado')], default='draft')
    description = fields.Char(string="Descripcion", compute="_compute_description")

    @api.depends('name', 'isbn')
    def _compute_description(self):
        self.description = self.name + ' | ' + self.isbn + ' | ' + self.autor_id.name + ' | ' + self.categoria_id.name

    def boton_publicar(self):
        self.state = 'published'
        print('PRUEBA PUBLICAR')

    def boton_borrador(self):
        self.state = 'draft'
        # print('PRUEBA CLICK BOTON')

    _sql_constraints = [("name_uniq", "unique (name)", "El nombre del libro ya existe")]
    # nombre del sql constraint
    # unique () los valores que no queremos que se dupliquen
    # Mensaje de error

class CategoriaLibro(models.Model):
    _name = 'categoria.libro'
    _description = 'categoria libros'

    name = fields.Char(string="Nombre de la categoria")