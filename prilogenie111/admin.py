from django.contrib import admin
from .models import MyModelTest

admin.site.register(MyModelTest)

#
#   gunicorn max_test_db.wsgi
#