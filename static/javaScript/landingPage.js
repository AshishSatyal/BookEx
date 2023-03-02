// in future we will be fetching JSON 
const bookDetails = [
       {
        img: "book_img_1.png",
        title: "your heart is the sea",
        author: "Nikita Gill"
       },
       {
        img: "book_img_2.png",
        title: "little black book",
        author: "Otecha Uwagba"
       },
       {
        img: "book_img_3.png",
        title: "guess how much i love you in the autumn",
        author: "Sam McBratney"
       },
       {
        img: "book_img_4.png",
        title: "the north and north wales independent coffee guide",
        author: "Anonymous"
       },
       {
        img: "book_img_5.png",
        title: "the catcher in the rye",
        author: "Ld Salinger"
       },
       {
        img: "book_img_6.png",
        title: "your soul is a river",
        author: "Nikita Gill"       
        },
       {
        img: "book_img_7.png",
        title: "Lagom",
        author: "Manehbkar Khnta"
       },
       {
        img: "book_img_1.png",
        title: "your heart is the sea",
        author: "Nikita Gill"
       }
]

// map over every book objects from bookDetails array and return new array with their respective properties...
bookDetails.map(book => {
    const bookCard = document.createElement("div");
    bookCard.className = "book-card";
    const bookLink = document.createElement("a");
    bookLink.id = "book-link";
    bookLink.title = book.title;
 
    const bookImg = document.createElement('img');
    bookImg.className = "book-img";
    bookImg.src = `../../static/images/${book.img}`;

    const title = document.createElement('p');
    title.className = "title";
    title.textContent = book.title;

    const author = document.createElement('i');
    author.className = "author";
    author.textContent = "- " + book.author;

    bookLink.append(bookImg, title);
    bookCard.append(bookLink, author);
    
    // every book-cards are stored inside div.book-container element...
    return document.querySelector('.book-container').appendChild(bookCard);
})

const bookContainer = [...document.querySelectorAll('.book-container')];    // spreading selected div.book-caontainer...

const prevBtn = document.querySelector('.prev-btn');
const nextBtn = document.querySelector('.next-btn');

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