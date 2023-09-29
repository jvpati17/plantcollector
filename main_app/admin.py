from django.contrib import admin

from .models import Plant, Watered, Pot, Status

admin.site.register(Plant)
admin.site.register(Watered)
admin.site.register(Pot)
admin.site.register(Status)

# Register your models here.
