var a = "test";

console.log(a);


// will be undefined because variable is initialized but defined after usage
console.log(b);

var b = "test";

for (var i = 0; i < 5; i++) {
    console.log(i);
}

function add(a, b) {
    return a + b;
}

const sub = (a, b) => {
    return a - b;
};

function mul(a, b) {
    return a * b;
}

const div = (a, b) => {
    return a / b;
};


const bigger = (a, b) => {
    return a > b ? a : b;
};

console.log("Your results:");

console.log(add(2, 3)); // 5
console.log(sub(5, 2)); // 3
console.log(mul(3, 4)); // 12
console.log(div(10, 2)); // 5
