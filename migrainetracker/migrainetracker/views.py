from django.shortcuts import render
from django.http import HttpResponse

HTML_STRING = """<h1> Migraine Tracker - Hello World </h1>"""


def home_view(request):
    """
    Take in a request
    Return an HTML as a response
    """
    return HttpResponse(HTML_STRING)