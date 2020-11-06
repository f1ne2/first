
def main(string,sub_string):
    delete_space(string)
    search_sub_string(string,sub_string)

def delete_space (string):
    str = ""
    n = 0
    m = 0
    for j in range(len(string)-1,0,-1):
        if string[j] != " ":
            n = j
            break
    for j in range(len(string)):
        if string[j] != " ":
            m = j
            break
    for i in range(m,n+1):
        str = str + string[i]
    print(str)

def search_sub_string (string,sub_string):
    j = 0
    k = 0
    for i in range(len(string)):
        if string[i] == sub_string[j]:
                j += 1
                k = i
                if j == len(sub_string):
                    print("конечный индекс подстроки",k,"начальный индекс подстроки",k-(len(sub_string)-1))
                    j = 0
        else:
            j = 0

string = "мама мыла    раму    "
sub_string = "мыла "
main(string,sub_string)