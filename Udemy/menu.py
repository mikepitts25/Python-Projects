choice = None


def menu():
      while True:
            choice = input("Please choose your option form the list below:\n"
                             "1.\tLearn Python\n"
                             "2.\tLearn Java\n"
                             "3.\tGo swimming\n"
                             "4.\tHave dinner\n"
                             "5.\tGo to bed\n"
                             "0.\tExit\n")
            if choice.isdigit() == False:
                continue
            elif 0 < int(choice) <= 5:
                  print("You chose {}.".format(choice))
            elif int(choice) == 0:
                  print("Goodbye")
                  break
            else:
                  continue
# try:
#     menu()
# except Exception:
#     print("Invalid entry. Please try again.")
menu()
