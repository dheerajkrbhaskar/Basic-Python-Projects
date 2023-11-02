

def alarm(aHour, aMin):
    import datetime as D1
    while True:
        now = D1.datetime.now()
        current_Hour = now.strftime("%H")
        current_Min = now.strftime("%M")

        # if aHour == current_Hour:
        #     if aMin == current_Min:
        #         print("congrats! time matches")
        #         break

        if aHour == current_Hour and aMin == current_Min:
            print("congrats! time matches")
            break
t_input = input("Enter alarm time(HH:MM) 24H: ")
timelist = t_input.split(":")
Hr, Min = timelist[0], timelist[1]
alarm(Hr, Min)