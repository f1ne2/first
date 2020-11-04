# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
choice = "y"
i = 0
name2 = []
while choice.lower() == "y":
    name = str(input("Введите элемент массива"))
    name2.append(name)
    i += 1
    choice = str(input("Для ввода следующего элемента нажмите y, а для выхода любую другую клавишу"))
    if choice == "y":
        continue
    else:
        break
new = []
n = 0
k=i
if i>0:
    while n < i:
        new.append(name2[k-1])
        n += 1
        k -= 1
print(name2)
print(new)
