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
              'wizard/course_assign_wizard_views.xml',
              'wizard/school_assign_wizard_views.xml',
              'security/ir.model.access.csv'
              ]
}