#!/usr/bin/node
let yum = process.argv[2];
let num = parseInt(yum);
if (!isNaN(num)) {
	for (let a = 0; a < num; a++) {
		console.log('C is fun');
	}
} else {
	console.log('Missing number of occurrences');
}
