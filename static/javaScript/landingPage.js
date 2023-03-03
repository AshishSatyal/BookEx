const bookContainer = [...document.querySelectorAll('.book-container')];    // spreading selected div.book-caontainer...
const prevBtn = document.querySelector('.prev-btn');
const nextBtn = document.querySelector('.next-btn');

console.log(bookContainer);

// console.log(prevBtn);
bookContainer.forEach((book, i) => {
    let containerDimension = book.getBoundingClientRect();
    let containerWidth = containerDimension.width;
    
    prevBtn.addEventListener('click', () => {
        book.scrollLeft -= containerWidth;
    })
    
    nextBtn.addEventListener('click', () => {
        book.scrollLeft += containerWidth;
    })
})