from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Setor
from .forms import SetorForm

@login_required
def setores_list(request):
    setores = Setor.objects.all()
    return render(request, 'setores.html', {'setores': setores})

@login_required
def setores_new(request):
    form = SetorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('setores_list')
    return render(request, 'setores_form.html', {'form': form})

@login_required
def setores_update(request, id):
    setor = get_object_or_404(Setor, pk=id)
    form = SetorForm(request.POST or None, instance=setor)

    if form.is_valid():
        form.save()
        return redirect('setores_list')
    return render(request, 'setores_form.html', {'form': form})

@login_required
def setores_delete(request, id):
    setor = get_object_or_404(Setor, pk=id)
    form = SetorForm(request.POST or None, instance=setor)

    if request.method == 'POST':
        setor.delete()
        return redirect('setores_list')

    return render(request, 'setores_delete.html', {'setor': setor})

