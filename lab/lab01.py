def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    if k > 0:
        falling = n
        while k > 1:
            falling = falling * (n-1)
            n -= 1
            k -= 1
        return falling
    elif k == 0:
        return 1
    else:
        print("k should not be smaller than 0")
    """if k == 0:
        return 1
    return reduce(mul, range(n, n-k, -1))"""


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    digit = 1
    sum_digit = 0
    while y - 10 ** digit >= 0:
        digit += 1
    while digit > 0:
        sum_digit = sum_digit + y // 10 ** (digit - 1)
        y = y % 10 ** (digit - 1)
        digit -= 1
    return sum_digit
    """ans = 0
    while y:
        ans += y % 10
        y //= 10
    return ans"""


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    if n // 10 == 0:
        return False
    while n:
        last_digit = n % 10
        n //= 10
        if last_digit == 8 == (n % 10):
            return True
    return False


