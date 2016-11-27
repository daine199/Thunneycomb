# CKEditor Settings

CKEDITOR_APPS = [
    'summerhere',
    'ckeditor',
    'ckeditor_uploader',
]

CKEDITOR_UPLOAD_PATH = "article_images/"
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_BROWSE_SHOW_DIRS = True

"""
    django-ckeditor uses jQuery in ckeditor-init.js file.
    You must set ``CKEDITOR_JQUERY_URL`` to a jQuery URL that will be used to load the library.
    If you have jQuery loaded from a different source just don't set [CKEDITOR_JQUERY_URL] and then,
    django-ckeditor will not try to load its own jQuery.
    If you find that CKEditor widgets don't appear in your Django admin site then
    check that this variable is set correctly.
"""
# CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_JQUERY_URL = 'summerhere/js/2.1.1/jquery.min.js'
# CKEDITOR_JQUERY_URL = 'summerhere/js/3.1.1/jquery.min.js'

"""
    Don't forget to ./manage.py collectstatic to sync the ckeditor static file to static dir.
"""

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 750,
    },
    'awesome_ckeditor': {
        'toolbar': 'Basic',
        'height': 300,
        'width': 750,
    },
}
