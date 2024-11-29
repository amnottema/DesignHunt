from django.shortcuts import render, redirect, get_object_or_404
from .forms import PortfolioForm, PortfolioFileForm
from .models import Portfolio, PortfolioFile
from django.contrib.auth.decorators import login_required

@login_required
def create_portfolio(request):
    if request.method == 'POST':
        portfolio_form = PortfolioForm(request.POST, request.FILES)
        file_form = PortfolioFileForm(request.POST, request.FILES)

        if portfolio_form.is_valid():
            portfolio = portfolio_form.save(commit=False)
            portfolio.user = request.user
            portfolio.save()

            PortfolioFile.objects.filter(portfolio=portfolio).delete()

            uploaded_files = request.FILES.getlist('portfolios')
            if uploaded_files:
                for uploaded_file in uploaded_files[:3]:
                    PortfolioFile.objects.create(portfolio=portfolio, file=uploaded_file)

            return redirect('create_portfolio')
    else:
        portfolio = Portfolio.objects.filter(user=request.user).first()
        portfolio_form = PortfolioForm(instance=portfolio) if portfolio else PortfolioForm()
        file_form = PortfolioFileForm()

    return render(request, 'create_portfolio/create-portfolio.html', {'portfolio_form': portfolio_form, 'file_form': file_form, 'portfolio': portfolio})