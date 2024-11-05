// Single element selector
console.log(document.getElementById('my-form'));
console.log(document.querySelector(".container"))

// Multiple Element
console.log(document.querySelectorAll(".item"))

// Looping through selections
const items = document.querySelectorAll(".item");
items.forEach((item) => console.log(item));

// DOM Manipulation
const ul = document.querySelector(".items")
// ul.remove();
// ul.lastElementChild.remove();
ul.firstElementChild.textContent = "hello";
ul.children[1].innerText = "Meow";
ul.lastElementChild.innerHTML = "<h1>MEOW!</h1>"

// Changing styles
const btn = document.querySelector(".btn");
btn.style.background = "red"

// Events
btn.addEventListener("click", (eventVar) => {
    eventVar.preventDefault();
    document.querySelector("#my-form").style.background = "#ccc"
    document.querySelector("body").classList.add('bg-dark');
    ul.lastElementChild.innerHTML = "<h1>Hello</h1>"
})

// btn.addEventListener("click", function(e) {
//     e.preventDefault();
//     console.log(e);
// })