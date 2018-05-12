

def _is_multiple(value, mod):
    return (value % mod) == 0


def fizz_buzz(value):
    if _is_multiple(value, 3) and _is_multiple(value, 5):
        return "FizzBuzz"
    if _is_multiple(value, 3):
        return "Fizz"
    if _is_multiple(value, 5):
        return "Buzz"
    return str(value)
