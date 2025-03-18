from django.contrib import admin
from home.models import Contact,Game


class GameAdmin(admin.ModelAdmin):
    list_display=('name','game_type')

# Register your models here.
admin.site.register(Contact)
admin.site.register(Game,GameAdmin)