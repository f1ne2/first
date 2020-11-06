
def main(string,sub_string,str_new):
    str = trim(string)
    print(str)
    start = find(string,sub_string)
    print(start)
    str_edit = replace(string,start,str_new)

def trim (string):
    str = ""
    for i in range(0,len(string)):
        if string[i] == " " and string[i+1] == " ":
            continue
        else:
            str = str + string[i]
    return str

def find (string,sub_string):
    start = []
    j = 0
    k = 0
    for i in range(len(string)):
        if string[i] == sub_string[j]:
            j += 1
            k = i
            if j == len(sub_string):
                start.append(k-(len(sub_string)-1))
                start.append(k)
                j = 0
        else:
            j = 0
    return start

def replace (string,start,str_new):
    str_edit = ""
    if len(start) != 0:
        for i in range(len(start)):
            if i == 0:
                str_edit = str_edit + string[i:start[i]] + str_new
            if i % 2 == 0 and i != 0:
                str_edit = str_edit + string[start[i-1]+1:start[i]] + str_new
            if i == len(start)-1:
                str_edit = str_edit + string[start[i]+1:len(string)]
    print(str_edit)

string = " sjygf мыла  rjgh  мыла раму"
sub_string = "мыла"
str_new = "лилa"
main(string,sub_string,str_new)