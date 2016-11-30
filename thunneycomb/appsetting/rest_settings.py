# REST SETTINGS
LOGIN_ENABLE = False

REST_APPS = ['rest_framework',
             'rest_framework.authtoken'
             ]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.DjangoModelPermissions',),
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication'
    ),
    'LANGUAGE_CODE': 'zh_cn'
}
