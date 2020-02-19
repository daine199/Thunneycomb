# SSO Settings

SSO_APPS = [
    'admin_sso'
    ]


AUTHENTICATION_BACKENDS = (
    'admin_sso.auth.DjangoSSOAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
)


DJANGO_ADMIN_SSO_OAUTH_CLIENT_ID = 'test-client-id'
DJANGO_ADMIN_SSO_OAUTH_CLIENT_SECRET = 'test-client-secret'

