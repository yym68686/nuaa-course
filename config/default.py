import sys

# Server config
SERVER_NAME = None
DEBUG = False
for arg in sys.argv:
    if arg == '-d':
        DEBUG = True
SECRET_KEY = 'secret-key'


# available languages
LANGUAGES = {
        'en': 'English',
        'zh': '中文'
        }


# SQL config
SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://nuaa:nuaa@localhost/icourse?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask mail
MAIL_SERVER = ''
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = DEBUG
MAIL_USERNAME = "mail_address"
MAIL_PASSWORD = ""
MAIL_DEFAULT_SENDER = 'mail_address'
MAIL_MAX_EMAILS = None
#MAIL_SUPPRESS_SEND =
MAIL_ASCII_ATTACHMENTS = False

# Upload config
UPLOAD_FOLDER = '/home/uploads'
# Alowed extentsions for a filetype
# for example 'image': set(['png', 'jpg', 'jpeg', 'gif'])
ALLOWED_EXTENSIONS = {
        'image':set(['png', 'jpg', 'jpeg', 'gif']),
        'file':set('7z|avi|csv|doc|docx|flv|gif|gz|gzip|jpeg|jpg|mov|mp3|mp4|mpc|mpeg|mpg|ods|odt|pdf|png|ppt|pptx|ps|pxd|rar|rtf|tar|tgz|txt|vsd|wav|wma|wmv|xls|xlsx|xml|zip'.split('|')),
        }
MAX_CONTENT_LENGTH = 100 * 1024 * 1024



IMAGE_PATH = 'uploads/images'


# Debugbar Settings
# Enable the profiler on all requests
DEBUG_TB_PROFILER_ENABLED = True
# Enable the template editor
DEBUG_TB_TEMPLATE_EDITOR_ENABLED =True
DEBUG_TB_INTERCEPT_REDIRECTS = False
