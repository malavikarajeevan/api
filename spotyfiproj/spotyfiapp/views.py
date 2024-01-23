from django.shortcuts import render
import requests

# Create your views here.
def Home(request):
    urls='https://jsonplaceholder.typicode.com/posts'
    res=requests.get(urls)
    if res.status_code==200:
        data=res.json()
        print(data)
    return render(request,'index.html',{'data':data})