from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Menu,Choice

#单步调试
#import pdb;pdb.set_trace()

# The first view called home to describe the home page 
# including sereral links, Bobo's booth is link of home page
def home(request):
	menulist = Menu.objects.order_by('-id')
	context = {'menulist':menulist}
	return render(request,'lemonade/home.html',context)


#The second view called "detail" 
def detail(request,menu_id):
    menu = get_object_or_404(Menu,pk=menu_id)
    return render(request,'lemonade/detail.html',{'menu':menu})

  
