from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def profile(request, user = None):
    return render(request, "isBogdan.html", {})

def isBogdan(request):
    text = request.GET.get('text')
    print(text)
    if text == "Bogdan":
    	message = "Написано Богдан"
    else:
    	message = "Не Богдан"
    data = {
        'message': message,
    }
    return JsonResponse(data)
