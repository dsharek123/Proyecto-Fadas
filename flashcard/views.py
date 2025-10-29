from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Flashcard

@login_required
def flashcard_view(request):
    # Debug
    print("Usuario:", request.user)
    print("Método:", request.method)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        pregunta = request.POST.get('pregunta')
        respuesta = request.POST.get('respuesta')
        card_id = request.POST.get('card_id')
        
        print(f"Action: {action}, Pregunta: {pregunta}, Respuesta: {respuesta}, Card ID: {card_id}")
        
        if action == 'create' and pregunta and respuesta:
            flashcard = Flashcard.objects.create(
                usuario=request.user,
                pregunta=pregunta,
                respuesta=respuesta
            )
            print(f"Flashcard CREADA - ID: {flashcard.id}")
        
        elif action == 'edit' and pregunta and respuesta and card_id:
            flashcard = get_object_or_404(Flashcard, id=card_id, usuario=request.user)
            flashcard.pregunta = pregunta
            flashcard.respuesta = respuesta
            flashcard.save()
            print(f"Flashcard EDITADA - ID: {flashcard.id}")
        
        elif action == 'delete' and card_id:
            flashcard = get_object_or_404(Flashcard, id=card_id, usuario=request.user)
            flashcard.delete()
            print(f"Flashcard ELIMINADA - ID: {card_id}")
        
        return redirect('flashcard:flashcard_view')
    
    flashcards = Flashcard.objects.filter(usuario=request.user).order_by('-fecha_creacion')
    print(f"Total flashcards en BD: {flashcards.count()}")
    
    return render(request, 'flashcard.html', {'flashcards': flashcards})