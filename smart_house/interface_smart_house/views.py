from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    host = request.META["HTTP_HOST"]
    user_agent = request.META["HTTP_USER_AGENT"]
    user_address = request.META["REMOTE_ADDR"]
    path = request.path

    return HttpResponse(f"""
            <p> HOST: {host} </p>
            <p> user_agent: {user_agent} </p>
            <p> user_address: {user_address} </p>
            <p> path: {path} </p>
    """, headers={"SecretCode": "21234567"})

def about(request, name, age):
    return HttpResponse(f"""
            <h2> About user </h2>
            <p> name: {name} </p>
            <p> age: {age} </p>
            """)