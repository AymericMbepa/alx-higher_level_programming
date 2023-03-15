#!/usr/bin/node
class Rectangle {
    constructor(w, h) {
	if (w > 0 && h > 0) {
	    this.width = w;
	    this.height = h;
	}
    }

    print() {
	let pr = '';
	for (let i = 0; i < this.height; i++) {
	    for (let j = 0; j < this.width; j++) {
		pr += 'X';
		if ((j === this.width - 1) && i < this.height - 1) {
		    pr += '\n';
		}
	    }
	}
	console.log(pr);
    }
}

module.exports = Rectangle;
