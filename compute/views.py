from django.shortcuts import render

# Create your views here.
def loan(request):
    args = {'user':request.user}
    return render(request,'accounts3/loan.html',args)
