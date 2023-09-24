from django.contrib import admin
from .models import Institute,Educator,customuser
# Register your models here.
admin.site.register(Institute)
admin.site.register(Educator)
admin.site.register(customuser)