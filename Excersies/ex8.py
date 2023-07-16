numbers = [12, 75, 150, 180, 145, 525, 50]
# condition = num%5 == 0, num>150 ->skip-> next line, num>500->break

for number in numbers:
    if number > 500:
        break
    elif number > 150:
        continue
    elif number % 5 == 0:
        print(number)