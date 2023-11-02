
while True:
    user_input = input("Enter your phrase... ")
    word = user_input.split()
    a = ''
    for x in word:
        a = a + str(x[0]).upper()

    print(a)
    press = int(input("Press o to end this program"))
    if press == 0:
        break

