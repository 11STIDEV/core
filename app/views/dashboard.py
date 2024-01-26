from django.shortcuts import render, redirect


def dashboard(request, username):
    if request.user.is_authenticated:
        return render(
            request,
            'planejamento_semanal/dashboard.html'
        )
    else:
        return redirect('accounts:home')
