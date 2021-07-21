from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Maquina
from .forms import MaquinaForm


@login_required
def maquinas_list(request):
    maquinas = Maquina.objects.all()
    count_maquinas = Maquina.objects.count()
    return render(request,'equipamentos.html', {'maquinas': maquinas, 'count_maquinas': count_maquinas})

@login_required
def maquina_new(request):
    form = MaquinaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('maquinas_list')
    return render(request, 'maquinas_form.html', {'form': form})

@login_required
def maquina_update(request, id):
    maquina = get_object_or_404(Maquina, pk=id)
    form = MaquinaForm(request.POST or None, instance=maquina)

    if form.is_valid():
        form.save()
        return redirect('maquinas_list')
    return render(request, 'maquinas_form.html', {'form': form})

@login_required
def maquina_delete(request, id):
    maquina = get_object_or_404(Maquina, pk=id)
    form = MaquinaForm(request.POST or None, instance=maquina)

    if request.method == 'POST':
        maquina.delete()
        return redirect('maquinas_list')

    return render(request, 'maquina_delete.html', {'maquina': maquina})


