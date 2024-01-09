#!/usr/bin/node

exports.esrever = function (list) {
	const Num = [];
	for (let a = list.length - 1; a >= 0; a--) {
		Num.push(list[a]);
	}
	return (Num);
};
