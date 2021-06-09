from django.shortcuts import render,redirect
from .forms import myform
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from .Models.models import Product
from .Models.models import Category
from .Models.order import Order
from .Models.smartfarming import smartfar
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib import messages


# Create your views here.
def firstpage(request):
    return render(request,"dashboard.html")

""" it checks the method is POST or not using request.POST and myform is form from forms.py user_form which check values from
 myform is valid or not if it is not post it displays blank form """

def register(request):
    if request.method == "POST":
        
        user_form = myform(request.POST)
        if user_form.is_valid():
            
            user_form.save()
            
            return HttpResponseRedirect("/")
    else:
        user_form = myform()
    return render(request,"registerform.html",{"user_form":user_form})

""" authenticate checks that username and password is valid or ot means it is in user.database or not. In auth.login()  gives 
permissions  for specific user"""
 
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        
        uname = request.POST.get('username')
        request.session['uname'] = uname
        user = auth.authenticate(username=username,password=password)
        #uname = request.POST.get('username')
        #request.session['uname'] = uname
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect("/homepage/")
        else:
            messages.error(request,"Invalid id password ")
            return redirect("/login")
        
    return render(request,"login.html")


def homepage(request):
    try:
        print("1")
        uname1 = request.session['uname']
        print("2")
        prod = smartfar.objects.all();
        print("3")
        return render(request,"homepage.html",{'uname':uname1,'products':prod})
    except:
        return HttpResponseRedirect("/login/")

def search(request,id):
        
        prod11 = Product.objects.filter(category=id)
        if request.method=="GET" :
            if prod11:
                return render(request,"pk.html",{'products':prod11})
            else:
                prod11 = Product.objects.all()
                return render(request,"pk.html",{'products':prod11})


        else:
            productid=request.POST.get('demo')
            quantity=request.POST.get('quantity')
            if quantity:
                request.session['productid']=productid
                request.session['quantity']=quantity
                return HttpResponseRedirect("/cart")
            else:
                messages.error(request,"please enter quantity")
                return redirect('/search3')
       



def order(request):
    
    if request.method=="POST":
      
        pkid=request.session['productid']
        #name1=request.POST.get('name1')
        #request.session['name1']=name1
        #print(request.session['name1'])
        order = Order(productname=Product(id=pkid),customer=request.session['uname'],quantity=request.session['quantity'],price=request.POST.get('price'),address=request.POST.get('address'),mobilno=request.POST.get('mobno'))
        order.save()

        list1=Order.objects.filter(productname=request.session['productid'],customer=request.session['uname']).order_by('-id')[:1];
        name=User.objects.filter(username=request.session['uname'])
        print(list1)


        template_path = 'receipt.html'
        context = {'myvar': list1,'name':name}
    
        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] =  'attachment; filename="receipt.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisa_status = pisa.CreatePDF(
        html, dest=response)
        # if error then show some funy view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        

        return response
    else:
        context={}
        prodid=request.session['productid']
        #context['name']=User.objects.filter(username=request.session['uname'])
        context['filteredproduct'] = Product.objects.filter(id=prodid)
        context['quan']=request.session['quantity']

        return render(request,"cartsection.html",context)

def orderlist(request):
    list1=Order.objects.filter(customer=request.session['uname']).order_by('-id');
    return render(request,"orderlist.html",{'list1':list1})

"""
def render_pdf_view(request):
    list1=Order.objects.filter(productname=request.session['productid'],customer=request.session['uname']).order_by('-id')[:1];
    name=User.objects.filter(username=request.session['uname'])
    print(list1)


    template_path = 'receipt.html'
    context = {'myvar': list1,'name':name}
    
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] =  'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return redirect('/homepage')

  
"""
def contactus(request):
    return render(request,"contact.html")       
    
def logout(request):
    try:
        del request.session['uname']
        del request.session['productid']
        del request.session['quantity']
        print("4")
        auth.logout(request)
    except:
        
        auth.logout(request)
    return redirect("/") 


    
