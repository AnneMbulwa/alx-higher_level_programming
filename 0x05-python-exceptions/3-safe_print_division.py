#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        results = a / b
    except (ZeroDivisionError, FloatingPointError):
        results = None
    finally:
        print("Inside result: {}".format(results))
    return (results)
