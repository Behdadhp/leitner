from django_tables2 import SingleTableView
from . import tables, models


class LeitnerBoxList(SingleTableView):
    """view for listing all the words"""

    table_class = tables.LeitnerBoxTable
    table_pagination = {"per_page": 30}
    queryset = models.LeitnerBox.objects.all()
    template_name = "leitner_box/leitner_box.html"
