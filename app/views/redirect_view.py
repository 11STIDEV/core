from django.shortcuts import redirect, HttpResponse


def redirect_domain(request, ):
    if 'portalcci.com.br' in request.user.email:
        return redirect('profile')
    else:
        return HttpResponse('USUARIO INVALIDO')