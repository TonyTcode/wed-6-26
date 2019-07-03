email = open("email.txt").read().split()


def remove(email): 
    final_list = [] 
    for index in email: 
        if index not in final_list: 
            final_list.append(index) 
    return final_list



print(remove(email))