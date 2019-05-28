"""Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание."""

import requests
str = ["699991.txt"]
link = "https://stepic.org/media/attachments/course67/3.6.3/"

while str[0][0:2] != "We":
    print(link+str[0])
    response = requests.get(link + str[0])
    text = response.text.splitlines(True)
print(str)
open("out.txt", "w").writelines(str)
