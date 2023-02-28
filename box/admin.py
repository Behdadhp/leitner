from django.contrib import admin

from . import models


class LeitnerBoxAdmin(admin.ModelAdmin):
    """class representing of Leitner Box admin page"""

    list_display = ("word", "translate", "pronounce", "counter", "example")
    list_display_links = ("word", "translate", "pronounce", "counter", "example")


admin.site.register(models.LeitnerBox, LeitnerBoxAdmin)
