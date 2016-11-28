# PLATYCODON BLOG SYSTEM SETTINGS

PLATYCODON_APPS = [
    'ckeditor',
    'ckeditor_uploader',
    'platycodon'
]

CKEDITOR_JQUERY_URL = './platycodon/js/jquery/3.1.1/jquery.min.js'

"""
UPLOAD SETTINGS
"""
#  This setting specifies an relative path to your CKEditor media upload directory.
CKEDITOR_UPLOAD_PATH = "platycodon/"

# True: turn off img upload, False: turn on img upload.
CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False

# This restricts access to uploaded images to the uploading user
# (e.g. each user only sees and uploads their own images).
CKEDITOR_RESTRICT_BY_USER = True

# to show directories on the "Browse Server" page.
CKEDITOR_BROWSE_SHOW_DIRS = True

# Toolbar settings
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 300,
    },
}

