document.addEventListener('DOMContentLoaded',function () {
    const carouselContainer = document.querySelector('.hero-carousel');
    const slides = document.querySelector('carousel-slide');

    let currentIndex = 0;

    function updateCarousel() {
        carouselContainer.style.transform = `translateX(${-currentIndex * 100}%)`;
    }

        function nextSlide(){
    currentIndex = (currentIndex + 1) % slides.length;
    updateCarousel();
        }

        function prevSlide(){
    currentIndex = (currentIndex - 1 + slides.length) % slides.length;
    updateCarousel();
        }

        setInterval(nextSlide,3000)

        //keyboard navigation
        document.addEventListener('keydown', function (event){
            if (event.key === 'ArrowLeft'){
                prevSlide();
            }else if (event.key === 'ArrowRight') {
                nextSlide();
            }
        })
})