def sum_of_digits(n):
    n = abs(n)
    sum_of_digit = 0
    while n:

        digit = n % 10
        n //= 10
        sum_of_digit += digit
    return sum_of_digit


print(sum_of_digits(1325132435356) == 43)
print(sum_of_digits(123) == 6)
print(sum_of_digits(6) == 6)
print(sum_of_digits(-10) == 1)