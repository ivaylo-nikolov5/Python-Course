from django.shortcuts import render
from django import http

from django101.tasks.models import Task


def show_bare_minimum_view(request):
    return http.HttpResponse("It works!!!")


def show_all_tasks(request):
    all_tasks = Task.objects.order_by("id").all()
    result = ", ".join(f"{t.name}({t.id})" for t in all_tasks)
    return http.HttpResponse(result)