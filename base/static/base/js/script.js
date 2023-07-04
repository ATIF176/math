// ---
const hamMenuBtn = document.querySelector('.header__main-ham-menu-cont')
const smallMenu = document.querySelector('.header__sm-menu')
const headerHamMenuBtn = document.querySelector('.header__main-ham-menu')
const headerHamMenuCloseBtn = document.querySelector(
  '.header__main-ham-menu-close'
)
const headerSmallMenuLinks = document.querySelectorAll('.header__sm-menu-link')

hamMenuBtn.addEventListener('click', () => {
  if (smallMenu.classList.contains('header__sm-menu--active')) {
    smallMenu.classList.remove('header__sm-menu--active')
  } else {
    smallMenu.classList.add('header__sm-menu--active')
  }
  if (headerHamMenuBtn.classList.contains('d-none')) {
    headerHamMenuBtn.classList.remove('d-none')
    headerHamMenuCloseBtn.classList.add('d-none')
  } else {
    headerHamMenuBtn.classList.add('d-none')
    headerHamMenuCloseBtn.classList.remove('d-none')
  }
})

for (let i = 0; i < headerSmallMenuLinks.length; i++) {
  headerSmallMenuLinks[i].addEventListener('click', () => {
    smallMenu.classList.remove('header__sm-menu--active')
    headerHamMenuBtn.classList.remove('d-none')
    headerHamMenuCloseBtn.classList.add('d-none')
  })
}

// ---
const headerLogoConatiner = document.querySelector('.header__logo-container')

headerLogoConatiner.addEventListener('click', () => {
  location.href = 'index.html'
})

// Script for carousel
document.addEventListener('DOMContentLoaded', function() {
  const carouselContainer = document.querySelector('.carousel-container');
  const carouselSlides = Array.from(document.querySelectorAll('.carousel-slide'));
  const carouselPrev = document.querySelector('.carousel-prev');
  const carouselNext = document.querySelector('.carousel-next');
  const carouselPagination = document.querySelector('.carousel-pagination');

  let currentSlide = 0;
  const slideWidth = carouselSlides[0].offsetWidth;

  function goToSlide(index) {
    carouselContainer.style.transform = `translateX(-${slideWidth * index}px)`;
    carouselPagination.querySelector('.active').classList.remove('active');
    carouselPagination.querySelectorAll('span')[index].classList.add('active');
    currentSlide = index;
  }

  function goToNextSlide() {
    if (currentSlide === carouselSlides.length - 1) {
      goToSlide(0);
    } else {
      goToSlide(currentSlide + 1);
    }
  }

  function goToPrevSlide() {
    if (currentSlide === 0) {
      goToSlide(carouselSlides.length - 1);
    } else {
      goToSlide(currentSlide - 1);
    }
  }

  function createPagination() {
    carouselSlides.forEach((slide, index) => {
      const dot = document.createElement('span');
      dot.addEventListener('click', () => goToSlide(index));
      carouselPagination.appendChild(dot);
    });
    carouselPagination.querySelector('span').classList.add('active');
  }

  carouselNext.addEventListener('click', goToNextSlide);
  carouselPrev.addEventListener('click', goToPrevSlide);

  createPagination();

  setInterval(goToNextSlide, 5000); // Automatic slide every 5 seconds
});

