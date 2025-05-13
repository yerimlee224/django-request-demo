from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("메인 페이지입니다.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('book/', include('apps.book.urls')),
    path('pybo/', include('pybo.urls')),
    path('', home),  # ← 빈 경로에 대응
    path('', include('request_test.urls')),

]








