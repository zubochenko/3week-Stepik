"""Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно смотреть,
 как, например, на наиболее часто используемые.

Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте
 и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести лексикографически первое (можно использовать оператор
 < для строк).

Слова, написанные в разных регистрах, считаются одинаковыми."""
lst = []
n_lst = []
d = {}
with open("dataset_3363_3-2.txt", 'r') as file:
    #str = file.readline()while str:
    for line in file.readlines():
        lst.append(line.rstrip())
for i in lst:
    str = i.lower().split()
    n_lst.append(str)
print(n_lst)
for str in n_lst:
    for key in str:
        if key not in d:
            d[key]=1
        else:
            d[key]+=1
max_v = max(d.values())
new_d = {k: v for k, v in d.items() if v==max_v}
for k in new_d:
    print (k, new_d[k])

file.close()