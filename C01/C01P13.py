def multiplay(nums):
    m = 1
    for el in nums:
        m *= el[0] ** el[1]
    return m


def prime_factorization(n_start):
    n = n_start
    nums = []

    for num in range(2, n + 1):
        count = 0
        number = num
        if multiplay(nums) == n_start:
            break

        while n % num == 0:
            n /= num
            count += 1
        if count:
            nums.append((number, count))

    return nums