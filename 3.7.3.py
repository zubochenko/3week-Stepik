"""Простейшая система проверки орфографии основана на использовании списка известных слов.
Каждое слово в проверяемом тексте ищется в этом списке и, если такое слово не найдено, оно помечается, как ошибочное.
Напишем подобную систему.
Через стандартный ввод подаётся следующая структура: первой строкой — количество 𝑑
 записей в списке известных слов, после передаётся  d строк с одним словарным словом на строку, затем — количество 𝑙
 строк текста, после чего — 𝑙  строк текста.

Напишите программу, которая выводит слова из текста, которые не встречаются в словаре. Регистр слов не учитывается. Порядок вывода слов произвольный. Слова, не встречающиеся в словаре, не должны повторяться в выводе программы.
"""
num_d = int(input())
lst_words = []
lst_str = []
new_list = []
def iter(number_iter,lst):
    while number_iter != 0:
        words = input().lower()
        lst.append(words)
        number_iter -= 1
        continue
    return lst
iter(num_d, lst_words)
num_str = int(input())
for i in range(num_str):
    words = input().split(' ')
    for word in words:
        lst_str.append(word)

d = {key: value for key, value in zip(lst_words, range(1,num_d+1))}
for i in lst_str:
    if i.lower() not in d and i not in new_list:
        print (i)
        new_list.append(i)