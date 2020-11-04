# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main(array):
    new = reverse(array)
    print(new)

def reverse(array):
    new = []
    k = len(array)-1
    for item in array:
        new.append(array[k])
        k -= 1
    return new


massive = [1,2,3,10,15,153,25]
main(massive)
