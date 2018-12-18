from django.contrib import admin

# Register your models here.

from blog1 import models
admin.site.register(models.message_info)
