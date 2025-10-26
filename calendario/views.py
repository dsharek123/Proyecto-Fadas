from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tema
import json
from .forms import TemaForm


@login_required
def vista_calendario(request):
    temas_qs = Tema.objects.all()
    temas_list = []
    for t in temas_qs:
        if not getattr(t, 'fecha', None):
            continue
        temas_list.append({
            'id': t.id,
            'title': f'{t.tema} - {t.actividad}',
            'start': t.fecha.isoformat(),
        })
    return render(request, 'core/calendario.html', {'temas_json': json.dumps(temas_list)})

def nuevo_tema(request):
    if request.method == 'POST':
        tema_text = request.POST.get('tema', '').strip()
        actividad = request.POST.get('actividad', '').strip()
        fecha = request.POST.get('fecha') or None

        if tema_text:
            Tema.objects.create(tema=tema_text, actividad=actividad, fecha=fecha)
            return redirect('vista_calendario')
        return render(request, 'core/nuevo_tema.html', {'error': 'El campo Tema es obligatorio.', 'fecha_inicial': fecha})

    fecha_inicial = request.GET.get('fecha', '')
    return render(request, 'core/nuevo_tema.html', {'fecha_inicial': fecha_inicial})

def editar_tema(request, tema_id):
    tema = get_object_or_404(Tema, pk=tema_id)
    if request.method == 'POST':
        form = TemaForm(request.POST, instance=tema)
        if form.is_valid():
            form.save()
            return redirect('vista_calendario')
    else:
        form = TemaForm(instance=tema)
    return render(request, 'core/editar_tema.html', {'form': form, 'tema': tema})

def eliminar_tema(request, tema_id):
    tema = get_object_or_404(Tema, pk=tema_id)
    if request.method == 'POST':
        tema.delete()
        return redirect('vista_calendario')
    return render(request, 'core/eliminar_tema.html', {'tema': tema})