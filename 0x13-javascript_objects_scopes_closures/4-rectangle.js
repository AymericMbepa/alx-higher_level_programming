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

    rotate() {
	[this.width, this.height] = [this.height, this.width];
    }

    double() {
	[this.width, this.height] = [2 * this.width, 2 * this.height];
    }
}

module.exports = Rectangle;
