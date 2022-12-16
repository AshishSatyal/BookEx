'use strict';

$('.book_img_rotator').hiSlide(); //best selling books animation

window.addEventListener('scroll', reveal);

function reveal() {
    const revealCard = document.querySelectorAll('.card');

    revealCard.forEach(card => {
        let windowheight = window.innerHeight;
        let revealtop = card.getBoundingClientRect().top; //cards top value on the window
        const revealPoint = 150;

        if(revealtop < windowheight - revealPoint) {
            card.classList.add('active');
        }
    })
}