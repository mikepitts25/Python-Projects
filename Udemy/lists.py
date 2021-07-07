available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse pad",
                   "hdmi cable",
                   "dvd drive"]

current_choice = "-"
computer_parts = []
valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]


def menu():
    print("Please add options from the list below: ")
    for number, part in enumerate(available_parts):
        print("{0}:\t{1}".format(number + 1, part))


while current_choice != '0':
    if current_choice in valid_choices:
        print("Adding {} to the list".format(available_parts[int(current_choice) - 1]))
        computer_parts.append(available_parts[int(current_choice) - 1])
    else:
        menu()
        # if current_choice == '1':
        #     computer_parts.append("computer")
        # elif current_choice == '2':
        #     computer_parts.append("monitor")
        # elif current_choice == '3':
        #     computer_parts.append("keyboard")
        # elif current_choice == '4':
        #     computer_parts.append("mouse")
        # elif current_choice == '5':
        #     computer_parts.append("mouse pad")
        # elif current_choice == '6':
        #     computer_parts.append("hdmi cable")

    current_choice = input()

print("Your cart contains: " + str(computer_parts))
