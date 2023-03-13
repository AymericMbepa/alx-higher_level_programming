#!/usr/bin/node
const arg = parseInt(process.argv[2]);

function factorial(n) {
    if ((n === 0) || (n === 1)) {
	return 1;
    } else {
	return n * factorial(n - 1);
    }
}

if (!arg) {
    console.log(factorial(0));
} else {
    console.log(factorial(arg));
}
