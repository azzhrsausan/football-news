from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406439091',
        'name': 'Sausan Farah Azzahra',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)