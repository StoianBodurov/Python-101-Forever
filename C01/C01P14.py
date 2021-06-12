def is_prime(n):
    if n < 2:
        return False

    half_num = n // 2
    for num in range(2, half_num + 1):
        if n % num == 0:
            return False
    return True


def is_even(n):
    return n % 2 == 0


def goldbach(n):
    list_of_tuples = []

    if is_even(n):
        for j in range(2, n // 2 + 1):
            if is_prime(j):
                for k in range(2, n + 1):
                    if is_prime(k):
                        if j + k == n:
                            list_of_tuples.append((j, k))
        if list_of_tuples:
            return list_of_tuples

        return None

    return None