import django_tables2 as tables

from . import models


class LeitnerBoxTable(tables.Table):
    word = tables.Column(verbose_name="English Word")
    translate = tables.Column(verbose_name="Persian Word")
    pronounce = tables.Column()
    example = tables.Column()
    counter = tables.Column(verbose_name="Days")

    class Meta:
        template_name = "django_tables2/bootstrap4.html"
        model = models.LeitnerBox

