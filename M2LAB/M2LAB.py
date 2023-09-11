import random


num_1 = random.randint(1,10)
num_2 = random.randint(1,10)
operator_num = random.randint(1,4)
#correct_ans
amt_wrong = 0
#streak



if operator_num == 1:
    operator = "+"
    correct_ans = num_1 + num_2
elif operator_num == 2:
    operator = "-"
    correct_ans = num_1 - num_2
elif operator_num == 3:
    operator = "*"
    correct_ans = num_1 * num_2
elif operator_num == 4:
    operator = "/"
    correct_ans = num_1 / num_2
print("CALCULATOR\n\n")
print(correct_ans)

print()
print(num_1,operator,num_2)
user_ans = input("Answer: ")


if correct_ans == user_ans:
    print("NICE! FIRST TRY!")
 

print(user_ans)
