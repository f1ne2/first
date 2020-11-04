# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main(array):
    new = reverse(array)
    print(new)

def reverse(array):
    new = []
    for i in range(len(array)-1,-1,-1):
        new.append(array[i])
    return new

massive = [1,2,3,10,15,153,25,525,24,879,79]
main(massive)
