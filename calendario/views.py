from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tema
import json
from .forms import TemaForm
import datetime

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
            'start': t.fecha.isoformat() if t.fecha else None,
        })
    return render(request, 'core/calendario.html', {'temas_json': json.dumps(temas_list)})

def nuevo_tema(request):
    if request.method == 'POST':
        tema_text = request.POST.get('tema', '').strip()
        actividad = request.POST.get('actividad', '').strip()
        fecha_str = request.POST.get('fecha')
        
        fecha = None
        if fecha_str:
            try:
                fecha = datetime.datetime.fromisoformat(fecha_str)
            except ValueError:
                try:
                    fecha = datetime.datetime.strptime(fecha_str, '%Y-%m-%dT%H:%M')
                except ValueError:
                    pass

        if tema_text:
            Tema.objects.create(tema=tema_text, actividad=actividad, fecha=fecha)
            return redirect('vista_calendario')
        return render(request, 'core/nuevo_tema.html', {
            'error': 'El campo Tema es obligatorio.', 
            'fecha_inicial': fecha_str
        })

    fecha_inicial = request.GET.get('fecha', '')
    if fecha_inicial and 'T' not in fecha_inicial:
        fecha_inicial += 'T09:00'
    
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