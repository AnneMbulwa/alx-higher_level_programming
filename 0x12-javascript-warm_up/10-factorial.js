#!/usr/bin/node
function factorial(nums) {
	if (isNaN(nums) || nums <= 1) {
		return 1;
	} else {
		return nums * factorial(nums - 1);
	}
}

let w = process.argv[2];
let z = parseInt(w);

console.log(factorial(z));
