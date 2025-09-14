from django.shortcuts import render, redirect
from django.contrib  import messages
from .forms import SuenoForm
from .models import Sueno

def sueno_pendiente(request):
    return render(request, 'suenos/pendiente.html')

def registrar_sueno(request):
    if request.method == "POST":
        form = SuenoForm(request.POST)
        if form.is_valid():
            sueno = form.save(commit=False)
            sueno.estado = "PENDING"
            sueno.save()
            messages.success(request, "¡Tu sueño fue registrado y está pendiente de aprobación!")
            return redirect("sueno_pendiente")
        else:
            messages.error(request, "Corrige los errores en el formulario.")
    else:
        form = SuenoForm()

    return render(request, "suenos/registrar.html", {"form": form})


def lista_suenos(request):
    suenos = Sueno.objects.filter(estado="APPROVED").order_by('-fecha')
    return render(request, 'suenos/lista.html', {'suenos': suenos})
