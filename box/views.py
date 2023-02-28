from django_tables2 import SingleTableView
from . import tables


class LeitnerBoxList(SingleTableView):
    """view for listing all the words"""

    table_class = tables.LeitnerBoxTable
    table_pagination = {"per_page": 30}
