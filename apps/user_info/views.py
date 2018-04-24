from django.shortcuts import render, redirect
from apps.user_info.models import User

# Create your views here.
def index(request):
    return render(request, 'user_info/index.html')

def login(request):
    if request.method == 'POST':
        html_email = request.POST['html_email']
        html_password = request.POST['html_password']
        try:
            user = User.objects.get(email = html_email)
            if user.password == html_password:
                request.session['user_id'] = user.id
                request.session['email'] = user.email
                return redirect('user_info:index')
            else:
                messages.error(request, 'Invalid Login')
                return redirect('user_info:login')

        except:
            messages.error(request, 'No such user')
            return redirect('user_info:login')

    return render(request, 'user_info/login.html')

def logout(request):
    request.session.clear()
    return redirect('user_info:index')

def register(request):
    if 'user_id' in request.session:
        return redirect('user_info:index')

    if request.method == 'POST':
        if len(request.POST['html_password']) > 0 and request.POST['html_password']==request.POST['html_confirm']:
            try:
                user = User.objects.create(email = request.POST['html_email'], password = request.POST['html_password'])
                request.session['user_id'] = user.id
                request.session['email'] = user.email
                
            except:
                messages.error(request, 'This is wrong')
                return redirect('user_info:register')

        return redirect('user_info:index')

    return render(request, 'user_info/register.html')