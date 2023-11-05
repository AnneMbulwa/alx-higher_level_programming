#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
        a = 10
        b = 5

        operators = ["+", "-", "*", "/"]

        for a in range(len(operators)):
            if operators[a] == "+":
                results = add(a, b)
            if operators[a] == "-":
                results = sub(a, b)
            if operators[a] == "*":
                results = mul(a, b)
            if operators[a] == "/":
                results = div(a, b)
            print("{} {} {}".format(a, operators[a], b, results))
