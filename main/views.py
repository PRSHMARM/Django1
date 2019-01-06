#from django.shortcuts import render

#Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


from main.models import User, Credit, Debit, Transfer
from main import forms
from django.forms import forms
from . import forms
from main.forms import credit_form, transfer_form


def homePageView(request):
    return HttpResponseRedirect('/login/')
def signup(request):
    print("method is", request.method)
    if request.method == "GET":
        form = forms.UserForm()
    else:
        form = forms.UserForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return HttpResponse("Form Is Submitted Succesfully")

    context = {
        'user_form': form
    }
    return render(request,'signup.html',context)


def login(request):
    if request.method == "GET":
        formlogin = forms.userloginform()
        context = {
            'user_loginform': formlogin
        }
        return render(request, 'login.html', context)
    else:
        formlogin = forms.userloginform(request.POST)
        email = formlogin.data["email"]
        password = formlogin.data["password"]
        print(email,password)
        user = User.objects.filter(email=email,password=password)
        print(user)
        if len(user)>0:
            return HttpResponseRedirect('/dashboard/?user_id='+str(user[0].id))
        else:
            context ={
        'user_loginform': formlogin
    }
    return render(request, 'login.html', context)


def dashboard(request):
    user_id = request.GET.get("user_id")
    user = User.objects.filter(id=user_id)
    context = {
        "user": user[0],
             }
    return render(request, 'dashboard.html',context)

def logout(request):
    return HttpResponse("you have been successfully logged out")
    return HttpResponseRedirect('/login/')


def credit(request):
    if request.method == 'GET':
        credit_form = forms.credit_form()
        context ={
            'user_credit_form': credit_form,
            #'user_id':user_id
        }
        return render(request, 'credit.html', context)
    else:
        credit_form = forms.credit_form(request.POST)
        if credit_form.is_valid():
            obj =credit_form.save()
            user_id = request.GET.get("user_id")
            print(user_id)
            credit =credit_form.data["credit"]

            user = User.objects.get(id=user_id)
            balance = user.balance
            user.balance=int(balance)+int(credit)
            obj=user.save()
            return HttpResponseRedirect('/dashboard/?user_id=' + str(user_id))
        context ={
            'user_credit_form': credit_form
    }
    return render(request, 'credit.html', context)


def debit(request):
    if request.method == 'GET':
        debit_form = forms.debit_form()
        context ={
            'user_debit_form': debit_form,
            #'user_id':user_id
        }
        return render(request, 'debit.html', context)
    else:
        debit_form = forms.debit_form(request.POST)
        if debit_form.is_valid():
            obj =debit_form.save()
            user_id = request.GET.get("user_id")
            print(user_id)
            debit = debit_form.data["debit"]

            user = User.objects.get(id=user_id)
            balance = user.balance
            user.balance=int(balance)-int(debit)
            obj=user.save()
            return HttpResponseRedirect('/dashboard/?user_id=' + str(user_id))
        context ={
            'user_debit_form': debit_form
    }
    return render(request, 'debit.html', context)




def transfer(request):
    global receiver,creditor
    print("method is", request.method)
    if request.method == "GET":
        transfer_form = forms.transfer_form()
        context ={
            'user_transfer_form': transfer_form,
        }
        return render(request,'transfer.html',context)
    else:
        transfer_form = forms.transfer_form(request.POST)
        if transfer_form.is_valid():
            user_id = request.GET.get("user_id")
            print(user_id)
            #receiver_id = request.GET.get("receiver_id")
            #print(receiver_id)
            amount = transfer_form.data["amount"]
            receiver = transfer_form.data["receiver"]
            sender = User.objects.get(id=user_id)
            creditor = User.objects.get(id=receiver)

            sender_balance = sender.balance
            creditor_balance = creditor.balance
            sender.balance = int(sender_balance) - int(amount)
            creditor.balance = int(creditor_balance)+int(amount)
            obj = transfer_form.save()
            obj = sender.save()
            obj= creditor.save()
            return HttpResponseRedirect('/dashboard/?user_id=' + str(user_id))

    context = {
        'user_transfer_form': transfer_form,
    }
    return render(request,'transfer.html',context)


def Account_statement(request,):
    user_id = request.GET.get("user_id")
    user = User.objects.filter(id=user_id)
    credit = Credit.objects.filter(user=user_id)
    debit = Debit.objects.filter(user=user_id)
    #user2 =User.objects.filter(id=receiver)
    transfer = Transfer.objects.filter(user=user_id)
    received = Transfer.objects.filter(receiver=user_id)



    context={"user": user[0],
             #"user2":user2[0],
             "transfer":transfer,
             "receivings":received,
             "credit": credit,
             "debit" : debit,
             }
    return render(request, 'Account_statement.html', context)
