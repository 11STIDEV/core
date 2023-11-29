from django.shortcuts import redirect


def redirect_user(request, ):
    if request.user.is_authenticated:
        return redirect(f'profile/')
    else:
        return redirect('accounts/login')
