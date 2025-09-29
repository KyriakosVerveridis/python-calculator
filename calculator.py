def get_add(num1,num2):
    result = num1 + num2
    print(int(result))

def get_subtracked(nuim1,num2):
    result = num1 - num2
    print(int(result))

def get

while True:
    with open("epiloges.txt","r",encoding="utf-8") as file:
        content = file.read()
        print(content)

    operation = input("Κάνε μια επιλογή (πχ.1) για Πρόσθαιση: ")
    num1 = float(input("Βάλε τον πρώτο αριθμό: "))
    num2 = float(input("Βάλε τον δεύτερο αριθμό: "))

    if operation.startswith("1"):
        add = get_add(num1, num2)
    elif operation.startswith("2"):
        subtracked = get_subtracked(num1,num2)


