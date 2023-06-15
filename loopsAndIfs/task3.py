
listNames = []
listNamesLower = []
listNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = 0
allNum = 0
oddNum = 0
evenNum = 0

for x in range(10):
    print("Hello")
#
# for y in range(5):
#     listNames.append(input("Please enter your name"))
#
# print(listNames)
#
# for name in listNames:
#     listNamesLower.append(name.lower())
#
# print(listNamesLower)
#
#
for num in listNum:
    if num % 2 == 0:
        print(num)


while number <101:
    allNum += number
    if number % 2 != 0:
        evenNum += number
    else:
        oddNum += number
    number += 1
print(f"Sum of all numbers: {allNum}")
print(f"Sum of even numbers: {evenNum}")
print(f"Sum of odd numbers: {oddNum}")