from django.shortcuts import render
import requests

# Create your views here.
def Home(request):
    urls='https://dummyjson.com/products'
    res=requests.get(urls)
    if res.status_code==200:
        data=res.json()
        print(data)
    return render(request,'index.html',{'data':data})


def about(request):

    return render(request,'about.html')