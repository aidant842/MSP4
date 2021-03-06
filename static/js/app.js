var toggleMultiple = function(element, class0, class1) {
    element.classList.toggle(class0);
    element.classList.toggle(class1);
  }

const cardFade = () => {
    const cards = document.querySelectorAll('.card');
    const cardOverlay = document.querySelectorAll('.card-img-overlay');
    const cardText = document.querySelectorAll('.image-text');

    cards.forEach((card) => {
        card.addEventListener('mouseover', () => {
            cardOverlay.forEach((card) => {
                card.style.animation = `cardOverlayFade 0.5s ease-in-out`;
            });
            cardText.forEach((card) => {
                card.style.animation = `cardTextFade 0.5s ease-in-out`;
            });
        });   
    });
}

const navSlide = () => {
    const logo = document.querySelector('.logo');
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.primary-navigation');
    const navLinks = document.querySelector('.nav-links');
    const navLinksLi = document.querySelectorAll('.nav-links li');

    burger.addEventListener('click', () => {
        //Toggle Nav
        navLinks.classList.toggle('nav-link-active');
        nav.classList.toggle('nav-active');
        /* toggleMultiple(nav, 'nav-link-active', 'hidden'); */

        //Animate Liks
        navLinksLi.forEach((link, index) => {
            if(link.style.animation){
                link.style.animation = '';
            } else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.3}s`;
            }
        });
        
        //Burger animation
        burger.classList.toggle('toggle');
    });

    burger.addEventListener('mouseenter', () => {
        //Toggle Nav
        navLinks.classList.toggle('nav-link-active');
        nav.classList.toggle('nav-active');

        //Animate Liks
        navLinksLi.forEach((link, index) => {
            if(link.style.animation){
                link.style.animation = '';
            } else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.3}s`;
            }
        });
        //Burger animation
        burger.classList.toggle('toggle');
    });

}

navSlide();
cardFade();

/* Cursor */

let mouseCursor = document.querySelector(".cursor");
let links = document.querySelectorAll('a');

window.addEventListener('mousemove', cursor);

function cursor(e){
    mouseCursor.style.top = e.pageY + 'px';
    mouseCursor.style.left = e.pageX + 'px';
}

links.forEach(link => {
    link.addEventListener('mouseover', () => {
        mouseCursor.classList.add('link-grow');
    });

    link.addEventListener('mouseleave', () => {
        mouseCursor.classList.remove('link-grow');
    });
});
