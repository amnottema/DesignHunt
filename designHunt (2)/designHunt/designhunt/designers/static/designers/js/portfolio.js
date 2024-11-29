const filterButtons = document.querySelectorAll('.filter-button');
const portfolios = document.querySelectorAll('.portfolio-list-item');
const openMoreButton = document.querySelector('.open-more-button');
let availablePortfolioOnDisplay = 9;

const updatePortfolioVisibility = () => {
    const activeButton = document.querySelector('.filter-button.active');
    const filterClass = activeButton?.classList.contains('ux-ui-button') ? 'ux-ui-designer' : 'illustartor';

    const filteredPortfolios = Array.from(portfolios).filter(portfolio =>
        portfolio.classList.contains(filterClass)
    );

    portfolios.forEach(portfolio => {
        portfolio.style.display = filteredPortfolios.includes(portfolio) ? 'block' : 'none';
    });

    return filteredPortfolios;
};

const limitPortfolioOnDisplay = (filteredPortfolios) => {
    filteredPortfolios.forEach((portfolio, index) => {
        portfolio.style.display = index < availablePortfolioOnDisplay ? 'block' : 'none';
    });

    openMoreButton.style.display =
        availablePortfolioOnDisplay >= filteredPortfolios.length ? 'none' : 'flex';
};

filterButtons.forEach(filterButton =>
    filterButton.addEventListener('click', () => {
        filterButtons.forEach(btn => btn.classList.remove('active'));
        filterButton.classList.add('active');

        availablePortfolioOnDisplay = 9;
        const filteredPortfolios = updatePortfolioVisibility();
        limitPortfolioOnDisplay(filteredPortfolios);
    })
);

openMoreButton.addEventListener('click', () => {
    availablePortfolioOnDisplay += 9;
    const filteredPortfolios = updatePortfolioVisibility();
    limitPortfolioOnDisplay(filteredPortfolios);
});


const filteredPortfolios = updatePortfolioVisibility();
limitPortfolioOnDisplay(filteredPortfolios);
