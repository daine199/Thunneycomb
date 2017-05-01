# THUNDER TOKEN BACKEND

THUNDER_TOKEN = [
    'thunder_token',
]

AUTHENTICATION_BACKENDS = ('thunder_token.ThunderTokenBackend.TokenBackend',
                           'django.contrib.auth.backends.ModelBackend'
                           )


