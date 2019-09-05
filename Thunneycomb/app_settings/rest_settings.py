# REST SETTINGS
LOGIN_ENABLE = True

REST_APPS = ['rest_framework',
             'rest_framework.authtoken'
             ]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication'
    ),
    # 权限直接在模块中设置
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.DjangoModelPermissions',
    #     'rest_framework.permissions.IsAuthenticated',
    #     'rest_framework.permissions.AllowAny'
    # ],
    # 'LANGUAGE_CODE': 'zh_cn'
}
