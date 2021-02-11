// const list = [1, 2, 3, 4, 5]
// console.log(list[0])

// const foodInfo = {
//     name: "Cheese",
//     shelfLife: "20231111",
//     newProduct: false,
//     salesStore: ["GS market", "E mart", "CU"]
// }
// console.log(foodInfo['salesStore'][0])


// function hello() {
//     console.log('hello :)')
// }
// hello();


// function sayHello(parameter) {
//     console.log('Hello!',parameter);
// }
// sayHello('seob');


// function sayHello(name, age) {
//     console.log(`Hello ${name} you are ${10} years old`);
// }
// sayHello('seob');


// function sayHello(name, age) {
//     return `Hello ${name} you are ${10} years old`
// }
// const hiseob = sayHello('seob', 10)
// console.log(hiseob)



// * object 활용 * 
// const calculator = {
// 		plus: function(a, b) {
// 				return a + b; 
// 		},
// 		minus: function(a, b) {
// 				return a - b;
// 		}
// }

// const plus = calculator.plus(5, 5)
// const minus = calculator.minus(10, 5)
// console.log(plus)
// console.log(minus)



// const title = document.getElementById("title");
// console.log(title)



// function handleResize() {
//     console.log("I have been resized");
// }
// window.addEventListener("resize", handleResize);


const title = document.getElementById("title");
const any = document.getElementById("any");
console.log(any);
function handleClick() {
    title.style.color = 'blue';
}
function smallWordClick() {
    any.style.color = "darkred";
}
title.addEventListener("click", handleClick);
any.addEventListener("click", smallWordClick);



function checkMyAge(age) {
    if (age <= 19) {
        console.log('10대');
    } else if (age >= 20 && age < 40) {
        console.log('청년');
    } else {
        console.log('중년 이상')
    }
}
const myAge = prompt("몇 살");    // prompt는 js의 오래된 문법으로 이젠 잘 쓰지 않음.
checkMyAge(myAge);