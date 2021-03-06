# Класс map - применяет функцию к каждому члену последовательности
# n_test, k = map(int, input().split())  # input_file [a, b, c, ...] -> input_file(a), input_file(b), input_file(c) ...
# print(n_test + k)
# x = input().split()
# n_test, k = (int(i) for i in x)  # то же действие другим синтаксисом
# print(n_test + k)
# map не выдает все значения сразу, а является итератором и по нему можно итерироваться:
# map_obj =
# a = next(map_obj)
# b = next(map_obj)
# c = next(map_obj)
# print(a + b + c)
# Важно понимать, что объекты класса map вычисляют значения достаточно лениво.
# В тот момент, когда мы создаем объект нашего класса map, мы на самом деле запоминаем лишь две ссылки: на функцию и на
# итератор второго аргумента. Лишь в момент когда нас спрашивают какой элемент является следующим, мы считаем следующий
# элемент из итератора и применяем к нему ту функцию, которую нам передали.

# Класс filter
# Также принимает 2 аргумента: функцию и последовательность - элементы которой мы хотим отфильтровать.
# Функция должна возвращать True, если элемент последовательности нам подходит и False, если не подходит.
# x = input().split()
# xs = (int(i) for i in x)
# def even(x):
#     return x % 2 == 0
# evens = filter(even, xs)
# for i in evens:
#     print(i)
# Конструктор класса filter возвращает нам filter object. Он, в свою очередь, является итератором и внутри него
# реализован метод next().
# Если в конструктор класса list мы поместим итератор, он попробует собрать все элементы из данного итератора и
# поместить их внутрь данного списка.
# Однако, пользоваться им стоит аккуратно. Если вы уверены, что ваш итератор, во-первых, возвращает конечное число
# элементов, а, во-вторых, если они разумно умещаются в оперативной памяти.
# evens = list(filter(even, xs))
# print(evens)

# Сначала мы не знали функций и методов:
# print(' '.join([i for i in input().split() if int(i)%2 == 0]))
# Затем мы познакомились с функциями и методами:
# def even(x):
#     return x%2 == 0
# print(' '.join([i for i in input().split() if even(int(i))]))
# И наконец, освоили лямбда-функции:
# print(' '.join([i for i in input().split() if (lambda x: x%2 == 0)(int(i))]))

# Чем отличается filter от map? Обе функции принимают в качестве аргументов функцию и последовательность. Разница в том,
# что map применяет свою функцию ко всем объектам, а функция в filter должна возвращать логическое значение True/False
# и сама возвращает элементы для которых выполнилось True. map просто применяет функцию (любую) к элементам любой
# последовательности (данные типа float и str).

# lambda функции
# lambda функции в языке Python - это простой синтаксис для создания новых объектов функций (коротко и лаконично писать
# короткие функции для передачи внутрь другой функции). Лямбда функции предоставляют нам удобный способ создать функцию
# «прямо на месте».
# def even(x):
#     return x%2 == 0
# even = lambda x: x % 2 == 0  # заменим функцию выше
# evens = list(filter(lambda x: x % 2 == 0, xs))  # потом заменим even созданной функцией
# print(evens)
# Синтаксис использования:
# ●	Сначала идет ключевое слово lambda
# ●	Затем до двоеточия мы указываем аргументы, которые принимает наша функция. И здесь верны все те же правила, что
# верны и для аргументов обычных функций. Мы можем определить аргументы со звездочкой, с двумя звездочками и аргументы
# со значением по умолчанию.
# ●	После двоеточия следует одно выражение. Оно должно быть возвращаемым значением функции.
# Удобство использования lambda функций заключается в том, что их можно передавать внутрь других функций.
# x = [
#     ("Guido", "van", "Rossum"),
#     ("Haskell", "Curry"),
#     ("John", "Backus")
# ]
# def length(name):
#     return len(''.join(name))
# # name_lengths = [length(name) for name in x]
# # print(name_lengths)
# x.sort(name=length)
# print(x)
# x.sort(name=lambda name: len(''.join(name)))  # заменили функцию выше короткой записью
# print(x)
#
# never_use_this_at_production_code = lambda x: lambda y: lambda z: x * y * z
# mul2 = never_use_this_at_production_code(2)
# mul3 = mul2(3)
# print(mul3(4))  # 24
# Пример лямбды в лямбде в лямбде, и вызова в скрипте, можно наверное и с рекурсией что нибудь придумать, но я бы вместо
# этого воспользовался обычными функциями :)

# input_file = [lambda x, i=i: x ** i for i in range(10)]
# print(input_file[3](2))  # 8print(input_file[9](2))  # 512
# тонкость тут в том, что i - именованный аргумент, а такие аргументы вычисляются / присваиваются один раз при создании
# функции (актуально для любой функции, просто в данном случае у нас лямбда). Тут каждая лямбда вычисляет / сохраняет
# свою i  в момент генерации списка, если что.
# Тонкость в том, что, когда мы объявляем функцию, то переменные, которые мы в ней пишем, не вычисляются в момент
# объявления (за исключением значений по умолчанию). Поэтому когда мы пишем:
# input_file = [lambda x: x ** i for i in range(10)]
# То просто создаем список из 10 одинаковых функций вида: lambda x: x**i
# Вариант, когда мы передаем i в качестве значения по умолчанию, рассмотрен выше, значение по умолчанию вычисляется в
# момент создания функции, поэтому мы получим список, состоящий из функций вида: [(lambda x, i=0: x**i),
# (lambda x, i=1: x**i), ..., (lambda x, i=9: x**i)]
# Есть ещё один вариант, без использования значений по умолчанию:
# input_file = [eval('lambda x: x ** ' + str(i)) for i in range(10)]
# Здесь мы сначала конструируем строку, содержащую текст функции, а затем исполняем указанное выражение, создавая
# нужную нам функцию.

# Модуль operator
# Модуль operator экспортирует набор эффективных функций, которые соответствуют внутренним операторам Python.
# Например operator.add(x, y) эквивалентен выражению x + y.
# import operator as op
# print(op.add(4, 5))
# print(op.mul(4, 5))
# print(op.contains([1, 2, 3], 4))  # 4 in [1, 2, 3]  # вхождение в список
# Самыми интересными функциями в данной библиотеке являются itemgetter(), который позволяет нам достать элемент
# какой-нибудь коллекции и attrgetter(), который позволяет достать атрибут у какого-нибудь объекта.
# x = [1, 2, 3]
# input_file = op.itemgetter(1)  # input_file(x) == x[1]
# print(input_file(x))
# В результате Python выведет 2, так как она является 1-м элементом списка x (отчет с нуля).
# По аналогии с помощью этого метода можно обращаться к элементам словаря:
# x = {"123": 3}
# input_file = op.itemgetter("123")  # input_file(x) == x["123"]
# print(input_file(x))
# Конструктор attrgetter() ведет себя почти подобным образом, но он пытается взять атрибут у объекта:
# input_file = op.attrgetter("sort")  # input_file(x) == x.sort
# print(input_file([]))

# x = [
#     ("Guido", "van", "Rossum"),
#     ("Haskell", "Curry"),
#     ("John", "Backus")
# ]
# import operator as op
# x.sort(name=op.itemgetter(-1))  # сортировка по последнему элементу
# print(x)
# можем легко взять атрибуты объектов, которые у тебя объявлены в твоем классе, если класс делает столы и у него
# (у объекта-стола)есть атрибут площадь ты можем его быстренько достать. Кажется в этом удобство. Читать  с атрибутами
# объектов: https://habrahabr.ru/post/137415/
# как бы значит, что вы взяли ссылку на атрибут sort у list, т.е. input_file(x) == x.sort . Если вы теперь вызовите этот метод,
# т.е. напишите input_file(x)() или g(), а потом выведите список x, то увидите, что теперь он отсортирован.

# Модуль functools
# Функция partial()
# partial() получает функцию A с аргументами и возвращает новую функцию B, вызов которой эквивалентен вызову функции A
# с указанными аргументами.
# import operator as op
# from functools import partial  # Запомнить некоторые аргументы с которыми мы хотели вызвать функцию, и их не надо
# передавать
# x = int('1001', base=2)  # перевод двоичного в десятичное
# print(x)
# int_2 = partial(int, base=2)  # Запомнили
# x = int_2('1001')
# print(x)
#
# x = [
#     ("Guido", "van", "Rossum"),
#     ("Haskell", "Curry"),
#     ("John", "Backus")
# ]
# sort_by_last = partial(list.sort, name=op.itemgetter(-1))  # Запомнили
# print(x)
# sort_by_last(x)  # применили
# print(x)
#
# y = ["abc", "cba", "abb"]
# sort_by_last(y)  # применили на других данных
# print(y)

# Конечно reduce творит чудеса. Жаль, что про данный метод не рассказали. На мой взгляд наглядный пример её
# использования - подсчет факториала:
# from functools import reduce
# def factorial(n_test):
#    return reduce(lambda x, y: x*y, range(1, n_test+1))
# Разница между map() и reduce()?. map применяет функцию к каждому элементу коллекции в отдельности. На выходе список.
# reduce  же множит вашу операцию на весь список. Например reduce(lambda x,y: x+y, range(1,10)) - это сумма элементов
# от 1 до 9. Как будто вы суммируете не 2 элемента а все 9.
# from functools import reduce
# x = [1, 2, 3, 4, 5, 6, 7]
# print(list(map(lambda x: x + x, x)))  # каждый элемент складывается сам на себя
# print(reduce(lambda x, y: x + y, x))  # первый и второй элемент складываются, на следующей итерации первым элементом
# # становятся сложенные элементы, а вторым становится 3 элемент
# Вывод:
# [2, 4, 6, 8, 10, 12, 14]
# 28
# import this. Гвидо не любит лямбда функции, в питоне 3 их вообще хотели выпилить.
# Еще partial возвращает функцию с всякими встроенными атрибутами, такие как args, keywords и func.
# А еще мы можем поменять те аргументы которые "забросили" с помощью partial.
# int_2('31', base=8)
# partial ведет себя как обычная функция, только с заранее заполнеными аргументами, а lambda - это есть недофункция.
# Если вы говорите что у partial куча доп. кода, лагов, значит и у функций то же самое, что звучит как бред.


# Лямбда функции предоставляют нам удобный способ создать функцию «прямо на месте».
# Но иногда, когда нужно создавать много однотипных лямбда функций, еще удобнее будет создать функцию, которая будет их
# генерировать.
# Реализуйте функцию mod_checker(x, mod=0), которая будет генерировать лямбда функцию от одного аргумента y, которая
# будет возвращать True, если остаток от деления y на x равен mod, и False иначе.

def mod_checker(x, mod=0):
    return lambda y: y % x == mod

mod_3 = mod_checker(3)
print(mod_3(3))  # True
print(mod_3(4))  # False
mod_3_1 = mod_checker(3, 1)
print(mod_3_1(4))  # True

mod_checker = lambda x, mod=0: lambda y: y % x == mod  # решение в одну строку

# Функция zip() принимает итерируемый объект, например, список, кортеж, множество или словарь в качестве аргумента. Затем
# она генерирует список кортежей, которые содержат элементы из каждого объекта, переданного в функцию.
# Предположим, что есть список имен и номером сотрудников, и их нужно объединить в массив кортежей. Для этого можно
# использовать функцию zip(). Вот пример программы, которая делает именно это:
#
# employee_numbers = [2, 9, 18, 28]
# employee_names = ["Дима", "Марина", "Андрей", "Никита"]
#
# zipped_values = zip(employee_names, employee_numbers)
# zipped_list = list(zipped_values)
#
# print(zipped_list)
#
# Функция zip возвращает следующее:
# [('Дима', 2), ('Марина', 9), ('Андрей', 18), ('Никита', 28)]
# Эта программа создала массив из кортежей, каждый из которых содержит имя и номер сотрудника. Здесь много составляющих,
# поэтому разберем по порядку. На первых двух строках объявляются переменные, которые хранят номера и имена сотрудников.
# На следующей — функция zip() объединяет два списка вместе, создавая новый массив кортежей.
#
# Функция zip с циклом for
# Работа с несколькими итерируемыми объектами — один из основных сценариев использования функции zip() в Python. Она
# даже может быть итератором кортежей или любых других итерируемых объектов, что часто используется в разработке ПО.
# Вот пример использования zip() для итерации по массивам:
#
# employee_numbers = [2, 9, 18, 28]
# employee_names = ["Дима", "Марина", "Андрей", "Никита"]
#
# for name, number in zip(employee_names, employee_numbers):
# 	print(name, number)
# Этот код вернет следующее:
#
# [('Дима', 2), ('Марина', 9), ('Андрей', 18), ('Никита', 28)]
# В этом примере программа перебирает список кортежей, которые возвращает zip() и делит их на два: имена и номера. Это
# упрощает процесс перебора нескольких итерируемых объектов за раз. Если необходимо, можно перебирать три и больше
# объектов.
#
# Как сделать «unzip»
# В последнем коде были объединены разные типы данных. Но как восстановить их прежнюю форму? Если есть список кортежей
# (упакованных), которые нужно разделить, можно использовать специальный оператор функции zip().
# Это оператор-звездочка (*). Вот пример работы оператора распаковки в zip():
#
# employees_zipped = [('Дима', 2), ('Марина', 9), ('Андрей', 18), ('Никита', 28)]
# employee_names, employee_numbers = zip(*employees_zipped)
#
# print(employee_names)
# print(employee_numbers)
# Этот код вернет такой результат:
#
# ("Дима", "Марина", "Андрей", "Никита")
# (2, 9, 18, 28)
# Это может казаться сложным, поэтому разберем по шагам. На первой строке определяется переменная, которая включает
# список кортежей. Затем еще две переменные: employee_names и employee_numbers. Им присваиваются значения функции
# распаковки.
# Функция распаковки — это просто zip-функция, которая принимает переменную employee_zipped и использует оператор
# распаковки *. После этого выводятся две новые переменные, которые включают имена и номера сотрудников.


# Функция reversed() возвращает обратный итератор, то есть возвращает итератор, который перебирает элементы оригинала в
# обратном порядке.
# Функция reversed() не создает копию и не изменяет оригинал последовательности.
# Объект seq должен иметь метод __reversed__() или поддерживает протокол последовательности, это метод __len__() и
# метод __getitem__() с целочисленными аргументами, начинающимися с 0.
# Перевернем список (реверс списка):
# >>> x = [15, 11, 13, 12, 14, 10]
# >>> x =list(reversed(x))
# >>> x
# # [10, 14, 12, 13, 11, 15]
# # теперь в обратную сторону
# >>> [i for i in reversed(x)]
# # [15, 13, 14, 11, 12, 10]
#
# Перевернем строку (реверс строки) с помощью reversed():
# x = 'forest'
#
# for i in reversed(x):
#     # вывод символов строки 'x'
#     # по одному в обратном порядке
#     print(i, end='')
#
# print('\n' + '-'*len(x))
# print(x)
# # tserof
# # ------
# # forest
#
# Если в итоге нужно снова получить строку, только перевернутую (запишем покороче):
# >>> x = 'абракадабра'
# >>> line = ''.join(reversed(list(x)))
# >>> line
# # 'арбадакарба'


# Функция all() возвращает значение True , если все элементы в итерируемом объекте - истинны, в противном случае она
# возвращает значение False.
# Если передаваемая последовательность пуста, то функция all() также возвращает True.
# Функция all() применяется для проверки на True ВСЕХ значений в последовательности и эквивалентна следующему коду:
#
# def all(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True
# Так же смотрите встроенную функцию any()
#
# В основном функция all() применяется в сочетании с оператором ветвления программы if ... else. Работу функции all() можно сравнить с оператором and в Python, только all() работает с последовательностями:
#
# >>> True and True and True
# # True
# >>> True and False and True
# # False
#
# >>> all([True, True, True])
# # True
# >>> all([True, False, True])
# # False
# Но между and и all() в Python есть два основных различия:
#
# Синтаксис.
# Возвращаемое значение.
# Функция all() всегда возвращает False или True (значение bool)
#
# >>> all([3, 1, 2, 6])
# # True
# >>> all([3, 0, 2, []])
# # False
# Оператор and , возвращает ПОСЛЕДНЕЕ истинное значение, при условии, что в выражении все значения True а если в выражении присутствует значение False (ложное значение), то ПЕРВОЕ ложное значение. Что бы добиться поведения как у функции all(), необходимо выражение с оператором and обернуть в функцию bool().
#
# >>> 3 and 1 and 2 and 6
# # 6
# >>> 3 and 0 and 3 and []
# # 0
#
# >>> bool(3 and 1 and 2 and 6)
# # True
# >>> bool(3 and 0 and 3 and [])
# # False
# Из всего сказанного можно сделать вывод, что для успешного использования функции all() необходимо в нее передавать последовательность, полученную в результате каких то вычислений/сравнений, элементы которого будут оцениваться как True или False. Это можно достичь применяя функцию map() или выражения-генераторы списков, используя в них встроенные функции или методы, возвращающие bool значения, операции сравнения, оператор вхождения in и оператор идентичности is.
#
# num = [1, 2.0, 3.1, 4, 5, 6, 7.9]
# # использование встроенных функций или
# # методов на примере 'isdigit()'
# >>> [str(x).isdigit() for x in num]
# # [True, False, False, True, True, True, False]
#
# # использование операции сравнения
# >>> [x > 4 for x in num]
# # [False, False, False, False, True, True, True]
#
# # использование оператора вхождения `in`
# >>> ['.' in str(x) for x in num]
# # [False, True, True, False, False, False, True]
#
# # использование оператора идентичности `is`
# >>> [type(x) is int for x in num]
# # [True, False, False, True, True, True, False]
#
# # использование функции map()
# >>> list(map(lambda x: x > 1, num))
# # [False, True, True, True, True, True, True]
# Примеры проводимых проверок функцией all().
# Допустим, у нас есть список чисел и для дальнейших операций с этой последовательностью необходимо знать, что все числа например положительные.
#
# >>> num1 = range(1, 9)
# >>> num2 = range(-1, 7)
# >>> all([x > 0 for x in num1])
# # True
# >>> all([x > 0 for x in num2])
# # False
# Или проверить, что последовательность чисел содержит только ЦЕЛЫЕ числа.
#
# >>> num1 = [1, 2, 3, 4, 5, 6, 7]
# >>> num2 = [1, 2.0, 3.1, 4, 5, 6, 7.9]
# >>> all([type(x) is int for x in num1])
# # True
# >>> all([type(x) is int for x in num2])
# # False
# Или есть строка с числами, записанными через запятую и нам необходимо убедится, что в строке действительно записаны только цифры. Для этого, сначала надо разбить строку на список строк по разделителю ',' и проверить каждый элемент полученного списка на десятичное число методом str.isdigit(). Что бы учесть правила записи десятичных чисел будем убирать точку перед проверкой строки на десятичное число.
#
# >>> line1 = "1, 2, 3, 9.9, 15.1, 7"
# >>> line2 = "1, 2, 3, 9.9, 15.1, 7, девять"
# >>> all([x.replace('.', '').strip().isdigit() for x in line1.split(',')])
# # True
# >>> all([x.replace('.', '').strip().isdigit() for x in line2.split(',')])
# # False
# Еще пример со строкой. Допустим нам необходимо узнать, есть ли в строке наличие открытой И закрытой скобки?
#
# >>> simbols = ['(', ')']
# >>> line1 = "функция 'all()' всегда возвращает 'False' или 'True'"
# >>> line2 = "функция any всегда возвращает значение bool"
# >>> all([x in line1 for x in simbols])
# # True
# >>> all([x in line2 for x in simbols])
# # False


# Описание:
# Функция any() возвращает True, если какой-либо (любой) элемент в итерируемом объекте является истинным True, в противном случае any() возвращает значение False.
#
# Если последовательность пуста, то функция any() возвращает False.
#
# Функция any() применяется для проверки истинности ЛЮБОГО из значений в итерируемом объекте и эквивалентна следующему коду:
#
# def any(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False
# Так же смотрите встроенную функцию all().
#
# В основном функция any() применяется в сочетании с оператором ветвления программы if ... else. Работу функции any() можно сравнить с оператором or в Python, только any() работает с последовательностями:
#
# >>> False or True or False
# # True
# >>> any([False, True, False])
# # True
# Но между or и any() в Python есть два основных различия:
#
# Синтаксис.
# Возвращаемое значение.
# Функция any() всегда возвращает False или True.
#
# >>> any([0, 2, 1, 0, 0])
# # True
# >>> any([0, 0, ''])
# # False
# Оператор or возвращает ПЕРВОЕ истинное значение, а если все значения False, то ПОСЛЕДНЕЕ ложное значение.
#
# >>> 0 or 2 or 1 or 0 or 0
# # 2
# >>> 0 or 0 or ''
# # ''
#
#
# >>> bool(0 or 2 or 1 or 0 or 0)
# # True
# >>> bool(0 or 0 or '')
# # False
# Из всего сказанного можно сделать вывод, что для успешного использования функции any() необходимо в нее передавать последовательность, полученную в результате каких то вычислений/сравнений, элементы которого будут оцениваться как True или False. Это можно достичь применяя функцию map() или выражения-генераторы списков, используя в них встроенные функции языка, возвращающие bool значения, операции сравнения, оператор вхождения in и оператор идентичности is.
#
# num = [1, 2.0, 3.1, 4, 5, 6, 7.9]
# # использование встроенных функций
# # на примере 'isdigit()'
# >>> [str(x).isdigit() for x in num]
# # [True, False, False, True, True, True, False]
#
# # использование операции сравнения
# >>> [x > 4 for x in num]
# # [False, False, False, False, True, True, True]
#
# # использование оператора вхождения `in`
# >>> ['.' in str(x) for x in num]
# # [False, True, True, False, False, False, True]
#
# # использование оператора идентичности `in`
# >>> [type(x) is int for x in num]
# # [True, False, False, True, True, True, False]
#
# # использование функции map()
# >>> list(map(lambda x: x > 1, num))
# [False, True, True, True, True, True, True]
# Примеры проводимых проверок функцией any().
# Допустим у нас есть строка например с адресом и нам необходимо узнать, содержит ли адрес номер дома. Для этого разделим строку с адресом справа на лево методом str.rsplit() по разделителю ' ' один раз.
#
# >>> addr1 = '142100, г. Москва, ул. Свердлова, 15'
# >>> addr2 = '142100, г. Москва, ул. Свердлова'
# >>> any(map(str.isdigit, addr1.rsplit(' ',1)))
# # True
# >>> any(map(str.isdigit, addr2.rsplit(' ',1)))
# # False
# Второй пример с числовой последовательностью. Необходимо узнать, есть ли в последовательности числа больше определенного значения.
#
# >>> num1 = range(0, 20, 2)
# >>> num2 = range(0, 15, 2)
# >>> any([x > 15 for x in num1])
# # True
# >>> any([x > 15 for x in num2])
# # False
# Так же можно проверять строку на наличие, каких то определенных символов.
#
# >>> simbols = ['(', ')', '\'']
# >>> line1 = "функция 'any()' всегда возвращает 'False' или 'True'"
# >>> line2 = "функция any всегда возвращает значение bool"
# >>> any([x in line1 for x in simbols])
# # True
# >>> any([x in line2 for x in simbols])
# # False
