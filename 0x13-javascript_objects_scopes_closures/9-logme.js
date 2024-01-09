#!/usr/bin/node
let a = 0;/*counter*/

exports.logMe = function (item) { 
	console.log(`${a}: ${item}`);
	a++; 
};
