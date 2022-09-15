numerator = int(input("numerator: "))
denominator = int(input("denominator: "))

numbers = []

if denominator < numerator:
    for i in range(denominator):
        numbers.append(i+1)
else:
    for i in range(numerator):
        numbers.append(i+1)

numbers.pop(0)

dividables = []

for number in numbers:
    if numerator / number % 1 == 0 and denominator / number % 1 == 0:
        dividables.append(number)

print(f"{numerator}/{denominator}")
if dividables:
    print(dividables[-1])
    print(f"{int(numerator/ dividables[-1])}/{int(denominator / dividables[-1])}")
else:
    print(1)
    print(f"{numerator}/{denominator}")
