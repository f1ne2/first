
def main(stroka, old, new):
    result_replace = find(stroka, old, new)
    print(result_replace)

def find(stroka, old, new):
    massive = []
    for i in range(len(stroka)):
        for j in range(len(old)):
            if stroka[i+j] != old[j]:
                break
            elif j == len(old) - 1:
                massive = replace(stroka, new, i)
    return massive

def replace(str, new, i):
    for j in range(len(new)):
        str[i+j] = new[j]
    return str


str = "мама мыла раму"
str_old = "ма мы"
str_new = "ла ли"
main(str, str_old, str_new)