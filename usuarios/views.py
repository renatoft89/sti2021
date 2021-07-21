from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Usuario
from .forms import UsuarioForm

@login_required
def usuarios_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

@login_required
def usuarios_new(request):
    form = UsuarioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('usuarios_list')
    return render(request, 'usuarios_form.html', {'form': form})

@login_required
def usuario_update(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    form = UsuarioForm(request.POST or None, instance=usuario)

    if form.is_valid():
        form.save()
        return redirect('usuarios_list')
    return render(request, 'usuarios_form.html', {'form': form})

@login_required
def usuario_delete(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    form = UsuarioForm(request.POST or None, instance=usuario)

    if request.method == 'POST':
        usuario.delete()
        return redirect('usuarios_list')

    return render(request, 'usuarios_delete.html', {'usuario': usuario})