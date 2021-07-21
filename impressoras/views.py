from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Impressora
from .forms import ImpressoraForm

@login_required
def impressoras_list(request):
    impressoras = Impressora.objects.all()
    return render(request, 'impressoras.html', {'impressoras': impressoras})

@login_required
def impressoras_new(request):
    form = ImpressoraForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('impressoras_list')
    return render(request, 'impressoras_form.html', {'form': form})

@login_required
def impressoras_update(request, id):
    impressora = get_object_or_404(Impressora, pk=id)
    form = ImpressoraForm(request.POST or None, instance=impressora)

    if form.is_valid():
        form.save()
        return redirect('impressoras_list')
    return render(request, 'impressoras_form.html', {'form': form})

@login_required
def impressoras_delete(request, id):
    impressora = get_object_or_404(Impressora, pk=id)
    form = ImpressoraForm(request.POST or None, instance=impressora)

    if request.method == 'POST':
        impressora.delete()
        return redirect('impressoras_list')

    return render(request, 'impressoras_delete.html', {'impressora': impressora})






