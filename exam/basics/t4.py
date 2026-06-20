def dates(met: str):
    dates = met.split(', ' )
    print(dates)
    selected = list()

    for day in dates:
        d=day.split(':')
        print(f"day: {d}")
        
        if int(d[1])<25 and int(d[1])>10 and int(d[2])<21:
            selected.append(d[0])
            #print(d)

    print(selected)

    # вернуть подходящих дней нет

    return selected


phone_number = "26:10:10, 27:8:0, 28:12:20, 29:14:15, 30:18:10"

refined=dates(phone_number)    

print(refined)

