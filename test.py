print("Калькулятор 3000 готов!")
print("=======================")
print("Калькулятор 3000 готов!")
print("-----------------------")
print("Калькулятор 3000 готов!")
while True:
    print("Введите первую цифру:")
    a = int(input())
    print("Введите вторую цифру:")
    b = int(input())
    print("Что нужно сделать:")
    c = input()
    if c == '+':
        x = a + b
        print("Итог = ",x)
    elif c == "-":
        x = a - b
        print("Итог = ", x)
    elif c == '*':
        x = a * b
        print("Итог = ", x)
    elif c == "/":
        x = a / b
        print("Итог = ", x)