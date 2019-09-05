# WIKI Settings
WIKI_APPS = [
    'django.contrib.sites.apps.SitesConfig',
    'django.contrib.humanize.apps.HumanizeConfig',
    'django_nyt.apps.DjangoNytConfig',
    'mptt',
    'sekizai',
    'sorl.thumbnail',
    'wiki.apps.WikiConfig',
    'wiki.plugins.attachments.apps.AttachmentsConfig',
    'wiki.plugins.notifications.apps.NotificationsConfig',
    'wiki.plugins.images.apps.ImagesConfig',
    'wiki.plugins.macros.apps.MacrosConfig',
    'wiki.plugins.links.apps.LinksConfig',
    'wiki.plugins.help.apps.HelpConfig',
    'wiki.plugins.globalhistory.apps.GlobalHistoryConfig'
]

SITE_ID = 1

WIKI_ACCOUNT_HANDLING = True
WIKI_ACCOUNT_SIGNUP_ALLOWED = True

WIKI_ATTACHMENTS_EXTENSIONS = ['pdf', 'doc', 'pptx', 'odt', 'docx', 'txt']
