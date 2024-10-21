// Variables

const name = "John"
const age = 30;
const likes = "tech, it, computers, code"
console.log(typeof name);
console.log(typeof 30.5);
console.log(typeof null);
console.log(typeof undefined);

console.log(`My name is ${name} and I am ${age}`);
console.log(name.length);
console.log(name.toUpperCase());
console.log(name.substring(2,3).toUpperCase());
console.log(likes.split(", "));

// Arrays

const numbers = new Array(1,2,3,4,5);
console.log(numbers);

const fruits = ["apples", "bananas", "oranges"]
console.log(fruits[1]); // Prints "bananas"
fruits[3] = "grapes";
fruits.push("mangoes") // Adds value to end of array
fruits.unshift("lemons") // Adds value to beginning of array
console.log(fruits.indexOf("bananas"));

// Object literals

const person = {
	firstName: "John",
	lastName: "Smith",
	age: 30,
	hobbies: ["Piano", "computers", "fruits"],
	address: {
		street: "Main",
		city: "Vancouver",
		number: 30
	}
}

console.log(person.firstName, person.address.street, person.hobbies[2])

const {address: {city}} = person
console.log(city)

const todos = [
    {
        id:1,
        text: "take out trash",
        isCompleted: true
    },
    {
        id:2,
        text: "meeting",
        isCompleted: true
    },
    {
        id:3,
        text: "sleep",
        isCompleted: false
    },
];

console.log(todos[0].text)
const todoJSON = JSON.stringify(todos);
console.log(todoJSON)

// Can we access object items with bracket notation?
console.log(person["lastName"]);
const item = "lastName";
console.log(person[item]); // Yes, we can

// Loops

// <for> loops

for(let i = 0; i < 10; i++){
	console.log(i);
}

// For loop over an array index
for(let i = 0; i < fruits.length; i++) {
    console.log(fruits[i])
}

// For loop with increments inside loop
for(let i = 0; i < 35; i++){
	console.log(i);
    i += 10;
}

// For loop without increment
for(let i = 0; i < 35;){
	console.log(`${i} is the current value`);
    i += 10;
}

// Breaking out of a for loop
for(let i = 0; i <= 10; i+= 2) {
    if (i == 6) {
        break;
    }
    console.log(i)
}

// For-in loop to iterate over enumerable keys of object
// It will return the _key_ of a dict...
console.log("For..in loop over object")
for(let key in person) {
    console.log(key);
}

// ...or the index of the array
console.log("For..in loop over array")
for(let key in fruits) {
    console.log(key)
}

// The two above means we need to reference the original object to find the value by indexing into it:
console.log("For..in loop over array with indexing")
for(let key in fruits) {
    console.log(fruits[key])
}

// For-of loop to iterate over _items_ in a collection
// Used to avoid the example above and get values without indexing
console.log("For..of loop over iterable")
for(let fruit of fruits) {
    console.log(fruit)
}

// An _object_ is not iterable, and thus for-of loops won't work
// for(let key of person) {
//     console.log(key)
// }

// While loop
console.log("While loop")
let i = 0;
while(i < 10) {
    console.log(i)
    i++;
}

// Higher order array methods
// foreach calls the callback function _once_ per item in the array
// thus it can be used to iterate over the array
console.log("forEach method")
todos.forEach(function(todo) {
    console.log(todo)
    console.log(todo.text)
});

// map calls the callback function _once_ per item in the array
// thus it can be used to iterate over the array
// note that map _returns an array_ of _just the item_
console.log("map method")
const todoText = todos.map(function(todo) {
    console.log(todo)
    console.log(todo.text)
    return todo.isCompleted === true
});
console.log(todoText)


// filter calls the callback function _once_ per item in the array
// thus it can be used to iterate over the array
// note that filter _returns an array_ that contains the filter condition
console.log("filter method")
const todoCompleted = todos.filter(function(todo) {
    console.log(todo)
    console.log(todo.isCompleted)
    return todo.isCompleted === true
});
console.log(todoCompleted)

// Conditionals

const x = 10;
const y = "10";

if(x == 10) {
    console.log("x is 10")
}

if(x == y) {
    console.log("matches value")
}

if(x === 10) {
    console.log("matches value AND type")
}

if(x === y) {
    console.log("this will not print")
} else if(x === 11) {
    console.log("this could print if the _value_ of x changes")
} else {
    console.log("This prints")
}

// Logical OR

if(x === y || x == y) {
    console.log("Demonstrating logical OR")
}

if(x === y | x == y) {
    console.log("Demonstrating _bitwise_ OR")
}

// Logical AND

if(x === 10 && x == y) {
    console.log("Demonstrating logical AND")
}

if(x === 10 & x == y) {
    console.log("Demonstrating _bitwise_ AND ")
}

// Ternary operator

const t = 12;
// if condition THEN (?) value, ELSE (:) other value
const color = t > 10 ? "red" : "blue";
console.log(color)

// Switches

switch(color) {
    case "red":
        console.log(`color is ${color}`);
        break;
    case "blue":
        console.log(`color is ${color}`);
        // break;
    default:
        console.log(`color is unknown.`);
}


// Functions
function addNums(num1 = 1, num2 = 1) {
    return num1 + num2
}

console.log(addNums(5,5))
// Arrow function
const addArrowNums = (num1 = 1, num2 = 1) => num1 + num2
addArrowNums(2,3)

todos.forEach((todo) => console.log(todo.text + "MEOW"))

// Objects and OOP

// A constructor function
function Person(firstName, lastName, dob) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.dob = new Date(dob); // Using a constructor to create a date "class"

	// Adding methods
	this.getFullName = function() {
		return `${this.firstName} ${this.lastName}`
	}
}

Person.prototype.getBirthYear = function() {
    return this.dob.getFullYear()
}

// Instantiate object
const person1 = new Person("James", "Smith", "4-2-1990");
console.log(person1.getFullName())
console.log(person1.getBirthYear())


// Classes

class Human {
    constructor(firstName, lastName, dob) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.dob = new Date(dob);
    }

    getFullName() {
		return `${this.firstName} ${this.lastName}`
	}

    getBirthYear() {
        return this.dob.getFullYear()
    }
}

const human1 = new Human("James", "Smith", "4-2-1990");
console.log(human1.getFullName())
console.log(human1.getBirthYear())