import os 
os.system("clear")

# expenses = [10.50, 8, 5, 15, 20, 5, 3]
# total = sum(expenses)

# range(0, 7, 1)

# print("You spend $", total, sep="")

total = 0
expenses = []
num_expenses = int(input("Enter # of expenses:\n"))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expense:\n")))

total = sum(expenses)

print("You spend $", total, sep="")