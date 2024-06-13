while True:
    selected_option = input("Please enter 'a', 'b', or 'c', or enter 'q' to quit: ")

    if selected_option == "a":
        print("You selected option 'a'!")
    elif selected_option == "b":
        print("You selected option 'b'!")
    elif selected_option == "c":
        print("You selected option 'c'!")
    elif selected_option == "q":
        print("You selected option 'q'! Quitting the menu!")
        break
    else:
        print("You selected an invalid option.")
