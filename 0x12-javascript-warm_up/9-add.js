#!/usr/bin/node
const k = process.argv[2];
const l = process.argv[3];

function add(a, b) {
	return (a + b);
}

console.log(add(parseInt(k), parseInt(l)));
