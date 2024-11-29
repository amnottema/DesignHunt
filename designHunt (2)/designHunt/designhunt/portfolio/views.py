from django.shortcuts import render, get_object_or_404
from create_portfolio.models import Portfolio, PortfolioFile

def portfolio_detail(request, user_id):
    portfolio = get_object_or_404(Portfolio, user_id=user_id)
    portfolio_files = PortfolioFile.objects.filter(portfolio=portfolio)
    return render(request, 'portfolio/portfolio_detail.html', {'portfolio': portfolio, 'portfolio_files': portfolio_files})