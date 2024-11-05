first = int(input("Введите первое число:"))
second= int(input("Введите второе число:"))
third = int(input("Введите тетье число:"))
if first == second == third:
    print(3)
elif first == second or second == third or first == third :
    print (2)
else:
    print(0)