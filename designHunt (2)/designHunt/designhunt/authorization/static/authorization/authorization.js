const flipCard = document.querySelector('.flip-card');
const toggleButtons = document.querySelectorAll('.toggle-form');

toggleButtons.forEach((button) => {
    button.addEventListener('click', () => {
        flipCard.classList.toggle('flipped');
    });
});