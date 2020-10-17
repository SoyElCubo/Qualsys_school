{
    'name' : "La escuelita",
    'description' : "Capacitacion Odoo",
    'author' : "Cesar El Cubo Bonilla",
    'depends' : [
    'base'
    ],
    'data' : ['views/qualsys_school_views.xml',
              'views/qualsys_courses_views.xml',
              'views/qualsys_attendees_views.xml',
              'views/qualsys_teachers_views.xml',
              'wizard/course_assign_wizard_views.xml',
              'wizard/school_assign_wizard_views.xml',
              'reports/qualsys_school_report.xml',
              'reports/qualsys_school_template.xml',
              'security/ir.model.access.csv'
              ]
}