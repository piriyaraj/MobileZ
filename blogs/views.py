from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'blogs/pages/index.html')

def post(request,model,phone):
    print(model,phone)
    return render(request,'blogs/pages/post.html')