from odoo import models, fields, api


class Clientes(models.Model):
    _name = 'wp.clientes'
    _description = 'clientes'

    name = fields.Char(string="Nombre Institución")
    razon_social = fields.Char(string="Razón Social")
    cuit = fields.Char(string="Cuit")
    email = fields.Char(string="Email")
    direccion = fields.Char(string="Dirección")
    ciudad = fields.Char(string="Ciudad")
    provincia = fields.Char(string="Provincia")
    pais = fields.Char(string="País")
    telefono = fields.Char(string="Teléfono")
    state = fields.Selection(
        [('activo', 'Activo'),
         ('inactivo', 'Inactivo')],
        default='activo', string="Estado")

    # relaciones entre tablas
    contacto_line_ids = fields.One2many('wp.contactos', 'cliente_id', string='Contactos')
    alumno_line_ids = fields.One2many('wp.alumnos', 'cliente_id', string='Alumnos')

    def btn_activar(self):
        self.state = 'activo'

    def btn_desactivar(self):
        self.state = 'inactivo'
