#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    for i in range(1, 4):
        if i > a:
            break
        try:
            result += a ** b / i
        except Exception as err:
            print("Exception:", err, file=sys.stderr)
            return None
    return result
