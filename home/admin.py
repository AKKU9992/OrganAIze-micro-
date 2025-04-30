from django.contrib import admin
from home.models import Contact
from home.models import todoweek
from home.models import todomonth
from home.models import todo
# Register your models here.
admin.site.register(Contact)
admin.site.register(todoweek)
admin.site.register(todomonth)
admin.site.register(todo)