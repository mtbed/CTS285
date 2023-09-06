## VARIABLES
keep_going = True
select_list = "1. Add \n2. Subtract \n3. Divide \n4. Multiply \n5. Quit \n\nEnter a number 1-5:"

print("Welcome to my calculator.\n\n")
print(select_list)

choice = int(input())

while choice < 1 or choice > 5:
  print("\nPlease make a valid selection.\n\n")
  print(select_list)
  choice = int(input())

if choice >= 1 and choice <= 5:
  keep_going = True

while keep_going:
  if choice == 1:
    print("\nAdding \n")
    print("Enter a number:")
    num1 = int(input())
    print("\nEnter a number:")
    num2 = int(input())

    print("\n\nRESULT:\n")
    result = num1 + num2
    print(num1, " + ", num2, " = ", result)
    print("\n")

    print(select_list)
    choice = int(input())

  if choice == 2:
    print("\nSubtracting \n")
    print("Enter a number:")
    num1 = int(input())
    print("\nEnter a number:")
    num2 = int(input())

    print("\n\nRESULT:\n")
    result = num1 - num2
    print(num1, " - ", num2, " = ", result)
    print("\n")

    print(select_list)
    choice = int(input())

  if choice == 3:
    print("\nDividing \n")
    print("Enter a number:")
    num1 = int(input())
    print("\nEnter a number:")
    num2 = int(input())

    print("\n\nRESULT:\n")
    result = num1 / num2
    print(num1, " / ", num2, " = ", result)
    print("\n")

    print(select_list)
    choice = int(input())

  if choice == 4:
    print("\nMultiplying \n")
    print("Enter a number:")
    num1 = int(input())
    print("\nEnter a number:")
    num2 = int(input())

    print("\n\nRESULT:\n")
    result = num1 * num2
    print(num1, " * ", num2, " = ", result)
    print("\n")

    print(select_list)
    choice = int(input())

  if choice == 5:
    print("Quitting...")
    keep_going = False
