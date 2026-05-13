from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        'title': 'Product List',
        'records':[
            {'id':'99022','name':'Avocado','price':90.12},
            {'id':'65639','name':'Mango','price':170.45}
        ]
    }
    return render(request,'crudapp/home.html',context)