// import { sliderControl } from "./landingPage";  // importing sliderControl function from landingPage.js file

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

// checking browser support...
if ('content' in document.createElement('template')) {
    const bookContain = [...document.querySelectorAll(".book-container")];
    console.log(bookContain)

    bookContain.forEach(itemContainer => {
        bookDetails.map(book => {
            const bookTemplate = document.querySelector(".book-template");
            console.log(bookTemplate)
            // Clone the new book card and insert it into the book container of a slider...
                const clone = bookTemplate.content.cloneNode(true);
                let bookLink = clone.querySelector('.book-link');
                let bookImg = clone.querySelector('.book-img');
                let bookTitle = clone.querySelector('.book-title');
                let bookAuthor = clone.querySelector('.author');
                let addToCartBtn = clone.querySelector('.add-to-cart-btn');
                
                bookImg.src = `../../static/images/${book.img}`;
                bookTitle.textContent = book.title;
                bookAuthor.textContent = book.author;
                bookLink.title = book.title.toUpperCase();
                
                // console.log(clone)
                // console.log(bookImg, bookTitle, bookAuthor, addToCartBtn)
                // console.log(bookTemplate[0].textContent);
                    itemContainer.appendChild(clone);
        })
    })

    const bookContainer = [...document.querySelectorAll('.book-container')];    // spreading selected div.book-caontainer...
    
    const prevBtn = [...document.querySelectorAll('.prev-btn')];
    const nextBtn = [...document.querySelectorAll('.next-btn')];
    
    // console.log(prevBtn);
    bookContainer.forEach((book, i) => {
        let containerDimension = book.getBoundingClientRect();
        let containerWidth = containerDimension.width;
        
        prevBtn[i].addEventListener('click', () => {
            book.scrollLeft -= containerWidth;
        })
        
        nextBtn[i].addEventListener('click', () => {
            book.scrollLeft += containerWidth;
        })
    })
} else {
    console.log("template not found!");
}