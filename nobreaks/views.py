from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Nobreak
from .forms import NobreakForm

@login_required
def nobreaks_list(request):
    nobreak = Nobreak.objects.all()
    return render(request,'nobreaks.html', {'nobreaks': nobreak})

@login_required
def nobreaks_new(request):
    form = NobreakForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('nobreaks_list')
    return render(request, 'nobreaks_form.html', {'form': form})

@login_required
def nobreaks_update(request, id):
    nobreak = get_object_or_404(Nobreak, pk=id)
    form = NobreakForm(request.POST or None, instance=nobreak)

    if form.is_valid():
        form.save()
        return redirect('nobreaks_list')
    return render(request, 'nobreaks_form.html', {'form': form})

@login_required
def nobreaks_delete(request, id):
    nobreak = get_object_or_404(Nobreak, pk=id)
    form = NobreakForm(request.POST or None, instance=nobreak)

    if request.method == 'POST':
        nobreak.delete()
        return redirect('nobreaks_list')

    return render(request, 'nobreaks_delete.html', {'nobreak': nobreak})
