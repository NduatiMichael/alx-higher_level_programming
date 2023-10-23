#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            quotient = 0
            if i < len(my_list_1):
                dividend = my_list_1[i]
            else:
                dividend = 0
            if i < len(my_list_2):
                divisor = my_list_2[i]
                if divisor != 0:
                    quotient = dividend / divisor
                else:
                    print("division by 0")
            else:
                print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            result.append(quotient)
    return result
