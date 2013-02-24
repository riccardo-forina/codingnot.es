HOSTNAME = socket.gethostname()
DEBUG = False
if '.local' in HOSTNAME:
    DEBUG = True

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
# LESS_BIN = os.path.join(SCRIPT_ROOT, '..', 'node_modules', 'less', 'bin', 'lessc')
LESS_LINE_NUMBERS = 'mediaquery'

