exec(open("/home//venv/bin/activate_this.py").read())

import site
import os
import time
import traceback
import signal
import sys

#comments
sys.path.append('/home/www/djshop/saleor')
sys.path.append('/home/www/djshop')

#add the site-packages of the chosen virtualenv to work with
site.addsitedir("/home/www/djenv/lib/python3.5/site-packages")

project = "/home/www/djshop"
workspace = os.path.dirname(project)
sys.path.append(workspace)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "saleor.settings")
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

