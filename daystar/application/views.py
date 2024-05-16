from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .models import *
# from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import  logout
from django.contrib.auth.decorators import login_required


# Create your views here.
#home view, sitter view, baby view, payment view, procurement view
@login_required
def index(request):
    baby_list = Baby.objects.all()
    count_babies =len(baby_list)
    sitters_List = Sitter.objects.all()
    count_sitters = len(sitters_List)
    payments = Pay.objects.all()
    count_payments = Pay.objects.count()
    recent_babies = Baby.objects.all()[:5]
    recent_sitters = Sitter.objects.all()[:5]
    item = Doll_item.objects.all()
    count_items = Doll_item.objects.count()
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
@login_required
def addbaby(request):
    message = None
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        gender = request.POST['gender']
        age = request.POST['age']
        parent_name = request.POST['parent_name']
        timein  = request.POST['timein']
        # fees = request.POST['fees']
        broughtby = request.POST['broughtby']
        babynumber  = request.POST['babynumber']
        message_left = request.POST['message_left']
        # stay_duration = request.POST['stay_duration']
        # Address = request.POST['address'] 
        baby = Baby(fname=fname, lname=lname, gender=gender, age=age, parent_name=parent_name, timein=timein,  broughtby=broughtby, babynumber=babynumber, message_left=message_left )
        baby.save()
        message = 'Baby added successfully'
    context = {
        'message':message
    }
    template = loader.get_template('application/add_baby.html')
    return HttpResponse(template.render(context))
@login_required
def addsitter(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        gender = request.POST['gender']
        age = request.POST['age']
        address = request.POST['location']
        contact = request.POST['contact'] 
        status = request.POST['status']
        sitter = Sitter(fname=fname, lname=lname, gender=gender, age=age, location=address, contact=contact, status=status)
        sitter.save()
        # messages = 'Sitter added successfully'
    # contxt = {
    #     'messages': messages tis is the siiter message that refused to wrk 
    # }
    template = loader.get_template('application/add_sitter.html')
    return HttpResponse(template.render())

@login_required
def viewbaby(request, id):
    baby_obj = Baby.objects.get(id = id)
    # all_pays = Pay.objects.filter(payee=id)
    stay_duration = Baby.objects.filter(id=id)
    context = {
       'baby': baby_obj,
        # 'all_pays': all_pays,
        'stay_duration': stay_duration,
    }
    template = loader.get_template('application/view_baby.html')
    return HttpResponse(template.render(context))

@login_required
def viewsitter(request,id):
    sitters = Sitter.objects.get(id=id)
    context = {
       'sitters': sitters
    }
    template = loader.get_template('application/view_sitter.html')
    return HttpResponse(template.render(context))
    
    
    
@login_required
def baby(request):
    babies = Baby.objects.all()
    context = {
        'babies': babies
    }
    template = loader.get_template('application/baby_list.html')
    return HttpResponse(template.render(context))
@login_required
def sitter(request):
    sitters = Sitter.objects.all()
    context = {
       'sitters': sitters
    }
    template = loader.get_template('application/sitter_list.html')
    return HttpResponse(template.render(context))
@login_required
def payment(request):
    if request.method == 'POST':
        amount = request.POST['amount']
        date = request.POST['date']
        baby_id = request.POST['id']
        stay_duration = request.POST.get('stay_duration')
        baby = Baby.objects.get(id=baby_id )
        pay = Pay(baby=baby, amount= amount, date = date, stay_duration=stay_duration)
        pay.save()
        return redirect('payment_success', id=baby_id)
    else:
        babies = Baby.objects.all()
        pays = Pay.objects.all()
        return render(request, 'application/payments.html', {'babies': babies, 'pays':pays})
@login_required
def payment_success(request, id):
    baby = Baby.objects.get(id=id)
    return render(request, 'application/payment_success.html', {'baby':baby})

@login_required
def inventory(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    template = loader.get_template('application/inventory.html')
    return HttpResponse(template.render(context))

@login_required
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
    
@login_required
def settings(request):
    template = loader.get_template('application/settings.html')
    return HttpResponse(template.render())

@login_required
def register(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email= request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        myuser = User.objects.create_user(user_name, email, pass1)
        
        myuser.first_name = first_name
        myuser.last_name = last_name
        
        myuser.save()
        
        messages.success(request, 'Your account has been created successfully!')
        return redirect('/')
        
    return render(request, 'application/register.html')

@login_required
def doll_list(request):
    items = Doll_item.objects.all()
    count_items=len(items)
    context={'items': items, 'count': count_items}
    return render(request, 'application/doll_list.html', context)

@login_required
def shopitem_delete(request, id):
    Doll_item.objects.filter(id=id).delete()
    return redirect('/doll_list/')

@login_required
def doll_add(request):
    message = None
    if request.method == 'POST':
        # Extracting all fields from the POST request
        instance = request.POST
        shopitem = Doll_item(
            item_name=instance.get('item_name'),
            item_description=instance.get('item_description'),
            item_quantity=instance.get('item_quantity'),
            # date_added = date_added,
            )
        shopitem.save()
        message =  " added successfully"

    context = {'message': message}
    return render(request, 'application/dollitem_add.html', context)

@login_required
def doll_edit(request, id):
    message = None
    
    obj = Doll_item.objects.get(id=id)
    if request.method == 'POST':
        obj.item_name = request.POST.get('item_name')
        obj.item_description = request.POST.get('item_description')
        obj.item_quantity = request.POST.get('item_quantity')
        obj.date_added = request.POST.get('date_added')
        
        obj.save()
        return redirect('/shopitem_list/' )
        
    context = {'obj': obj}
    return render(request, 'application/dollitem_edit.html', context)

#transactions
@login_required
def transaction_list(request):
    transactions = Doll_transction.objects.all()
    return render(request, 'application/transaction_list.html', {'transactions': transactions})


@login_required
def transaction_delete(request, id):
    Doll_transction.objects.filter(id=id).delete()
    return redirect('/transaction_list/')      


def transaction_add(request):
    if request.method == 'POST':
        item_id = request.POST['doll_name']
        transaction_type = request.POST['transaction_type']
        transaction_quantity = request.POST['transaction_quantity']
        
        # Retrieve the item from Shopitem model
        item = Doll_item.objects.get(pk=item_id)
        
        if transaction_type == 'BUY':
            item.item_quantity += int(transaction_quantity)
            item.save()
        elif transaction_type == 'SELL':
            if item.item_quantity >= int( transaction_quantity):
                item.shop_quantity -= int( transaction_quantity)
                item.save()
            else:
                # Handle insufficient quantity scenario here
                pass
        
        # Create Transaction object
        Doll_transction.objects.create(
             item=item,
            transaction_type=transaction_type,
            transaction_quantity=transaction_quantity,
           transaction_date=request.POST.get('transaction_date'),
            unit_price=request.POST.get('unit_price'),
            total_price=request.POST.get('total_price')
        )
        
        return redirect('/transaction_list/')
    else:
        items = Doll_item.objects.all()
        return render(request, 'application/transaction_add.html', {'items': items})


@login_required
def transaction_edit(request, id):
    if request.method == 'POST':
        item_id = request.POST['item']
        transaction_type = request.POST['transaction_type']
        transaction_quantity= request.POST['transaction_quantity']
        
        try:
            item = Doll_item.objects.get(pk=item_id)
        except Doll_item.DoesNotExist:
            return render(request, 'error.html', {'message': 'Item not found'})
        
        if transaction_type == 'BUY':
            item.item_quantity += int(transaction_quantity)
            item.save()
        elif transaction_type == 'SELL':
            if item.item_quantity >= int(transaction_quantity):
                item.item_quantity -= int(transaction_quantity)
                item.save()
            else:
                return render(request, 'error.html', {'message': 'Insufficient quantity'})
        
        # Retrieving the transaction object
        try:
            transaction = Doll_transction.objects.get(pk=id)
        except Doll_transction.DoesNotExist:
            return render(request, 'error.html', {'message': 'Transaction not found'})
        
        # Updating Transaction object
        transaction.item = item
        transaction.transaction_type = transaction_type
        transaction.transaction_quantity = transaction_quantity
        # transaction.paymentby = request.POST.get('paymentby')
        transaction.unit_price = request.POST.get('unit_price')
        transaction.total_price = request.POST.get('total_price')
        transaction.save()
        
        return redirect('/transaction_list/')
    else:
        items = Doll_item.objects.all()
        try:
            transaction = Doll_transction.objects.get(pk=id)
        except Doll_transction.DoesNotExist:
            return render(request, 'error.html', {'message': 'Transaction not found'})
        
        return render(request, 'application/transaction_edit.html', {'items': items, 'transaction': transaction})




@login_required
def editsitter(request, id):
    sitters = Sitter.objects.get(id= id)
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        gender = request.POST['gender']
        age = request.POST['age']
        location = request.POST['location']
        NxtoK = request.POST['NxtoK']
        DOB = request.POST['DOB']
        NIN = request.POST['NIN']
        recommender = request.POST['recommender']
        educationlevel = request.POST['educationlevel']
        sitternumber = request.POST['sitternumber']
        contact = request.POST['contact']
        status = request.POST['status']
        
        sitters.fname = fname
        sitters.lname = lname
        sitters.gender = gender
        sitters.age = age
        sitters.location = location
        sitters.NxtoK = NxtoK
        sitters.DOB = DOB
        sitters.NIN = NIN
        sitters.recommender = recommender
        sitters.educationlevel = educationlevel
        sitters.sitternumber = sitternumber
        sitters.contact = contact
        sitters.status = status
        
        sitters.save()
        print('post successful')
        return redirect('/sitter/')
    else:
        sitters = Sitter.objects.get(id=id)
        return render(request, 'application/edit_sitter.html', {'sitters':sitters})

@login_required    
def deletesitter(request, id):
    sitter = Sitter.objects.get(id=id)
    sitter.delete()
    return redirect('/sitter/')

@login_required
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
    
@login_required
def deletebaby(request, id):
    baby = Baby.objects.get(id=id)
    baby.delete()
    return redirect('/baby/')


def logout_view(request):
    logout(request)
    return redirect('/')
     