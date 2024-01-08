#!/usr/bin/node
let size = parseInt(process.argv[2]);

if (!isNaN(size)){
	for (let a = 0; a < size; a++)
	{
		let row = '';
		for (let b = 0; b < size; b++)
			row += 'X';
		console.log(row);
	}
} else {
	console.log('Missing size');
}
