my_array = [0, 1, 2, 3, 5, 6, 7, 8, 9]    
correct_total = 45

def missing_num():

    counter = 0

    for item in range(0, len(my_array)):
        counter += my_array[item]
    return counter

missing = correct_total - missing_num() 
print(missing)