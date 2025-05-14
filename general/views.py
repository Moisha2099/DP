from django.shortcuts import render, redirect
from django.contrib.auth import logout
from general.models import Order
from general.forms import RegisterForm

def index(request):
    #latest_question_list = Question.objects.order_by("-pub_date")[:5]
    #output = ", ".join([q.question_text for q in latest_question_list])
    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return redirect(index)

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("login")
    else:
        form = RegisterForm()

    return render(response, "register.html", {"form":form})



def profile(request):
    user = request.user
    order_list = Order.objects.filter(user=user).order_by("-date_at")
    context = {'order_list': order_list}
    return render(request,'profile.html', context)

def admin_panel(request):
    order_list = Order.objects.all().order_by("-date_at")
    context = {'order_list': order_list}
    return render(request,'admin_panel.html', context)
