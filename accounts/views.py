from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# 로그인 뷰
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # 사용자명
        password = request.POST.get('password')  # 비밀번호

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, '아이디 또는 비밀번호가 올바르지 않습니다.')

    return render(request, 'accounts/login.html')
from django.conf import settings
print("TEMPLATE DIRS:", settings.TEMPLATES[0]['DIRS'])


# 홈 뷰 (로그인된 사용자만 접근 가능)
@login_required
def home_view(request):
    return render(request, 'accounts/home.html', {'user': request.user})

# 로그아웃 뷰
def logout_view(request):
    logout(request)
    return redirect('login')

