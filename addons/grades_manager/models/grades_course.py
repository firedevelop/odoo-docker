from odoo import models, fields

class GradesCourse(models.Model):
    _name = 'grades.course'
    _description = 'Grades Course'
    # _order = 'name' # _order = 'email' # Will Sort order by ... when page is load.
    # _rec_name = '' # this name used in some places like the path, info, etc.. is not necesary declarate by default will be the name

    name = fields.Char(string='Name') # by default the first variable will be Sort order by...
    student_qty = fields.Integer(string='Student quantity')
    grades_average = fields.Float(string='Grades average')
    description = fields.Text(string='Description')
    is_active = fields.Boolean(string='Is active')
    course_start = fields.Date(string='Course start')
    course_end = fields.Date(string='Course end')
    last_evaluation_date = fields.Datetime(string='Last evaluation date')
    course_image = fields.Binary(string='Course image')
    course_shift = fields.Selection([
        ('day', 'Day'),
        ('night', 'Night')
    ], string='Course shift')
