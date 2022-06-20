data = []
r = 0
while True:
    userInput = input("Masukan angka: ")
    if userInput == 'n':
        break
    r += 1
    data.append(userInput)

total = 0
for nilai in data:
    total += int(nilai)

total = total / r
print(total)
