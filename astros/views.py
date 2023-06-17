from django.shortcuts import render
from .ScoreAPI import get_score

# Create your views here.
def astros(request):

    data_dict = get_score()

    context = {
        'data': data_dict
    }

    return render(request, 'index.html', context)