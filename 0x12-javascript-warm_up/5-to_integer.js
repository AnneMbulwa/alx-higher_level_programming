#!/usr/bin/node
let x = parseInt(process.argv[2]);
if (!isNaN(x))
	console.log(`My number: ${x}`);
else
	console.log("No argument");
