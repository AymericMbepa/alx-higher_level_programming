#!/usr/bin/node
const num = parseInt(process.argv[2]);
let square = '';

if (num) {
    for (let i = 0; i < num; i++) {
	for (let j = 0; j < num; j++) {
	    square += 'X';
	}
	if (i < num - 1){
	    square += '\n';
	}
    }
    console.log(square);
} else {
    console.log('Missing size');
}
