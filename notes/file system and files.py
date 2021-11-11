# При работе с файлами мы рассматриваем 2 типа файлов:
# ●	текстовые - содержимое этих файлов является текстом и может быть интерпретировано в качестве текста.
# ●	бинарные (двоичные) файлы - не являются текстом.
# Практически для любого формата бинарных файлов уже точно существуют библиотеки в языке Python, которые умеют с этим
# форматом файлом работать.
# Например:
# Библиотека для работы с графикой Pillow https://ru.wikipedia.org/wiki/Python_Imaging_Library
# Библиотека для работы со звуком wave и Python Audio Tools https://wiki.python.org/moin/Audio/
# Далее будем рассматривать преимущественно текстовые файлы.
# Основа для работы с файлами — built-in функция open()
# open(file, mode="rt")
# Эта функция имеет два аргумента. Аргумент file принимает строку, в которой содержится путь к файлу. Второй аргумент,
# mode, позволяет указать режим, в котором необходимо работать с файлом. По умолчанию этот аргумент принимает значение
# «rt», с которым, и с некоторыми другими, можно ознакомиться в таблице ниже
# Режимы открытия файлов:
# 'r' (read)	открытие на чтение (является значением по умолчанию).
# 'w' (write)	открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
# 'x'	открытие на запись, если файла не существует, иначе исключение.
# 'a' (append)	открытие на дозапись, информация добавляется в конец файла, если файла не существует, создается новый.
# 'b' (binary)	открытие в двоичном режиме.
# 't' (text)	открытие в текстовом режиме (является значением по умолчанию).
# '+'	открытие на чтение и запись
# f = open('text.txt', 'r')
# Эти режимы могут быть скомбинированы. Например, «rb» открывает двоичный файл для чтения. Комбинируя «r+» или «w+»
# можно добиться открытия файла в режиме и чтения, и записи одновременно с одним отличием — первый режим вызовет
# исключение, если файла не существует, а работа во втором режиме в таком случае создаст его.
# Функция open() возвращает нам файловый объект file object, благодаря которому мы можем читать данные, записывать
# данные. Самое главное, file object нужно закрывать, когда вы с файлом поработали. Потому что нужно освобождать те
# системные ресурсы, которые были затрачены для того, чтобы поддерживать соединение с файлом.
# С помощью метода read() мы передаем число символов, которые мы хотим считать из нашего файла.
# x = f.read(5)
# Если указать read() без параметров, то мы считаем весь файл до конца:
# y = f.read()
# Мы можем посмотреть представление считанного текста в виде одной строки с помощью функции repr()
# repr - это однозначное (недвусмысленное) представление объекта в виде строки, такой, чтобы возможно было бы из этого
# представления сделать такой же объект, в отличие от str, который служит для создания читаемого объекта
# f = open('passwords.txt', 'r', encoding='utf-8')
# x = f.read()
# print(repr(x))
# И увидим строку, включающую в себя символы переноса строки \n
# Для разбиения текста на отдельные строки можно использовать метод splitlines(). В результате получим строки, которые
# не содержат символов переноса строки:
# f = open('passwords.txt', 'r', encoding='utf-8')
# x = f.read()
# y = x.splitlines()
# print(y)
# Если файл занимает много места на диске, мы можем считывать его построчно с помощью метода readline().
# f = open('passwords.txt', 'r', encoding='utf-8')
# x = f.readline()
# print(repr(x))
# Символ переноса  строки останется в строке
# Для того, чтобы его убрать, можно воспользоваться методом rstrip()
# x = f.readline().rstrip()
# После того как файл считан целиком, дальнейшие попытки применить к нему метод read() будут выдавать пустую строку.
# Прочитать строку с определенным номером (например, читаем четвертую строку файла, служебные символы убираются):
# from linecache import getline
# getline('file.txt', 4)
# Для тех, кто тоже задумался о различии strip (который давали в прошлом курсе) и rstrip:
# str = "mississippim"
# print(str.strip('m'))  # убирает указанный символ в конце и в начале строки
# print(str.rstrip('m'))  # убирает указанный символ в конце строки
# print(str.lstrip('m'))  # убирает указанный символ в начале строки
# Если не указывать в скобках символ - убирают служебные символы (в т.ч. пробелы)
# В книге Лутц пишет, что можно использовать открытие файла так:
# for line in open('data.txt'):
#     print(line, end='')
# И закрывать не обязательно, так как файл открывается в инструкции цикла, как временный и закрывается автоматически
# сборщиком мусора.
# При этом он пишет, что такой вызов в данный момент является наиболее предпочтительным.
# with open('data.txt') as f:
#     for line in f:
#         print(line, end='')
# Метод lineno возвращает номер строки, которую только что прочитали.
# Перед прочтением первой строки возвращается 0. После прочтения последней строки последнего файла (если читаем
# несколько) возвращает номер строки этой строки.
# def lineno_(x):
#     return x.lineno()
# with fileinput.input(files=(file, file2)) as f:
#     for line in f:
#         print(lineno_(f))
# При записи файла нужно самостоятельно добавлять символы переноса строки:
# f = open('test.txt', 'w')
# f.write('Hello\n')
# f.write('world')
# f.close()
# Если у нас уже есть список строк, который нужно записать в файл, хорошей практикой будет использовать для него метод
# join() и с его помощью добавить переносы строк:
# f = open('test.txt', 'w')
# lines = ['line 1', 'line 2', 'line 3']
# contents = '\n'.join(lines)
# f.write(contents)
# f.close()
# Также с помощью join() мы можем склеивать не только строки, но и отдельные слова, если нам это необходимо. В этом
# случае мы можем указывать в join() символ пробел или табуляцию.
# import os
# print(repr(os.linesep))
# Для любого типа файла поможет записать корректный знак переноса.
# В языке Python важно закрывать файлы. Однако от того места, где файл открывался то того где он должен закрыться,
# могла бы произойти ошибка. В этом случае интерпретатор не дойдет до вызова метода close()
# Чтобы обезопасить себя от такой ситуации, мы можем использовать инструкцию open() вместе с конструкцией with. Когда
# выходим из блока with, интерпретатор сам закроет наш файл, независимо оттого была в блоке ошибка или нет.
# with open('test.txt') as f:
#     for line in f:
#         line = line.rstrip()
#         print(line)
# Такая конструкция гарантирует закрытие файла вне зависимости от того дошел ли интерпретатор до конца блока with или
# во время выполнения произошла ошибка. Поэтому эта конструкция является рекомендованной для работы с файлами.
# Внутри конструкции with мы можем открыть сразу несколько файлов:
# with open('test.txt') as f, open('test-copy.txt', 'w') as w:
#     for line in f:
#         w.write(line)

# Библиотеки os и os.path
# С помощью функции listdir() мы можем узнать список папок и файлов.
# Запуск функции без аргументов выдает файлы и папки внутри текущей директории:
# import os
# import os.path
# print(os.listdir())
# Если в качестве аргумента указать имя определенной папки, то функция покажет ее содержимое.
# Функция os.getcwd() возвращает текущую папку:
# print(os.getcwd())
# print(os.listdir(".idea"))
# Функция exists() библиотеки os.path позволяет проверить наличие файла или папки
# print(os.path.exists("dict.py"))  # True
# Мы также можем проверить является ли переданный параметр файлом или папкой с помощью функций isfile() и isdir():
# print(os.path.isfile(dict.py))
# print(os.path.isdir(dict.py))
# Мы можем легко узнать абсолютный путь по относительному с помощью abspath()
# print(os.path.abspath('dict.py'))
# Можем сменить директорию с помощью chdir()
# os.chdir('.idea')
# print(os.getcwd())
# Функция os.walk() позволяет рекурсивно пройтись по всем папкам, подпапкам и т.д.
# Она возвращает нам генератор. И каждый раз, когда мы будем спрашивать следующее значение у этого генератора, он будет
# возвращать нам кортеж из 3 элементов:
# 1.	строковое представление текущей директории, которую он рассматривает
# 2.	список всех папок, которые есть в данной директории
# 3.	список всех файлов, которые есть в данной директории

# import os.path
#
# tree = os.walk('.')
# for current_dir, dirs, files in tree:
#     print(current_dir)
#     print(dirs)
#     print(files)
#     print('----------')
# Библиотека shutil
# Функция copy() библиотеки shutil позволяет копировать файлы.
# Она принимает 2 аргумента: откуда и куда копировать.
# import shutil
# shutil.copy('test.txt', 'tests/test3.txt')
# Функция copytree() позволяет скопировать целиком папку вместе с файлами:
# shutil.copytree('tests', 'tests/tests')

# А еще очень полезным в модуле os является возможность указания точного пути к открываемому файлу, так сказать
# "кроссплатформенно" (т.е. без путаницы в / и \ в путях):
# import os
# with open(os.path.join('C:', 'Test', 'Py', 'dataset_24465_4.txt'), 'r', encoding='utf-8') as src:
#     f = src.read()
# С помощью os.path.join система сама поставит слеш (*nix) или бек-слеш (Win), в зависимости от того - на какой ОСи
# запускается скрипт. Просто указываете имена директорий в пути.

# Очень опасные модули... os.listdir() - программа падает если передать не существующий каталог os.path.isfile и
# os.path.isdir возвращает False если их не существует, так что можно влететь os.path.abspath() - не проверяет наличие
# файла, а просто добавляет путь до текущей папки os.chdir() - падает если путь не существует shutil.copy - падает если
# исходный файл не существует и молча перезаписывает итоговый файл, если он существует В общем, при работе с модулем
# проверять каждый чих, желательно в try/except

# С помощью os.chdir("..") можно подниматься выше по директориям, если в скобках указать путь, то перейти по этому пути
# как подняться на уровень выше в дереве каталогов? Как вариант, (обратный слеш актуален для винды):
# os.chdir('\\'.join(os.getcwd().split('\\')[:-1]))
# os.chdir(os.path.split(os.getcwd())[0])
# Начать саму работу с файлом можно с помощью объекта класса io.TextIOWrapper, который возвращается функцией open().
# У этого объекта есть несколько атрибутов, через которые можно получить информацию
# name — название файла;
# mode — режим, в котором этот файл открыт;
# closed — возвращает True, если файл был закрыт.
# По завершении работы с файлом его необходимо закрыть при помощи метода close()
# f = open("examp.le", "w")
# //  работа с файлом
# f.close()
# Однако более pythonic way стиль работы с файлом встроенными средствами заключается в использовании конструкции
# with .. as .., которая работает как менеджер создания контекста. Написанный выше пример можно переписать с ее помощью
# with open("examp.le", "w") as f:
# // работа с файлом
# Главное отличие заключается в том, что python самостоятельно закрывает файл, и разработчику нет необходимости помнить
# об этом. И бонусом к этому не будут вызваны исключения при открытии файла (например, если файл не существует).
# Чтение из файла
# При открытии файла в режимах, допускающих чтение, можно использовать несколько подходов.
# Для начала можно прочитать файл целиком и все данные, находящиеся в нем, записать в одну строку.
# with open("examp.le", "r") as f:
#     text = f.read()
# Используя эту функцию с целочисленным аргументом, можно прочитать определенное количество символов.
# with open("examp.le", "r") as f:
#     part = f.read(16)
# При этом будут получены только первые 16 символов текста. Важно понимать, что при применении этой функции несколько
# раз подряд будет считываться часть за частью этого текста — виртуальный курсор будет сдвигаться на считанную часть
# текста. Его можно сдвинуть на определенную позицию, при необходимости воспользовавшись методом seek().
# with open("examp.le", "r") as f: # 'Hello, world!'
#     first_part = f.read(8)       # 'Hello, w'
#     f.seek(4)
#     second_part = f.read(8)      # 'o, world'
# Другой способ заключается в считывании файла построчно. Метод readline() считывает строку и, также как и с методом
# read(), сдвигает курсор — только теперь уже на целую строку. Применение этого метода несколько раз будет приводить к
# считыванию нескольких строк. Схожий с этим способом, другой метод позволяет прочитать файл целиком, но по строкам,
# записав их в список. Этот список можно использовать, например, в качестве итерируемого объекта в цикле.
# with open("examp.le", "r") as f:
#     for line in f.readlines():
#         print(line)
# Однако и здесь существует более pythonic way. Он заключается в том, что сам объект io.TextIOWrapper имеет итератор,
# возвращающий строку за строкой. Благодаря этому нет необходимости считывать файл целиком, сохраняя его в список, а
# можно динамически по строкам считывать файл. И делать это лаконично.
# with open("examp.le", "r") as f:
#     for line in f:
#         print(line)
# Запись в файл
# Функциональность внесения данных в файл не зависит от режима — добавление данных или перезаписывание файла. В
# выполнении этой операции также существует несколько подходов.
# Самый простой и логичный — использование функции write()
# with open("examp.le", "w") as f:
#     f.write(some_string_data)
# Важно, что в качестве аргумента функции могут быть переданы только строки. Если необходимо записать другого рода
# информацию, то ее необходимо явно привести к строковому типу, используя методы __str__(self) для объектов или
# форматированные строки.
# Есть возможность записать в файл большой объем данных, если он может быть представлен в виде списка строк.
# with open("examp.le", "w") as f:
#     f.writelines(list_of_strings)
# Здесь есть еще один нюанс, связанный с тем, что функции write() и writelines() автоматически не ставят символ переноса
# строки, и это разработчику нужно контролировать самостоятельно.
# Существует еще один, менее известный, способ, но, возможно, самый удобный из представленных. И как бы не было странно,
# он заключается в использовании функции print(). Сначала это утверждение может показаться странным, потому что
# общеизвестно, что с помощью нее происходит вывод в консоль. И это правда. Но если передать в необязательный аргумент
# file объект типа io.TextIOWrapper, каким и является объект файла, с которым мы работаем, то поток вывода функции
# print() перенаправляется из консоли в файл.
# with open("examp.le", "w") as f:
#     print(some_data, file=f)
# Сила такого подхода заключается в том, что в print() можно передавать не обязательно строковые аргументы — при
# необходимости функция сама их преобразует к строковому типу.


# Вам дается текстовый файл, содержащий некоторое количество непустых строк.
# На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.
# Пример входного файла:
# ab
# c
# dde
# ff
# Пример выходного файла:
# ff
# dde
# c
# ab

# with open('test.txt') as f, open('test-copy.txt', 'w') as w:
#     lst = []
#     for line in f:
#         lst.append(line.rstrip())
#     for element in reversed(lst):
#         w.write(element + '\n')
#
# lines = open("input.txt").readlines()
# with open("output.txt", "w") as out:
#     out.writelines(reversed(lines))
#
# with open('dataset_24465_4.txt', 'r') as fr, open('dataset_24465_4_w.txt', 'w') as fw:
#     fw.writelines(fr.readlines()[::-1])
#
# такое значение перед reverse-ом: ['ab\n', 'c\n', 'dde\n', 'ff'], затем reverse и печать в файл- то есть после "ff"
# нет "\n"; а если смотреть в документацию, то там сказано:  writelines() does not add line separators
# Прошло конечно огромное количество времени, но я все же докопался до того, что и reverse, и reversed склеят нам
# последнюю и предпоследнюю строчку. НО в нашем задании этого не случается, потому что в конечной строке также есть
# символ переноса строки.
# Сразу почуял подвох, слишком просто. Очевидно, что выгружать весь файл очень расточительно для ресурсов, немного
# поисков и нашел подходящий пакет "file_read_backwards". Код в итоге выглядит так:
#
# from file_read_backwards import FileReadBackwards
# with FileReadBackwards('file1.txt') as f, open('file2.txt','w') as w:
#     for line in f:
#         w.write(line+'\n')

import os

os.chdir('D:\\main')
out = []
for current_dir, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            out.append(current_dir.lstrip('.\\').replace('\\', '/'))
            break
f = open('D:\\main_ans.txt', 'w')
for element in sorted(out):
    f.write(element + '\n')
f.close()