first = int(input()) #int() без аргументов возвращает 0
second = int(input())
third = int(input())

if first == second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)