from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TertuliaForm
from .forms import TertuliaRegistro
from django.contrib import messages


@login_required(login_url="/users/login/")
def inscripcion_tertulia(request):
    if request.method == 'POST':
        form = TertuliaRegistro(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been registered successfully!')
            return redirect('home')

    else:
        form = TertuliaRegistro()
    return render(request, 'inscripciones/tertulias_registro.html', {'form': form})
