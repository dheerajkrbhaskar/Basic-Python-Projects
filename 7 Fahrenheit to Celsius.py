def F2C(f):

    c = (f-32) * 5/9
    return c
def C2F(c):
    f = (c*9/5) + 32
    return f

print(F2C(98.6))
print(C2F(37))