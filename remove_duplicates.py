def remove(names): 
    final_list = [] 
    for index in names: 
        if index not in final_list: 
            final_list.append(index) 
    return final_list


names = ["Alex", "John", "Mary", "Steve", "John", "Steve"]

print(remove(names))