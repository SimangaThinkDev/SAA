from django.contrib import admin
from .models import Airport, Flight

# Register your models here.
admin.site.register(Flight)
admin.site.register(Airport)
