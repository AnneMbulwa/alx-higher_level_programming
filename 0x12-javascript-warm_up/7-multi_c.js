#!/usr/bin/node
let num = parseInt(process.argv[2]);
if (!isNaN(num))
	for (let a = 0; a < num; a++)
		console.log("C is fun");
else
	console.log("Missing number of occurrences");
