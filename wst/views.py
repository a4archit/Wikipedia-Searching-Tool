from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pyttsx3
import wikipedia
import json

def home(request):
    answer = ""
    if request.method == 'POST':
        query = request.POST.get('queryBar')
        # getting answer of query from wikipedia
        print(f"{query}\nsearching...")
        try:
            answer = wikipedia.summary(query, sentences=2)
        except:
            answer = f"Something went wrong with searching '{query.capitalize()}'"
        print(answer)
    context = {
        "answer": answer
    }
    return render(request, 'home.html', context=context)

@csrf_exempt
def speak(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            text = data.get('text', '')
            engine = pyttsx3.init()
            if text:
                engine.say(text)
            else:
                engine.say("There is no text to speak.")
            engine.runAndWait()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
