from django.shortcuts import render, redirect


def pagina_inicial(request,):
    if request.user.is_authenticated:
        # Se o domínio do email do usuário for '@portalcci.com.br'
        # ele é liberado para acessar o portal. Caso o domínio seja
        # outro da instituição, ele é redirecionado para a pagina de
        # logout.
        if 'portalcci.com.br' in request.user.email:
            return render(request, 'pages/index.html', {'context': 'context'})
        else:
            return redirect('account_logout')
    else:
        return redirect('account_login')
