from models import Participation
from django.contrib import admin

class OteAdmin(admin.ModelAdmin):
    list_display = ('id_number',)

admin.site.register(Participation, OteAdmin)
