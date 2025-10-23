first_number = int(float(input("Enter first number: ")))
second_number = int(input("Enter second number: "))


answer = first_number + second_number

print(f'The sum of both numbers is {answer}')



# ------ alternative 1
# try:
#     first_number = int(float(input("Enter first number: ")))
#     second_number = int(float(input("Enter second number: ")))
#     answer = first_number + second_number
#     print(f"The sum of both numbers is {answer}")
# except ValueError:
#     print("Please enter valid numbers.")


# ------ alternative 2
# def get_int(prompt):
#     while True:
#         try:
#             return int(input(prompt))
#         except ValueError:
#             print("Please enter an integer.")
#
# first_number = get_int("Enter first number: ")
# second_number = get_int("Enter second number: ")
#
# answer = first_number + second_number
# print(f"The sum of both numbers is {answer}")


