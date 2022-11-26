from odoo import models, fields, api


class Clientes(models.Model):
    _name = 'wp.clientes'
    _description = 'clientes'

    razon_social = fields.Char(string="Razon Social")
    cuit = fields.Char(string="Cuit")
    email = fields.Char(string="Email")
    direccion = fields.Char(string="Direccion")
    ciudad = fields.Char(string="Ciudad")
    provincia = fields.Char(string="Provincia")
    pais = fields.Char(string="Pais")
    telefono = fields.Char(string="Telefono")
    estado = fields.Selection(
        [('activo', 'Activo'),
         ('inactivo', 'Inactivo')],
        default='activo')

    # relaciones entre tablas
    cotizacion_line_ids = fields.One2many('wp.cotizaciones', 'cliente_id', string='Cotizaciones')
    contacto_line_ids = fields.One2many('wp.contactos', 'cliente_id', string='Contactos')
    alumno_line_ids = fields.One2many('wp.alumnos', 'cliente_id', string='Alumnos')
