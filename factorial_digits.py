def fact_digits(n):
    fac_sum = 0
    while n:
        fac = 1
        digit = n % 10
        n //= 10
        for num in range(digit, 0, -1):
            fac *= num
        fac_sum += fac
    return fac_sum


print(fact_digits(101) == 3)
print(fact_digits(111) == 3)
print(fact_digits(145) == 145)
print(fact_digits(999) == 1088640)