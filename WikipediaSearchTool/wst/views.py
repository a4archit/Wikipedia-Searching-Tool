from django.shortcuts import render
from typing import Dict
import wikipedia
import time

# Create your views here.

def home(request):
    answer = ""
    if request.method == 'POST':
        query = ""
        query: str = request.POST.get('queryBar')
        # getting answer of query from wikipedia
        print(f"{query}\nsearching...")
        try:
            answer: str = wikipedia.summary(query, sentences=2)
        except:
            answer = f"Something went wrong with searching '{query.capitalize()}'"
        print(answer)
    context: Dict[str,str] = {
        "answer": answer
    }
    return render(request, 'home.html', context=context)

