def add(num1,num2):
    result = num1 + num2
    print(int(result))


while True:
    with open("epiloges.txt","r",encoding="utf-8") as file:
        content = file.read()
        print(content)

    operation = input("Κάνε μια επιλογή (πχ.1) για Πρόσθαιση: ")
    num1 = float(input("Βάλε τον πρώτο αριθμό: "))
    num2 = float(input("Βάλε τον δεύτερο αριθμό: "))

    if operation.startswith("1"):
        get_add = add(num1, num2)


