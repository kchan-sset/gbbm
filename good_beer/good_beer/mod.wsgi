import os, sys
sys.path.append('/Users/kenny.chan/Sites/py_fwk/gbbm/good_beer')
os.environ['DJANGO_SETTINGS_MODULE'] = 'good_beer.settings'
os.environ['PYTHON_EGG_CACHE'] = '/Users/kenny.chan/Sites/py_fwk/projects/mysite/eggs'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()