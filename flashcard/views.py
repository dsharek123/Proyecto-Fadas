from django.shortcuts import render

def flashcard_view(request):
    return render(request, 'flashcard.html')
