from django.utils.translation import ugettext_lazy as _

JET_DEFAULT_THEME = 'default'

JET_SIDE_MENU_COMPACT = True

JET_THEMES = [
    {
        'theme': 'default',  # theme folder name
        'color': '#47bac1',  # color of the theme's button in user menu
        'title': 'Default'  # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]

# Custom dashboard
# JET_INDEX_DASHBOARD = 'dashboards.primary.CustomIndexDashboard'
JET_INDEX_DASHBOARD = 'jet.dashboard.dashboard.DefaultIndexDashboard'

JET_SIDE_MENU_ITEMS = [  # A list of application or custom item dicts
    {'label': _('System'), 'items': [
        {'label': _('Log out'), 'url': '/logout/'}
    ]},
    {'label': _('Members'), 'items': [
        {'name': 'people.member'},
        {'name': 'matirbank.matirbank'},
        {'name': 'matirbank.bankhistory'},
    ]},
    {'label': _('Events'), 'items': [
        {'name': 'events.programtype'},
        {'name': 'events.program'},
    ]},
    {'label': _('Geography'), 'items': [
        {'name': 'geography.branch'},
        {'name': 'helpers.identification'},
        {'name': 'geography.area'},
        {'name': 'geography.district'},
        {'name': 'geography.division'},
    ]},
    {'label': _('Users'), 'items': [
        {'name': 'auth.user'},
        {'name': 'auth.group'},
        {'name': 'people.userprofile'},
    ]}
]


# Django REST-Framework
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'PAGE_SIZE': 10
}