#!/usr/bin/node
const [arg1, arg2] = process.argv.slice(2).map(Number);

function add(a, b) {
    return a + b;
}
console.log(add(arg1, arg2));
