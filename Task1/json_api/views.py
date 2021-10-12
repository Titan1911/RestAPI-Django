from django.shortcuts import render
import json
from .models import Account
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView
from .serializers import AccountSerializer

# Create your views here.
def account(request):
    if Account.objects.exists():
        accounts = Account.objects.all()
        return render(request, 'home.html', {
            'accounts': accounts
        })
    path='data.json'
    with open(path,'r') as i:
        data=json.load(i)
    # print(a)
    # data=json.load(f)
    for i in data['data']:
        Account.objects.create(account_no=i['account_no'],isActive=i['isActive'],balance=i['balance'])
    accounts = Account.objects.all()
    print(accounts)
    return render(request, 'home.html', {
        'accounts': accounts
    })
    # return render(request,'home.html')

@api_view(['GET'])
def accountApi(request):
    api_urls={
        'List':'/account-list/',
        'Detail':'/account-delete/',
        'Create':'/account-create/',
        'Delete':'/account-delete/',
    }
    return Response(api_urls)

# @api_view(['GET'])
# def accountList(request):
#     account=Account.objects.all()
#     serializer=AccountSerializer(account,many=True)
#     return Response(serializer.data)
#
# @api_view(['GET'])
# def accountDetail(request,pk):
#     account=Account.objects.get(id=pk)
#     serializer=AccountSerializer(account,many=False)
#     return Response(serializer.data)
#
# @api_view(['POST'])
# def accountCreate(request):
#     serializer = AccountSerializer(data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#
#     return Response(serializer.data)
#
# @api_view(['DELETE','GET'])
# def accountDelete(request,pk):
#     account=Account.objects.get(id=pk)
#     account.delete()
#
#     return Response(f"Item with id:{pk} successfully Deleted")
#

class accountListAPIView(ListAPIView):
    serializer_class = AccountSerializer
    queryset=Account.objects.all()

class accountUpdateAPIView(UpdateAPIView):
    serializer_class=AccountSerializer
    queryset = Account.objects.all()

class accountCreateAPIView(CreateAPIView):
    serializer_class=AccountSerializer
    queryset = Account.objects.all()

class accountDeleteAPIView(DestroyAPIView):
    serializer_class=AccountSerializer
    queryset = Account.objects.all()

class accountRetrieveAPIView(RetrieveAPIView):
    serializer_class=AccountSerializer
    queryset = Account.objects.all()