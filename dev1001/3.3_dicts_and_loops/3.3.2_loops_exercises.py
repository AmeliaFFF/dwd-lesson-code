def input_within_range():
    MIN_VALUE = 1
    MAX_VALUE = 100

    user_input = 3

    while user_input < MIN_VALUE or user_input > MAX_VALUE:
        user_input = int(input("Please enter a number between 1 and 100: "))
        if user_input < MIN_VALUE:
            print("ERROR: That value is too low!")
        if user_input > MAX_VALUE:
            print("ERROR: That value is too high!") 

    return user_input