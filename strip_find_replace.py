
def main(string,sub_string,str_new):
    str = trim(string)
    print(str)
    indexes = find(string,sub_string)
    print(indexes)
    str_edit = replace(string,sub_string,str_new)
    print(str_edit)

def trim(string):
    str = ""
    for i in range(len(string)-1):
        if string[i] == " " and string[i+1] == " ":
            continue
        else:
            str = str + string[i]
    if string[len(string)-1] != " ":
        str = str + string[len(string)-1]
    if str[0] == " ":
        str = str[1:len(str)]
    if str[len(str)-1] == " ":
        str = str[0:len(str)-1]
    return str

def find(string,sub_string):
    indexes = []
    j = 0
    for i in range(len(string)):
        if string[i] == sub_string[j]:
            j += 1
            if j == len(sub_string):
                indexes.append(i-len(sub_string)+1)
                j = 0
        else:
            j = 0
    return indexes

def replace(string, sub_string, str_new):
    str_edit = ""
    indexes = find(string, sub_string)
    if len(indexes) != 0:
        for i in range(len(indexes)):
            if i == 0:
                str_edit = str_edit + string[i:indexes[i]] + str_new
            else:
                str_edit = str_edit + string[indexes[i - 1] + len(sub_string):indexes[i]] + str_new
        str_edit = str_edit + string[indexes[len(indexes) - 1] + len(sub_string):len(string)]
    return str_edit

string = "            dhd sdjlsnd мыла skdnskdb v мыла                              "
sub_string = "мыла"
str_new = "лилa"
main(string,sub_string,str_new)