from odoo import models, fields, api
from datetime import datetime, timedelta


class Cotizaciones(models.Model):
    _name = 'wp.cotizaciones'
    _description = 'cotizaciones'

    # nro_cotizacion = fields.Char(string="Nro. Cotizacion", readonly=True, required=True, copy=False, default='New')
    id = fields.Integer(string='Nro. Cotizacion', readonly=True)
    fecha_emision = fields.Date('Fecha emision', default=datetime.today(), readonly=True)
    fecha_aceptacion = fields.Date('Fecha de aceptacion')
    fecha_vigencia = fields.Date('Fecha de vigencia')
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
    total = fields.Float('Total')
    descuento = fields.Float('Descuento (%)')
    cuit = fields.Char(string='Cuit', related='cliente.cuit', readonly=True)
    direccion = fields.Char(string='Direccion', related='cliente.direccion', readonly=True)
    telefono = fields.Char(string='Telefono', related='cliente.telefono', readonly=True)
    email = fields.Char(string='Email', related='cliente.email', readonly=True)

    # relaciones entre tablas
    cliente = fields.Many2one(comodel_name='wp.clientes', string='Cliente')
    cursos_id = fields.Many2many(comodel_name='wp.cursos', string='Cursos')
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

    def _calculos(self):
        self.iva = 0.00
        self.total = 0.00
        importeConDesc = (self.importe - self.descuento * self.importe / 100)
        self.iva = importeConDesc * 21 / 100
        self.total = importeConDesc + self.iva

    @api.onchange("cotizacion_detalle_line_ids")
    def _onchange_cotizacion_detalle_line_ids(self):
        self.importe = 0.00
        self.cantidad_cursos = 0
        self.cantidad_alumnos = 0
        for item in self.cotizacion_detalle_line_ids:
            self.importe = self.importe + item.subtotal
            self.cantidad_cursos += 1
            self.cantidad_alumnos = self.cantidad_alumnos + item.cantidad
        self._calculos()

    @api.onchange("descuento")
    def _onchange_descuento(self):
        if self.descuento > 100.00:
            self.descuento = 0.00
            return {
                'warning': {
                    'title': '¡Advertencia!',
                    'message': 'El porcentaje no puede ser mayor al 100%'}
            }
        if self.descuento < 0.00:
            self.descuento = 0.00
            return {
                'warning': {
                    'title': '¡Advertencia!',
                    'message': 'El porcentaje no puede ser menor que 0.00%'}
            }
        if self.importe and self.descuento:
            self._calculos()

    def btn_cancelar(self):
        self.state = 'cancelada'

    # @api.model
    # def create(self, vals):
    #    obj = super(Cotizaciones, self).create(vals)
    #    if obj.nro_cotizacion == 'New':
    #        number = self.env['ir.sequence'].next_by_code('seq.cotizaciones') or 'New'
    #        obj.write({'nro_cotizacion': number})
    #    return obj
