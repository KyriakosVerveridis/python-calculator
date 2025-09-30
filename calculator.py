
results = []

def get_add(num1,num2):
    result = num1 + num2
    results.append(result)
    print(int(result))
    return results

def get_subtracked(num1,num2):
    result = num1 - num2
    results.append(result)
    print(int(result))
    return results

def get_multiply(num1,num2):
    result = num1 * num2
    results.append(result)
    print(int(result))
    return results

def get_divide(num1,num2):
    result = num1 / num2
    results.append(result)
    print(int(result))
    return results

while True:
    with open("epiloges.txt","r",encoding="utf-8") as file:
        content = file.read()
        print(content)

    operation = input("Κάνε μια επιλογή (πχ.1) για Πρόσθαιση: ")
    while not operation.isdigit() or int(operation) < 1 or int(operation) > 5:
        print("Μη έγκυρη επιλογη διαλεγε 1,2,3,4,5")
        operation = input("Κάνε μια επιλογή (πχ.1) για Πρόσθαιση: ")
    if operation.startswith("5"):
        break
    num1 = float(input("Βάλε τον πρώτο αριθμό: "))
    num2 = float(input("Βάλε τον δεύτερο αριθμό: "))

    if operation.startswith("1"):
        add = get_add(num1, num2)
    elif operation.startswith("2"):
        subtracked = get_subtracked(num1,num2)
    elif operation.startswith("3"):
        multiply = get_multiply(num1,num2)
    else:
        try:
            divide = get_divide(num1,num2)
        except ZeroDivisionError:
            print("0")
    int_results = [int(num) for num in results]
    print(f"Ιστορικό τελευταίων πράξεων {int_results}")





