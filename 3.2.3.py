
"""Имеется реализованная функция 𝑓(𝑥), принимающая на вход целое число 𝑥
, которая вычисляет некоторое целочисленое значение и возвращает его в качестве результата работы.
Функция вычисляется достаточно долго, ничего не выводит на экран, не пишет в файлы и зависит только от переданного аргумента 𝑥.
Напишите программу, которой на вход в первой строке подаётся число  — количество значений 𝑥
, для которых требуется узнать значение функции 𝑓(𝑥), после чего сами эти 𝑛
 значений, каждое на отдельной строке. Программа должна после каждого введённого значения аргумента вывести соответствующие
значения функции на отдельной строке.
Для ускорения вычисления необходимо сохранять уже вычисленные значения функции при известных аргументах.
Обратите внимание, что в этой задаче установлено достаточно сильное ограничение в две секунды по времени исполнения кода на тесте."""
num_iter = int(input())
lst = []
d={}
while num_iter !=0:
    x = int(input())
    lst.append(x)
    num_iter-=1
for i in lst:
    if f(i) in d:
        print(d[i])
    else:
        d[i]=f(i)
        print(d[i])
