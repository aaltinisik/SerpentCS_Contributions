# See LICENSE file for full copyright and licensing details.


from odoo import api, models, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def check_limit(self):
<<<<<<< HEAD
        """Check if credit limit for partner was exceeded."""
        self.ensure_one()
        partner = self.partner_id
        moveline_obj = self.env['account.move.line']
        movelines = moveline_obj.\
            search([('partner_id', '=', partner.id),
                    ('account_id.user_type_id.type', 'in',
                    ['receivable', 'payable']),
                    ('full_reconcile_id', '=', False)])

        debit, credit = 0.0, 0.0
        today_dt = datetime.strftime(datetime.now().date(), DF)
        for line in movelines:
            if line.date_maturity < today_dt:
                credit += line.debit
                debit += line.credit

        if (credit - debit + self.amount_total) > partner.credit_limit:
            # Consider partners who are under a company.
            if partner.over_credit or (partner.parent_id and partner.parent_id.over_credit):
                partner.write({
                    'credit_limit': credit - debit + self.amount_total})
                return True
            else:
                msg = '%s Can not confirm Sale Order,Total mature due Amount ' \
                      '%s as on %s !\nCheck Partner Accounts or Credit ' \
                      'Limits !' % (partner.over_credit,credit - debit, today_dt)
                raise UserError(_('Credit Over Limits !\n' + msg))
        else:
=======
        self.ensure_one()
        partner = self.partner_id
        user_id = self.env['res.users'].search([
            ('partner_id', '=', partner.id)], limit=1)
        if user_id and not user_id.has_group('base.group_portal') or not \
                user_id:
            moveline_obj = self.env['account.move.line']
            movelines = moveline_obj.search(
                [('partner_id', '=', partner.id),
                 ('account_id.user_type_id.name', 'in',
                  ['Receivable', 'Payable'])]
            )
            confirm_sale_order = self.search([('partner_id', '=', partner.id),
                                              ('state', '=', 'sale')])
            debit, credit = 0.0, 0.0
            amount_total = 0.0
            for status in confirm_sale_order:
                amount_total += status.amount_total
            for line in movelines:
                credit += line.credit
                debit += line.debit
            partner_credit_limit = (partner.credit_limit - debit) + credit
            available_credit_limit = \
                ((partner_credit_limit -
                  (amount_total - debit)) + self.amount_total)

            if (amount_total - debit) > partner_credit_limit:
                if not partner.over_credit:
                    msg = 'Your available credit limit' \
                          ' Amount = %s \nCheck "%s" Accounts or Credit ' \
                          'Limits.' % (available_credit_limit,
                                       self.partner_id.name)
                    raise UserError(_('You can not confirm Sale '
                                      'Order. \n' + msg))
                partner.write(
                    {'credit_limit': credit - debit + self.amount_total})
>>>>>>> upstream/12.0
            return True

    @api.multi
    def action_confirm(self):
        """Extend to check credit limit before confirming sale order."""
        for order in self:
            order.check_limit()
<<<<<<< HEAD
        return super(SaleOrder, self).action_confirm()
=======
        return res

    @api.constrains('amount_total')
    def check_amount(self):
        for order in self:
            order.check_limit()
>>>>>>> upstream/12.0
