# See LICENSE file for full copyright and licensing details.

<<<<<<< HEAD
from openerp import models, fields, api
=======
from odoo import models, fields, api
>>>>>>> upstream/12.0
import datetime
from dateutil.relativedelta import relativedelta


class SelectTraining(models.TransientModel):

    _name = 'select.training'

<<<<<<< HEAD
    is_triaing_needed = fields.Boolean(string="Is Training needed?",
                                       required=True)

    @api.multi
    def action_done(self):
        act_id = self._context.get('active_id')
        applicant = self.env['hr.applicant'].search([('id', '=', act_id)])
=======
    is_triaing_needed = fields.Boolean(
        string="Is Training needed?", required=True)

    @api.multi
    def action_done(self):
        applicant = self.env['hr.applicant'].search(
            [('id', '=', self._context.get('active_id'))])
>>>>>>> upstream/12.0
        employee_dict = applicant.create_employee_from_applicant()
        course_obj = self.env['training.courses']
        class_obj = self.env['training.class']
        attendee_obj = self.env['list.of.attendees']
        for rec in self:
            if rec.is_triaing_needed:
<<<<<<< HEAD
                course = course_obj.search([('job_id', '=',
                                             applicant.job_id.id)])
                if not course:
                    t_nam = 'Training Course for ' + str(applicant.job_id.name)
                    course = course_obj.create({'name': t_nam,
                                                'job_id': applicant.job_id.id,
                                                'duration': 1,
                                                'duration_type': 'month'})
                training_class = class_obj.search([('course_id', '=',
                                                    course.id)])
                if not training_class:
                    dt_now = datetime.date.today()
                    tri_class_val = {
                        'course_id': course.id,
                        'training_attendees': 1,
                        'training_start_date': dt_now +
                        datetime.timedelta(days=1),
                        'training_end_date': dt_now +
                        datetime.timedelta(days=1) + relativedelta(months=1,
                                                                   days=-1),
                        'state': 'approved'}
                    training_class = class_obj.create(tri_class_val)
                st_dt = training_class.training_start_date
                attendee_obj.create({
                    'class_id': training_class.id,
                    'employee_id': employee_dict.get('res_id', False),
                    'training_start_date': st_dt,
                    'training_end_date': training_class.training_end_date,
                    'date_of_arrival': st_dt,
=======
                course = course_obj.search(
                    [('job_id', '=', applicant.job_id.id)])
                if not course:
                    course = course_obj.create({
                        'name': 'Training Course for ' + str(
                            applicant.job_id.name),
                        'job_id': applicant.job_id.id,
                        'duration': 1,
                        'duration_type': 'month'})
                training_class = class_obj.search(
                    [('course_id', '=', course.id)])
                if not training_class:
                    training_class = class_obj.create({
                        'course_id': course.id,
                        'training_attendees': 1,
                        'training_start_date': datetime.date.today() +
                        datetime.timedelta(days=1),
                        'training_end_date': datetime.date.today() +
                        datetime.timedelta(days=1) + relativedelta(
                            months=1, days=-1),
                        'state': 'approved'})
                attendee_obj.create({
                    'class_id': training_class.id,
                    'employee_id': employee_dict.get('res_id', False),
                    'training_start_date': training_class.training_start_date,
                    'training_end_date': training_class.training_end_date,
                    'date_of_arrival': training_class.training_start_date,
>>>>>>> upstream/12.0
                    'state': 'in_training'})
        return True
