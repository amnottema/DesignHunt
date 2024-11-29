from django.shortcuts import render
from create_portfolio.models import Portfolio

def designers(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'designers/designers.html', {'portfolios': portfolios})