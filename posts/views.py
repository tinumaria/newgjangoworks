from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from posts.models import *

class PostView(APIView):

    def get(self,request,*args,**kwargs):

        #list limited post
        if "limit" in request.query_params:
            limit=int(request.query_params.get("limit"))
            limit_post=blogs[0:limit]
            return Response(data=limit_post)

        #list post liked by a user
        if "liked_by" in request.query_params:
            id=int(request.query_params.get("liked_by"))
            liked_post=[blog for blog in blogs if id in blog["liked_by"]]
            return Response(data=liked_post)

        # list all post
        else:
            return Response(data=blogs)
            #return Response({"data":blogs})

    #create a post, method:post
    #data={"postId":10,"userId":2,"title":"good","content":"hello"}
    def post(self,request,*args,**kwargs):
        blog=request.data #fetching payload
        blogs.append(blog)
        return Response(data=blog)


class PostDetailView(APIView):

    #specific post, method:get
    #url: http://127.0.0.1:8000/social/posts/{pid}
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pid")
        blog=[blog for blog in blogs if blog["postId"]==id].pop()
        return Response(data=blog)

    #delete a post
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("pid")
        blog=[blog for blog in blogs if blog["postId"]==id].pop()
        blogs.remove(blog)
        return Response(data=blog)

    #update a post
    def put(self,request,*args,**kwargs):
        id=kwargs.get("pid")
        blog=[blog for blog in blogs if blog["postId"]==id].pop()
        blog.update(request.data)
        return Response(data=blog)


#like a post, method:post
#url: http://127.0.0.1:8000/social/posts/likes/<int:pid>
class AddLikeView(APIView):
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pid")
        blog=[blog for blog in blogs if blog["postId"]==id].pop()
        user=request.data.get("userId")
        blog["liked_by"].append(user)
        return Response(data=blog)



