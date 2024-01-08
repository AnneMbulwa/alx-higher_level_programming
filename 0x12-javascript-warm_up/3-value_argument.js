#!/usr/bin/node

let x = process.argv[2];
if (x === undefined)
	console.log('No argument');
else
	console.log(x);
