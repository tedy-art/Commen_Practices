def even_odd_number():
    start = int(input("Start with : "))
    stop = int(input("Stop with : "))
    even_number = []
    odd_number = []
    
    for i in range(start, stop+1):
        if i%2 == 0:
            even_number.append(i)
        else:
            odd_number.append(i)
    print('even_numbers : ',even_number)
    print('Odd number : ', odd_number)
    
even_odd_number()