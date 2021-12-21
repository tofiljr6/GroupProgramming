from django.views import generic
from django.shortcuts import redirect

from tables_layout.models import Table


class IndexView(generic.ListView):
    template_name = 'tables_layout/index.html'
    context_object_name = 'tables_list'

    def get_queryset(self):
        return Table.objects.all()


def save(request):
    Table.objects.all().delete()
    c = 1
    while True:
        if request.POST.get(f'x{c}') is not None:
            if request.POST.get(f'x{c}', '') != '':
                t = Table(id=Table.objects.count() + 1,
                          x=request.POST[f'x{c}'],
                          y=request.POST[f'y{c}'])
                t.save()

        else:
            break
        c += 1
    return redirect("tables_layout:index")
