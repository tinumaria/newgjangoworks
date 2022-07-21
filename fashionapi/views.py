import datetime

from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

import datetime
from functools import reduce

class HelloWorldView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"hello world"})

class GoodmorningView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"good morning"})

#based on time, give greetings

class GreetingsView(APIView):
    def get(self,request,*args,**kwargs):
        cur_time=datetime.datetime.now()
        cur_hour=cur_time.hour
        msg=""
        if cur_hour<12:
            msg="Good morning"
        elif cur_hour<18:
            msg="Good afternoon"
        elif cur_hour<24:
            msg="Good evening"
        return Response({"data":msg})

class CubeView(APIView):
    def post(self,request,*args,**kwargs):
        n=request.data.get("num")
        res=n**3
        return Response({"cube":res})

class FactorialView(APIView):
    def post(self,request,*args,**kwargs):
        n=request.data.get("num")
        fact=1
        for i in range(1,n+1):
            fact*=i
        return Response({"fact":fact})
#or
class FactorialViewNew(APIView):
    def post(self,request,*args,**kwargs):
        n=request.data.get("num")
        fact=reduce(lambda n1,n2:n1*n2,range(1,n+1))
        return Response({"fact":fact})

#wordcount
class WordCountView(APIView):
    def post(self,request,*args,**kwargs):
        text=request.data.get("text")
        wc={}
        word=text.split(' ')
        for i in word:
            if i not in wc:
                wc[i]=1
            else:
                wc[i]+=1
        return Response({"data":wc})
