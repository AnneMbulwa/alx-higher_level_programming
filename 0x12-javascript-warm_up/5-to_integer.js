#!/usr/bin/node
let y = process.argv[2];
let x = parseInt(y);
if (isNaN(x) || y === undefined) {
	console.log('Not a number');
} else {
	console.log(`My number: ${x}`);
}
