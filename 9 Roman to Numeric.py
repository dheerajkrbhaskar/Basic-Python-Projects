def roman2num(roman):
    num = 0
    dict1 = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    for i in range(len(roman)-1):
        if dict1.get(roman[i]) < dict1.get(roman[i+1]):
            num -= dict1.get(roman[i])
        else:
            num += dict1.get(roman[i])

    num += dict1.get(roman[-1])
    return num

r_num = "MDCXXVII"
print(roman2num(r_num))

