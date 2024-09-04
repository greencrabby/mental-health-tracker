from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306275001',
        'name': 'Joshua Elisha Shalom Soedarmintarto',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)