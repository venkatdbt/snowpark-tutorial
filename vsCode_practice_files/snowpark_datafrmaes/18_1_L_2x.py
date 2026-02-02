def calculate_bonus(salary:int):
    if salary<=20000:
        return salary*0.05
    elif 2000<salary<24000:
        return salary*0.07
    else:
        return salary*0.1