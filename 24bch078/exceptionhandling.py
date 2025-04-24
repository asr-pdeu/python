#11.1

def get_integer_input():

    while True:

        user_input = input("Please enter an integer: ")

        try:

            user_int = int(user_input)

            print(f"You entered the integer: {user_int}")

            return user_int

        except ValueError:

            print("Error: That was not a valid integer. Please try again.")

 

 

get_integer_input()

 

 
