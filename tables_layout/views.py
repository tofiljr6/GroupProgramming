from django.views import generic
from django.shortcuts import redirect

from tables_layout.models import Table


class IndexView(generic.ListView):
    template_name = 'tables_layout/index.html'
    context_object_name = 'tables_list'

    def get_queryset(self):
        return Table.objects.all()


def add(request):
    Table(id=Table.objects.count()+1).save()
    return redirect("index")


def remove(request):
    Table.objects.latest('id').delete()
    return redirect("index")
