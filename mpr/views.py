from django.shortcuts import render
from django.http import HttpResponse
from .models import *  # Import the Registration model
from django.db.models import Max,Min
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.db.models import Q
from datetime import date as d, datetime as dt
from datetime import date, datetime
from django.shortcuts import render, redirect
from django.contrib import messages



def index(request):

    return render(request, "index.html")
def login(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = Login.objects.get(view_email=email, view_password=password)
            if user is not None:
                if user.user_type == 'admin':
                    print('admin#####')
                    messages.info(request, 'Welcome to admin dashboard')
                    return redirect('/admin_dash')
                elif user.user_type == 'customer':
                    request.session['cid'] = user.id
                    request.session['cemail'] = user.view_email
                    request.session['type'] = user.user_type
                    print('cust#####')
                    messages.info(request, 'Welcome to customer dashboard')
                    return redirect('/customer_dash')
                elif user.user_type == 'seller':
                    request.session['sid'] = user.id
                    request.session['semail'] = user.view_email
                    request.session['type'] = user.user_type
                    print('seller#####')
                    messages.info(request, 'Welcome to seller dashboard')
                    return redirect('/seller_dash')
                else:
                    pass
            else:
                pass
        except Login.DoesNotExist:
                print("Login matching query does not exist. User not found.")
       
    return render(request, "login.html")
def about(request):
    return render(request, "about.html")
def contact(request):
    return render(request, "contact.html")



def customer_reg(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['Phone']
        image = request.POST['image']
        if Login.objects.filter(view_email=email).exists():
            messages.info(request, 'Already registered')
            return redirect('/')
        else:
            customer_ = Login.objects.create(
                view_email=email, view_password=password, user_type='customer')
            customer_.save()
            reg = Customer.objects.create(
                username=customer_, name=name, email=email, phone=phone,image=image)
            reg.save()
            return redirect('/')
    return render(request, "customer_reg.html")   
 

 #admin
def admin_dash(request):
    return render(request, "ADMIN/admin_dash.html")
def Admin_viewRequest(request):
    data = Request.objects.all()
    return render(request, "ADMIN/Admin_viewRequest.html",{'data':data})
from django.shortcuts import get_object_or_404, redirect
from .models import Request

def reject_request(request):
    req_id = request.GET.get('id')
    req = get_object_or_404(Request, id=req_id)  # Retrieve the object or return 404 if not found
    req.status = "rejected"
    req.save()

    return redirect('/Admin_viewRequest')  # Assuming you want to redirect to the same page after processing

def approve(request):
    req_id = request.GET.get('id')
    req = get_object_or_404(Request, id=req_id)  # Retrieve the object or return 404 if not found
    req.status = "approved"
    req.save()
    cus_id=req.customer_id
    caption=req.caption
    description=req.description
    platform=req.platform
    startDate=req.startDate
    endDate=req.endDate
    location=req.location
    prefered_age_group=req.prefered_age_group
    adimage=req.adimage
    keywords=req.keywords
    customer = Customer.objects.get(id = cus_id)

    add = ConfirmedRequest.objects.create(customer= customer, caption=caption, description=description, platform=platform,
        startDate=startDate,endDate=endDate,location=location,prefered_age_group=prefered_age_group,adimage=adimage,keywords=keywords)
    add.save()
    return redirect('/Admin_viewRequest')  # Assuming you want to redirect to the same page after processing


def Admin_viewConfirmedreq(request):
    data = ConfirmedRequest.objects.all()
    return render(request, "ADMIN/Admin_viewConfirmedreq.html",{'data':data})

def admin_addAmount(request):
    req_id = request.GET.get('id')
    data = ConfirmedRequest.objects.get(id =req_id)
    
    if request.POST:
        amount = request.POST['amount']
        data.price = amount
        data.paymentstatus='pending'
        data.save()
        confirmedreq_id =data.id
        confirmedRequest = ConfirmedRequest.objects.get(id =confirmedreq_id)
        customer_id =data.customer_id
        customer = Customer.objects.get(id =customer_id)
        cre = Adminreport.objects.create(customer= customer,ConfirmedRequest=confirmedRequest)
        cre.save()
        return redirect('/Admin_viewConfirmedreq')
    return render(request, "ADMIN/admin_addAmount.html",{'data':data})

def addreport(request):
    req_id = request.GET.get('id')
    data = Adminreport.objects.get(ConfirmedRequest =req_id)
    if request.POST:
        like = request.POST['like']
        comment = request.POST['comment']
        share = request.POST['share']
        linkBasedinteraction = request.POST['linkBasedinteraction']
        keywordBasedinteraction = request.POST['keywordBasedinteraction']
        ageBasedinteraction = request.POST['ageBasedinteraction']
        data.like = like
        data.comment= comment
        data.share = share
        data.linkBasedinteraction= linkBasedinteraction
        data.keywordBasedinteraction = keywordBasedinteraction
        data.ageBasedinteraction= ageBasedinteraction
        data.save()
        
        return redirect('/Admin_viewConfirmedreq')
    return render(request, "ADMIN/addreport.html")

def admin_viewReport(request):
    req_id = request.GET.get('id')
    data = Adminreport.objects.filter(id =req_id)
    return render(request, "ADMIN/admin_viewReport.html",{'data':data})
def view_customers(request):

    data = Customer.objects.all()
    return render(request, "ADMIN/view_customers.html",{'data':data})
def delete_customers(request):
        id = request.GET.get('id')
        customer =Customer.objects.get(id =id)
        log_id =customer.username_id
        customer.delete()
        dele = Login.objects.get(id=log_id)
        dele.delete()
        return redirect('/view_customers')

 
#Customer
def customer_dash(request):
    return render(request, "CUSTOMER/customer_dash.html")

from datetime import date
def add_request(request):
    cid = request.session['cid']
    customer =Customer.objects.get(username_id =cid)
   

    if request.POST:
        caption = request.POST['caption']
        description = request.POST['description']
        platform = request.POST['platform']
        startDate = request.POST['startDate']
        endDate = request.POST['endDate']
        location = request.POST['location']
        prefered_age_group = request.POST['prefered_age_group']
        adimage = request.POST['adimage']
        keywords = request.POST['keywords']
        add = Request.objects.create(customer= customer, caption=caption, description=description, platform=platform,
        startDate=startDate,endDate=endDate,location=location,prefered_age_group=prefered_age_group,adimage=adimage,keywords=keywords)
        add.save()
        messages.info(request, 'Request added')
        return redirect('/customer_dash')
           
    return render(request, "CUSTOMER/add_request.html")


def view_request(request):
    cid = request.session['cid']
    customer =Customer.objects.get(username_id =cid)
    cus_id =customer.id
    data = Request.objects.filter(customer_id =cus_id)
    return render(request, "CUSTOMER/view_request.html",{'data':data})

def cancel_request(request):
    req_id = request.GET.get('id')
    req = Request.objects.get(id=req_id)
    req.status = "cancelled"
    req.save()

    return redirect('/view_request')

def customer_viewConfirmedreq(request):
    data = ConfirmedRequest.objects.all()
    return render(request, "CUSTOMER/customer_viewConfirmedreq.html",{'data':data})
def pay(request):
    req_id = request.GET.get('id')
    if request.POST:
        req = ConfirmedRequest.objects.get(id=req_id)
        req.paymentstatus = "paid"
        req.save()
        return redirect('/customer_viewConfirmedreq')
    
    return render(request, "CUSTOMER/pay.html")
def view_report(request):
    data = Adminreport.objects.all()
    return render(request, "CUSTOMER/view_report.html",{'data':data})

