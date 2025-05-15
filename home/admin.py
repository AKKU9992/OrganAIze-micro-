from django.contrib import admin
from home.models import Contact
from home.models import todoweek
from home.models import todomonth
from home.models import todo
from home.models import PriorityTask
# Register your models here.
admin.site.register(PriorityTask)
admin.site.register(Contact)
admin.site.register(todoweek)
admin.site.register(todomonth)
admin.site.register(todo)