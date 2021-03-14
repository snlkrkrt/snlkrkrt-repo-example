odd_numbers = list(range(1,10,2))
even_numbers = list(range(0,10,2))
combining_list = odd_numbers + even_numbers
new_list = [i*2 for i in combining_list]
for k in new_list:
    print(type(k))