text = input("Enter n (number of elements): ")

if "-" in text:
    print("Negative number is not allowed!")
elif not text.isdigit():
    print("Invalid input! Enter digits only.")
elif int(text) == 0:
    print("n must be at least 1!")
else:
    n = int(text)
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

    print()
