from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError

class ThuNhap(models.Model):
    _name = 'thu_nhap'
    _description = 'Quản lý thu nhập'

    id_thu_nhap = fields.Char("Mã ", required=True)
    nguon = fields.Char("Nguồn thu nhập", required=True)
    so_tien = fields.Float("Số tiền", required=True)
    ngay_nhan = fields.Date("Ngày nhận", required=True, default=date.today)
    description = fields.Text("Mô tả")
    id_nhan_vat = fields.Many2one("nhan_vat", string="Nhân vật")

    @api.constrains('so_tien')
    def _check_amount(self):
        for record in self:
            if record.so_tien <= 0:
                raise ValidationError("Số tiền phải lớn hơn 0.")

    def total_income(self):
        total = sum(record.so_tien for record in self.search([]))
        return total