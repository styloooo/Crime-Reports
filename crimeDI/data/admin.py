from django.contrib import admin
import crimeDI.data.models as models

# Register your models here.
admin.site.register(models.Incident)
admin.site.register(models.Agency)
admin.site.register(models.Location)
admin.site.register(models.Officer)
admin.site.register(models.Crime)
admin.site.register(models.Race)
admin.site.register(models.Offender)
admin.site.register(models.Victim)
admin.site.register(models.Arrestee)
admin.site.register(models.Arrest)
admin.site.register(models.Property)