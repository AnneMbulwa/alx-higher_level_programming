#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_store = []
    results = 0

    for a in range(0, list_length):
        try:
            results = my_list_1[a] / my_list_2[a]
        except ZeroDivisionError:
            print("division by 0")
            new_store.append(0)
        except TypeError:
            print("wrong type")
            new_store.append(0)
        except IndexError:
            print("out of range")
            new_store.append(0)
        finally:
            pass
        new_store.append(results)
    return (new_store)
