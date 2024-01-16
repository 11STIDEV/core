from django.shortcuts import redirect


def redirect_user(request, ):
    if request.user.is_authenticated:
        return redirect('profile/')
    else:
        return redirect('accounts/login')
