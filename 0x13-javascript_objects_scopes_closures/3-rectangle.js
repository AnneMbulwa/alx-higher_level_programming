#!/usr/bin/node
module.exports = class Rectangle {
	constructor (w, h) {
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h;
		} else {
			this.width = 0;
			this.height = 0;
		}
	}
	print () {
		for (let a = 0; a < this.height; a++) {
			console.log('X'.repeat(this.width));
		}
	}
};
