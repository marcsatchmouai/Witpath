from odoo import models, fields, api
from datetime import datetime, timedelta


class Cotizaciones(models.Model):
    _name = 'wp.cotizaciones'
    _description = 'cotizaciones'

    id = fields.Integer(string='Nro.', readonly=True)
    fecha_emision = fields.Date('Fecha emision', default=datetime.today(), readonly=True)
    fecha_aceptacion = fields.Date('Fecha de aceptacion')
    fecha_vigencia = fields.Date('Fecha de vigencia', readonly=True)
    state = fields.Selection(
        [('pendiente', 'Pendiente'),
         ('aceptada', 'Aceptada'),
         ('vencida', 'Vencida'),
         ('cancelada', 'Cancelada')],
        default='pendiente')
    cantidad_cursos = fields.Integer('Cantidad Cursos')
    cantidad_alumnos = fields.Integer('Cantidad Alumnos')
    importe = fields.Float('Importe')
    iva = fields.Float('IVA (21%)')
    descuento = fields.Float('Descuento')
    cuit = fields.Char(string='Cuit', related='cliente.cuit', readonly=True)
    direccion = fields.Char(string='Direccion', related='cliente.direccion', readonly=True)
    telefono = fields.Char(string='Telefono', related='cliente.telefono', readonly=True)
    email = fields.Char(string='Email', related='cliente.email', readonly=True)

    # relaciones entre tablas
    cliente = fields.Many2one(comodel_name='wp.clientes', string='Cliente')
    cursos = fields.Many2many(comodel_name='wp.cursos', string='Cursos')
    cotizacion_detalle_line_ids = fields.One2many('wp.cotizaciones_detalle', 'cotizacion_id', 'Detalle')

    # Funciones
    @api.onchange("fecha_aceptacion")
    def _onchange_fecha_aceptacion(self):
        if self.fecha_emision and self.fecha_aceptacion:
            vencimiento = self.fecha_emision + timedelta(days=10)
            if self.fecha_aceptacion <= vencimiento:
                self.state = "aceptada"
            else:
                self.state = "vencida"

    @api.onchange("fecha_emision")
    def _onchange_fecha_vigencia(self):
        if self.fecha_emision:
            self.fecha_vigencia = self.fecha_emision + timedelta(days=10)

    def btn_cancelar(self):
        self.state = 'cancelada'
