def is_prime(num):

    if num == 1:
        return False
    elif num == 2:
        return True

    for number in range(2, num):
        if num % number == 0:
            return False
    return True


print(is_prime(2))