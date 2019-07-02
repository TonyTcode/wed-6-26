user_input = ""
user_input2 = ""

while user_input != "q":
  user_input = input("Enter your name: ")
  user_input2 = input("Why do you like progamming: ") 
  
  if user_input != "q":
    with open("guest.txt", "a") as file_guest:
      guests = file_guest.write(user_input)

  if user_input2 != "q":
    with open("guest.txt", "a") as file_guest2:
      guest_reason = file_guest2.write(user_input2)




#code to write into a file while not deleting the previous text

#user_input = input("Enter your name: ")

#with open("guest.txt", "a") as file_guest:
    #guests = file_guest.write(user_input)

#print(guests)