# apps/book/views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse("안녕하세요, book 앱입니다!")








