# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main(array):
    new = reverse(array)
    max = maximum(array)
    min = minimum(array)
    print(new)
    print(max)
    print(min)

def reverse(array):
    new = []
    for i in range(len(array)-1,-1,-1):
        new.append(array[i])
    return new
def maximum(array):
    max = array[0]
    for i in range(1,len(array)):
        if array[i]>max:
            max = array[i]
    return max

def minimum(array):
    min = array[0]
    for i in range(1,len(array)):
        if array[i]<min:
            min = array[i]
    return min

massive = [11,-1,54,10,15,153,25,525,24,879,79,-56,1000]
main(massive)
