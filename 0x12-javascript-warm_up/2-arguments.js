#!/usr/bin/node
let x = process.argv.length - 2;
if (x === undefined) {
	console.log("No argument");
} else  if (x === 1) {
	console.log("Argument found");
} else 
	console.log("Arguments found");
