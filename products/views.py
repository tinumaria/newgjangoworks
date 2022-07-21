from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import *

class ProductsView(APIView):
    def get(self,request,*args,**kwargs):
        if "limit" in request.query_params:
            limit=int(request.query_params.get("limit"))
            limit_prod=products[0:limit]
            return Response(data=limit_prod)
        else:
            return Response(data=products)

    def post(self,request,*args,**kwargs):
        prod=request.data
        products.append(prod)
        return Response(data=products)

class ProductDetailView(APIView):
    def get(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        prod=[prod for prod in products if prod["id"]==pid].pop()
        return Response(data=prod)
    def delete(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        prod=[prod for prod in products if prod["id"]==pid].pop()
        products.remove(prod)
        return Response(data=products)
    def put(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        prod=[prod for prod in products if prod["id"]==pid].pop()
        prod.update(request.data)
        return Response(data=prod)