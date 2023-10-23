#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_store = []
    results = 0

    for a in range(0, list_length):
        try:
            results = my_list_1[a] / my_list_2[a]
        except ZeroDivisionError:
            results = 0
            print("division by 0")
        except TypeError:
            results = 0
            print("wrong type")
        except IndexError:
            results = 0
            print("out of range")
        finally:
            pass
        new_store.append(results)
    return new_storie
