from django.urls import path
from . import views  # 같은 디렉토리의 views.py 불러오기

urlpatterns = [
    path('', views.index, name='index'),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('pybo/', include('book.urls')),
    path('' , include('pybo.urls')),