from django.contrib import admin

from .models import Plant, Watered, Pot, Status, Photo

admin.site.register(Plant)
admin.site.register(Watered)
admin.site.register(Pot)
admin.site.register(Status)
admin.site.register(Photo)

# Register your models here.
