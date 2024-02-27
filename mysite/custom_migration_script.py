import os
from django.conf import settings
from djongo.sql2mongo import SQLDecodeError
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application
from djongo import djongo_admin

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')


application = get_wsgi_application()

call_command('makemigrations', interactive=False)
call_command('migrate', interactive=False)

try:
    call_command('sqlclear', 'your_app_name', interactive=False)
except SQLDecodeError:
    pass

call_command('mongo2sql', 'your_app_name', 'mongodb://localhost:27017/your_mongo_db_name')

call_command('migrate', interactive=False)

call_command('mongo2sql', 'your_app_name', '--clean', interactive=False)