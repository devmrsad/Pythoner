from math import floor
try:
    questions_count = int(input("Enter the questions count: "))
    correct_answers = int(input("Enter the count of your correct answers: "))
    wrong_answers = int(input("Enter the count of your wrong answers: "))
except:
    exit("The input values should be numeric!")

# wrong data detection
if correct_answers + wrong_answers > questions_count:
    exit(f"you cannot have answered {correct_answers + wrong_answers} questions out {questions_count}!")

percentage = (((3 * correct_answers) - wrong_answers) / (3 * questions_count)) * 100
round_percentage = floor(percentage)

print(f"You have answered {max(0, round_percentage)}% of the questions.")