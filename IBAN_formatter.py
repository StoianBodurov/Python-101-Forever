def iban_formatter(iban):
    result = []
    count = 0

    for el in iban:
        if el.isspace():
            continue
        count += 1
        result.append(el)
        if count == 4:
            result.append(" ")
            count = 0
    return ''.join(result)


print(iban_formatter("BG80BNBG96611020345678") == "BG80 BNBG 9661 1020 3456 78")
print(iban_formatter("BG80 BNBG 9661 1020 3456 78") == "BG80 BNBG 9661 1020 3456 78")
print(iban_formatter("BG14TTBB94005362446381") == "BG14 TTBB 9400 5362 4463 81")
print(iban_formatter("BG91UNCR70001864961754") == "BG91 UNCR 7000 1864 9617 54")