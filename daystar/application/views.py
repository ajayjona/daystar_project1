from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import *


# Create your views here.
#home view, sitter view, baby view, payment view, procurement view
def index(request):
    baby_list = Baby.objects.all()
    count_babies =len(baby_list)
    sitters_List = Sitter.objects.all()
    count_sitters = len(sitters_List)
    payments = Pay.objects.all()
    count_payments = Pay.objects.count()
    recent_babies = Baby.objects.all()[:3]
    recent_sitters = Sitter.objects.all()[:3]
    item = Item.objects.all()
    count_items = Item.objects.count()
    context = {
        'baby_list': baby_list,
        'payments': payments,
        'count_payments': count_payments,
        'count_sitters': count_sitters,
        'Sitters_List': sitters_List,
        'count_babies': count_babies,
        'recent_babies': recent_babies,
        'recent_sitters':recent_sitters,
        'item': item,
        'count_items': count_items,
    }
    template = loader.get_template('application/index.html')
    return HttpResponse(template.render(context))

def addbaby(request):
    message = None
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        gender = request.POST['gender']
        age = request.POST['age']
        parent_name = request.POST['parent_name']
        timein  = request.POST['timein']
        fees = request.POST['fees']
        broughtby = request.POST['broughtby']
        babynumber  = request.POST['babynumber']
        message_left = request.POST['message_left']
        stay_duration = request.POST['stay_duration']
        # Address = request.POST['address'] 
        baby = Baby(fname=fname, lname=lname, gender=gender, age=age, parent_name=parent_name, timein=timein, fees=fees, broughtby=broughtby, babynumber=babynumber, message_left=message_left, stay_duration=stay_duration)
        baby.save()
        message = 'Baby added successfully'
    context = {
        'message':message
    }
    template = loader.get_template('application/add_baby.html')
    return HttpResponse(template.render(context))

def addsitter(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        gender = request.POST['gender']
        age = request.POST['age']
        address = request.POST['location']
        contact = request.POST['contact'] 
        sitter = Sitter(fname=fname, lname=lname, gender=gender, age=age, location=address, contact=contact)
        sitter.save()
        # messages = 'Sitter added successfully'
    # contxt = {
    #     'messages': messages tis is the siiter message that refused to wrk 
    # }
    template = loader.get_template('application/add_sitter.html')
    return HttpResponse(template.render())


def viewbaby(request, id):
    baby_obj = Baby.objects.get(id = id)
    all_pays = Pay.objects.filter(payee=id)
    stayduration = Categorystay.objects.filter(id=id)
    context = {
       'baby': baby_obj,
        'all_pays': all_pays,
        'stayduration': stayduration,
    }
    template = loader.get_template('application/view_baby.html')
    return HttpResponse(template.render(context))


def viewsitter(request,id):
    sitters = Sitter.objects.get(id=id)
    context = {
       'sitters': sitters
    }
    template = loader.get_template('application/view_sitter.html')
    return HttpResponse(template.render(context))
    
    
    

def baby(request):
    babies = Baby.objects.all()
    context = {
        'babies': babies
    }
    template = loader.get_template('application/baby_list.html')
    return HttpResponse(template.render(context))

def sitter(request):
    sitters = Sitter.objects.all()
    context = {
       'sitters': sitters
    }
    template = loader.get_template('application/sitter_list.html')
    return HttpResponse(template.render(context))

def payment(request, id):
    if request.method == 'POST':
        amount = request.POST['amount']
        date = request.POST['date']
        baby = Baby.objects.get(id = id)
        pay = Pay(baby=baby, amount= amount, date = date )
        pay.save()
        return redirect('payment_success', id=id)
    else:
        babies = Baby.objects.all()
        pays = Pay.objects.all()
        return render(request, 'application/payments.html', {'babies': babies, 'pays':pays})
    
def payment_success(request, id):
    baby = Baby.objects.get(id=id)
    return render(request, 'application/payment_success.html', {'baby':baby})

def inventory(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    template = loader.get_template('application/inventory.html')
    return HttpResponse(template.render(context))

def additem(request):
    if request.method == 'POST':
        item_name = request.POST['item_name']
        quantity = request.POST['quantity']
        current_stock = request.POST['current_stock']
        # date_received = request.POST['date_recieved']
        item = Item(item_name=item_name, quantity=quantity, current_stock=current_stock)
        item.save()
        return render(request, 'application/inventory.html')
    else:
        return render(request, 'application/add_inventory.html') 
def settings(request):
    template = loader.get_template('application/settings.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('application/login.html')
    return HttpResponse(template.render())

def logout(request):
    request.session.flush()
    return redirect('login')


def editsitter(request, id):
    
    if request.method == 'POST':
        print('post successful')
        return redirect('/sitter/')
    else:
        sitters = Sitter.objects.get(id=id)
        return render(request, 'application/edit_sitter.html', {'sitters':sitters})
    
def deletesitter(request, id):
    sitter = Sitter.objects.get(id=id)
    sitter.delete()
    return redirect('/sitter/')

def edit_baby(request, id):
    babe = Baby.objects.get(id = id)
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        gender = request.POST['gender']
        age = request.POST['age']
        parent_name = request.POST['parent_name']
        timein = request.POST['timein']
        fees = request.POST['fees']
        broughtby = request.POST['broughtby']
        babynumber  = request.POST['babynumber']
        message_left = request.POST['message_left']
        # stay_duration = request.POST['stay_duration']
        
        babe.fname = fname
        babe.lname = lname
        babe.gender = gender
        babe.parent_name = parent_name
        babe.timein = timein
        babe.age = age
        babe.broughtby = broughtby
        babe.fees = fees
        babe.babynumber = babynumber
        babe.message_left = message_left
        # babe.stay_duration = stay_duration
        babe.save()
        print('update successful')
        return redirect('/baby/')
    else:
        return render(request, 'application/edit_baby.html', {'babe':babe})
def deletebaby(request, id):
    baby = Baby.objects.get(id=id)
    baby.delete()
    return redirect('/baby/')
     