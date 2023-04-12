from django.shortcuts import render

# Create your views here.
def index(request):
    p_title ="Afro-Django"
    username = 'Aloisius'
    gender = 'Male'
    return render(
        request, 
        'index.html',
        {'p_title': p_title, 'username':username, 'gender':gender}
    )

def register(request):
    return render(request, 'register.html')
