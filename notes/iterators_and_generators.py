# Интерпретатор узнает какие именно элементы лежат в множестве (списках, словарях, строках и т.п.) с помощью итератора.
# Если мы хотим перебирать элементы какого-то объекта Х с помощью цикла for, необходимо, чтобы у объекта Х был итератор.
# Итератор - это такой объект перечислитель. Мы можем спросить у итератора, какой объект является следующим в объекте Х
# и он должен будет его вернуть. А если элементы в объекте Х уже кончились, то он должен бросить ошибку StopIteration:
# Для получения итератора объекта используют функцию iter()
# Чтобы спросить следующий объект у итератора, используют функцию next()

# my_list = [1, 2, 3]
# for i in my_list:
#     print(i)  # через for
# iterator = iter(my_list)
# while True:
#     try:
#         i = next(iterator)
#     except StopIteration:
#         break
#     else:
#         print(i)  # через next
# В результате выполнения получаем идентичный результат. Синтаксически первая конструкция более простая. Однако,
# понимание того, что мы используем итераторы и функцию next() для того, чтобы перебирать элементы, позволит нам в
# дальнейшем писать свои собственные итераторы для того, чтобы перебирать элементы наших собственных классов.

# from random import random
# class RandomIterator:
#     def __iter__(self):
#         return self
#     def __init__(self, k):
#         self.k = k
#         self.i = 0
#     def __next__(self):
#         if self.i < self.k:
#             self.i += 1
#             return random()
#         else:
#             raise StopIteration
# for x in RandomIterator(10):
#     print(x)
# Чтобы объект можно было проитерировать, т.е. перечислить его элементы, у него должен быть определен метод  __iter__,
# который возвращает итератор. А для того, чтобы объект считался итератором, у него должен быть определен метод __next__
# Эти две функции (__iter__ и __next__) могут быть определены в одном и том же классе, тогда экземпляры этого класса
# одновременно будут являться и итерируемыми и итераторами, но это каша, так не делают, итераторы - это отдельные классы

# class DoubleElementListIterator:
#     def __init__(self, lst):
#         self.lst = lst
#         self.i = 0
#     def __next__(self):
#         if self.i < len(self.lst):
#             self.i += 2
#             try:
#                 return self.lst[self.i - 2], self.lst[self.i - 1]
#             except IndexError:
#                 return self.lst[self.i - 2], ''
#         else:
#             raise StopIteration
# class MyList(list):
#     def __iter__(self):
#         return DoubleElementListIterator(self)
# for pair in MyList([1, 2, 3, 4, 5]):
#     print(pair)
# Чтобы элементы экземпляра какого-либо класса (list, str, MyClass итд) можно было перебрать (итерировать), в этом
# классе должна быть функция __iter__, которая должна возвращать итератор. Итератор - это класс, в котором определена
# функция __next__. Видим, что мы перебираем объекты из списка парами.  Таким образом, мы можем сами определить
# поведение для своего класса, если мы перебираем в нем элементы с помощью цикла for.
# Метод __iter__() запускается один раз при создании экземпляра класса MyList и в этот момент этот созданный экземпляр
# становится "итерируемым" (интерпретатор запоминает все, что ему нужно для работы про этот объект). Дальше вы уже
# работаете с этим экземпляром и все что вы делаете, в том числе итерируетесь по нему (вызываете метод next), связано
# именно с этим экземпляром. При создании нового экземпляра __iter__() будет запущен еще раз, но этот вызов будет связан
# именно с этим новым экземпляром и никак не повлияет на счетчики ранее созданных экземпляров.

# Подробное объяснение происходящего, с переделанным в логичном виде примером про RandomIterator:
# Создание собственного итератора - это создание класса - итератора. Чтобы экземпляр класса можно было проитерировать
# у этого класса должен быть определен метод ** iter **, который возвращает итератор экземпляра. Чтобы объект являлся
# итераторм в нем должен быть определ метод ** next **, который осуществляет переход к следующему элементу и выводит
# ошибку в случае, если элементы интируемого множества уже проитерированны. Создадим класс, основанный на типе данных
# lsit, экземпляры которого будут итерироваться парами.
# Сначала создадим итератор, в котором определим метод next и условие окончания итерации

# class DoubleElementListIterator:
#     # В init определим атрибуты итератора на основе значений которых будет работать метод next
#     def __init__(self, lst):
#         # Прежде всего передадим итератору в качестве атрибута сам итерируемый список
#         self.lst = lst
#         # Затем опредилм атрибут - номер текущего элемента в листе
#         self.i = 0
#     # Прописываем правило итерирования и остановки
#     def __next__(self):
#         # Если счетчик итераций не дошел до последнего элемента листа,
#         # то в качестве следующего значения вернем пару из двух элементов стоящих перед текущим
#         if self.i < len(self.lst):
#             self.i += 2
#             return self.lst[self.i - 2], self.lst[self.i - 1]
#         # если достигнут последний элемент в листе останавливаем итерацию
#         else:
#             raise StopIteration
# # Теперь создаем класс, экземпляры которого мы хотим итерировать образом описанным выше
# class MyList(list):
#     # Определяем метод итератор, который ссылается на уже описанный итератор
#     def __iter__(self):
#         return DoubleElementListIterator(self)
# for pair in MyList([1, 2, 3, 4, 5, 6]):
#     print(pair)

# Пример с генератором рандомных чисел.Экземпляры объекта MyClass являются целыми числами и при итерировании этих
# экзмепляров, их значение(целое число) означает количество итераций - вывода рандомного числа от 0 до 1

# from random import random
# class RandomIterator:
#     def __init__(self, k):
#         self.k = k
#         self.i = 0
#     def __next__(self):
#         if self.i < self.k:
#             self.i += 1
#             return random()
#         else:
#             raise StopIteration
# class MyClass(int):
#     def __iter__(self):
#         return RandomIterator(self)
# for x in MyClass(3):
#     print(x)

# Также проитерироваться можно по упорядоченной последовательности для которой определен метод __getitem__:
# class IndexIterable:
#     def __init__(self, obj):
#         self.obj = obj
#     def __getitem__(self, index):
#         return self.obj[index]
# for letter in IndexIterable('str'):
#     print(letter)

# - итератор - это объект в котором реализован метод "next"
# - объект "итерируемый" - если в нем реализован метод __iter__.
# - если в итераторе нет метода iter - он не итерируемый, несмотря на наличие метода next, поэтому пришлось добавить его
# самого в себя (досадная бюрократическая формальность)
# - сильно запутывает то, что судя по всему Итератор не является наследником какого-то Великого Итератора.
# Есть next - итератор, нет - значит и нет. Т.е. это самостоятельный тип объекта ни от чего не наследуемый, кроме
# абстрактного Objects. И как я понял по определению он не может быть совмещен в объектом существующего класса
# (того же листа, пробовал - матерится). Но может быть реализован внутри объекта, который ни от кого не наследуется.
# Но тогда это будет в первую очередь итератор, а во вторую - все остальное.

# self.lst = lst - Это действительно ссылка на список, а не копия списка?
# class MyClass:
#     def __init__(self, lst):
#         self.lst = lst
#         print(id(self.lst))
#
# my_list = [1, 2, 3]
# print(id(my_list))  # 1694156482248
# my_class = MyClass(my_list)  # 1694156482248
#
#
# class Integer(int):
#     def show(self):
#         print(self)
# one = Integer(1)
# one.show()  # 1
# show - самописный, у int-а такого нет. Как работает, ну начнем со строчки one = Integer(1) в момент Integer(1) python
# создает экземпляр Integer, вызывая у него __init__()  и передавая туда аргументом 1,  но как видно init-а там нет
# - поэтому он вызовет родительский init int-а, который умеет принимать разные вещи (ну float-ы например) и собственно
# создает экземпляр со значением 1. Далее в show мы просим напечатать self - то есть самого себя (вернее передаем ссылку
# на себя) - экземпляр Integer со значением 1 - это он собственно и делает.
# Где хранит значение? - ну Integer этого не умеет, а вот Int умеет (как это устроено - отдельная тема) - там и хранит
# :) С наследованием от листа - аналогично. Что не умеет наследник - берется в листе.
# Ещё раз главное в двух словах: self - ссылка на экземпляр объекта. Когда где либо возвращается или печатается или ещё
# что-то делается с этим self - собственно это делается с этим экземпляром.
# Ещё немного запутывающей магии:

# class MyClass:
#     def __init__(self):
#         self.attr = 'some string'
#
#     def __str__(self):  # magic метод отвечающий за то, как будет вести себя экземпляр когда его запихнут в print()
#         return self.attr
#
#     def show(self):
#         print(self)  # собственно тут запихиваем экземпляр в print - что произойдет при вызове show?
#
# mc = MyClass()
# mc.show()  # идем в MyClass, находим show() - в параметр self передаем ссылку на экземпляр mc,
#           # в теле метода передаем её же в print(), print ищет в MyClass метод __str__() -
#           # передает ему эту же ссылку вместо self, ну а __str__() уже знает что делать -
#           # найти у переданного экземпляра атрибут и вернуть его

# Генераторы - это функции, в которых вместо слова return мы используем ключевое слово yield.
# И при этом вместо того, чтобы значение возвращать, функция будет генерировать следующее значение.

# from random import randint
# def random_generator(k):
#     for i in range(k):
#         yield randint(1, 10)
# x = random_generator(3)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# Таким образом, отличие генератора от обычной функции заключается в том, что с помощью ключевого слова yield, которое
# мы используем вместо ключевого слова return, мы можем вернуть значение из функции сразу несколько раз. А спрашивать
# какое именно значение будет следующим мы будем именно с помощью функции next().
# Также важно понимать, что интерпретатор смотрит сразу на все тело функции. И если он встречает хотя бы один раз внутри
# тела функции слово yield, то он понимает, что эта функция является генератором. А вызов генератора ведет себя не
# также, как вызов обычной функции.
# Когда мы вызываем функцию с ключевым словом yield внутри, нам возвращается объект генератор. Этот объект генератор
# примечателен тем, что он знает целиком все тело нашей функции. И исполнение тела функции начнется лишь тогда, когда мы
# попросим у генератора следующий элемент. В этот момент он начнет с самого начала исполнять нашу функцию - до первого
# ключевого слова yield. Когда он встретит слово yield, он вернет значение наружу, туда где мы вызывали функцию next().
# Самое главное, когда мы возвращаем значение, мы также запоминаем и все состояние нашей функции. Чтобы затем, когда мы
# вызовем next() в следующий раз, мы продолжим не с начала функции, а с того места, где мы до этого остановились.
# Затем, если в какой-то момент мы не найдем ключевое слово yield, мы бросим ошибку StopIteration.
# Таким образом, с помощью генераторов в языке Python реализуется концепция так называемого отложенного исполнения.
# Мы продолжим исполнение функции лишь тогда, когда нам в действительности понадобится следующее значение.
# Генераторы - это удобный синтаксис для написания итераторов. Вместо того, чтобы реализовывать класс, содержащий в себе
# методы __iter__ и __next__, достаточно написать функцию, которая вместо return использует ключевое слово yield. Тем
# самым давая понять, что она будет производить сразу несколько значений, которые нужно вернуть из функции.
# Важно понимать, что генератор заканчивает исполнение своей функции ровно тогда же, когда и обычная функция заканчивает
# исполнение своего тела. Он бросает ошибку StopIteration либо, когда дошел до конца тела функции,
# либо когда встретит конструкцию return.
# То что мы передаем внутрь конструкции return будет сообщением внутри ошибки StopIteration.
# Важно помнить, что исполнение тела функции генератора происходит только тогда, когда мы вызываем next(). И происходит
# это от одного yield до следующего. А если следующий yield не найден, то тогда он заканчивает свое исполнение и бросает
# ошибку StopIteration.


# Одним из самых часто используемых классов в Python является класс filter. Он принимает в конструкторе два аргумента
# a и input_file – последовательность и функцию, и позволяет проитерироваться только по таким элементам x из последовательности a
# что input_file(x) равно True. Будем говорить, что в этом случае функция input_file допускает элемент x, а элемент x является допущенным.
# В данной задаче мы просим вас реализовать класс multifilter, который будет выполнять ту же функцию, что и стандартный
# класс filter, но будет использовать не одну функцию, а несколько.
# Решение о допуске элемента будет приниматься на основании того, сколько функций допускают этот элемент, и сколько не
# допускают. Обозначим эти количества за pos и neg.
# Введем понятие решающей функции – это функция, которая принимает два аргумента – количества pos и neg, и возвращает
# True, если элемент допущен, и False иначе.
#
# class multifilter:
#     def judge_half(self, pos, neg):
#         return pos >= neg  # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
#
#     def judge_any(self, pos, neg):
#         return pos >= 1  # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
#
#     def judge_all(self, pos, neg):
#         return neg == 0  # допускает элемент, если его допускают все функции (neg == 0)
#
#     def __init__(self, iterable, *funcs, judge=judge_any):
#         self.iterable = iterable  # iterable - исходная последовательность
#         self.funcs = tuple(funcs)  # funcs - допускающие функции
#         self.judge = judge  # judge - решающая функция
#
#     def __iter__(self):
#         for element in self.iterable:
#             pos, neg = 0, 0
#             for func in self.funcs:
#                 if func(element):
#                     pos += 1
#                 else:
#                     neg += 1
#             if self.judge(self, pos, neg):
#                 yield element  # возвращает итератор по результирующей последовательности
#
#
# def mul2(x):
#     return x % 2 == 0
#
# def mul3(x):
#     return x % 3 == 0
#
# def mul5(x):
#     return x % 5 == 0
#
# a = [i for i in range(31)]  # [0, 1, 2, ... , 30]
#
# print(list(multifilter(a, mul2, mul3, mul5)))
# # # [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]
# print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# # # [0, 6, 10, 12, 15, 18, 20, 24, 30]
# print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# # # [0, 30]

# Пример правильного решения
#
# class multifilter:
#     def judge_half(pos, neg):
#         return pos >= neg
#
#     def judge_any(pos, neg):
#         return pos > 0
#
#     def judge_all(pos, neg):
#         return neg == 0
#
#     def __init__(self, iterable, *funcs, judge=judge_any):
#         self.iterator = iter(iterable)
#         self.funcs = funcs
#         self.judge = judge
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while (True):
#             elem = next(self.iterator)
#             pos, neg = 0, 0
#             for func in self.funcs:
#                 if func(elem):
#                     pos += 1
#                 else:
#                     neg += 1
#
#             if self.judge(pos, neg):
#                 return elem

# Итератор - это отдельный класс, в котором есть функция __next__, которая возвращает по порядку элементы переданного
# итерируемого объекта. Например, создайте простейший итератор - класс MyIterator, который возвращает элементы
# переданного ему итерируемого объекта(iterable), и никакой логики внутри(по честному будет сказать, что в этом примере
# итератор ждет не просто итерируемый объект, а список, потому что в next он использует доступ к элементам по индексу):

# class MyIterator:
#     def __init__(self, iterable):
#         self.index = 0
#         self.iterable = iterable
#
#     def __next__(self):
#         if self.index < len(self.iterable):
#             self.index += 1
#             return self.iterable[self.index - 1]
#         raise StopIteration

# Теперь создайте свой класс MyList ни от чего не наследуя и просто определите внутри функцию __iter__ сделав тем самым
# объекты этого класса итерируемыми, а внутри __iter__ возвращайте свой ранее созданный итератор MyIterator передавая в
# него итерируемый объект, например список:

# class MyList:
#     def __init__(self, lst):
#         self.lst = lst
#
#     def __iter__(self):
#         return MyIterator(self.lst)

# А теперь создайте объект типа MyList передав в него, например, список:
# l = MyList([1, 2, 3, 4, 5])

# Полный код:

# class MyIterator:
#     def __init__(self, iterable):
#         self.index = 0
#         self.iterable = iterable
#
#     def __next__(self):
#         if self.index < len(self.iterable):
#             self.index += 1
#             return self.iterable[self.index - 1]
#         raise StopIteration
#
#
# class MyList:
#     def __init__(self, lst):
#         self.lst = lst
#         self.index = 0
#
#     def __iter__(self):
#         return MyIterator(self.lst)
#
#
# l = MyList([1, 2, 3, 4, 5])
# print(type(l))  # "l" is not a list, but MyList object

# but "l" contains elements and "l" is iterable
# for i in l:
#     print(i)

# Теперь глядя на весь этот код должно стать понятно, что объект "l" - это НЕ список:
# - l - это объект типа MyList
# - он итерируемый(определен метод __iter__)
# - для итерации по элементам объекта типа MyList используется итератор MyIterator
# - итератор MyIterator возвращает по одному элементу переданного в него итерируемого объекта(в нашем случае списка,
# который мы задавали при создании объекта "l")

# Поняв это вы легко сможете перенести функцию __next__ внутрь класса MyList, сделав тем самым класс MyList еще и
# итератором(теперь, когда объекты класса MyList являются итераторами, то функция __iter__ может возвращать сам объект
# класса MyList, то есть "return self").Конечно же надо позаботиться о переменных, которые используются в __next__:

# class MyList:
#     def __init__(self, lst):
#         self.iterable = lst
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.iterable):
#             self.index += 1
#             return self.iterable[self.index - 1]
#         raise StopIteration


# Ну а теперь добавьте логику в функцию next, например, каждый элемент делить на 2 перед выводом:

# class MyList:
#     def __init__(self, lst):
#         self.iterable = lst
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.iterable):
#             self.index += 1
#             return self.iterable[self.index - 1] / 2
#         raise StopIteration
#
# l = MyList([1, 2, 3, 4, 5])
#
# for i in l:
#     print(i)

# 0.5
# 1
# 1.5
# 2
# 2.5

# Добавляя сложности, дальше можно определить функцию f2 и использовать в __next__, которая будет делить на 2 и
# результат подставлять в return в __next__:

# class MyList:
#     def __init__(self, lst):
#         self.iterable = lst
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def f2(self, n_test):
#         return n_test / 2
#
#     def __next__(self):
#         if self.index < len(self.iterable):
#             self.index += 1
#             return self.f2(self.iterable[self.index - 1])
#         raise StopIteration
#
#
# l = MyList([1, 2, 3, 4, 5])
#
# for i in l:
#     print(i)

# Еще сложнее, вынесем функцию f2 за класс, а внутрь класса будем передавать ее аргументом, плюс добавим внутрь класса
# еще одну функцию judge, которая будет использовать нашу f2 и тоже что - то делать(не забывайте инициализировать новые
# переменные в __init__):

# class MyList:
#     def __init__(self, lst, func):
#         self.iterable = lst
#         self.func = func
#         self.index = 0
#
#     def judge(self, num):
#         return "element = " + str(num)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.iterable):
#             self.index += 1
#             self.result_of_f2 = self.func(self.iterable[self.index - 1])
#             self.result_of_judge = self.judge(self.result_of_f2)
#             return self.result_of_judge
#         raise StopIteration
#
#
# def f2(n_test):
#     return n_test / 2
#
#
# l = MyList([1, 2, 3, 4, 5], f2)
#
# for i in l:
#     print(i)

# !!! НО ИМЕЙТЕ В ВИДУ !!! Если класс итерируемый(__iter__) И ОН ЖЕ является итератором(__next__), то итерироваться по
# элементам объекта этого класса возможно будет только ОДИН раз.В указанном примере  попробуйте заменить for i in l на
# две строки print(list(l)):
# print(list(l))
# print(list(l))
# Получите вывод:
# ['element = 0.5', 'element = 1.0', 'element = 1.5', 'element = 2.0', 'element = 2.5']
# []
# А если использовать внешний итератор, то все ок.

# Решето Эратосфена:
# n_test = int(input("n_test="))
# a = range(n_test+1)
# a[1] = 0
# lst = []
#
# i = 2
# while i <= n_test:
#     if a[i] != 0:
#         lst.append(a[i])
#         for j in range(i, n_test+1, i):
#             a[j] = 0
#     i += 1
# print(lst)

# Листинг 7
# n_test = input("n_test=")
# lst=[2]
# for i in range(3, n_test+1, 2):
# 	if (i > 10) and (i%10==5):
# 		continue
# 	for j in lst:
# 		if j*j-1 > i:
# 			lst.append(i)
# 			break
# 		if (i % j == 0):
# 			break
# 	else:
# 		lst.append(i)
# print lst

# Реализуйте функцию-генератор primes, которая будет генерировать простые числа в порядке возрастания, начиная с числа 2.
# import itertools
#
# def primes():
#     lst, i = [2], 1
#     if i == 1:
#         yield 2
#     while True:
#         i += 2
#         if (i > 10) and (i % 10 == 5):
#             continue
#         for j in lst:
#             if j * j - 1 > i:
#                 lst.append(i)
#                 yield i
#                 break
#             if i % j == 0:
#                 break
#         else:
#             lst.append(i)
#             yield i
#
# print(list(itertools.takewhile(lambda x: x <= 131, primes())))

# В данном решении используется наблюдение: если у числа xx , есть какой-либо делитель отличный от 1 и xx, то этот
# делитель обязательно не больше чем корень из x.
# def primes():
#     yield 2
#     prime = 3
#     while True:
#         is_prime = True
#         divisor = 3
#         while divisor ** 2 <= prime:
#             if prime % divisor == 0:
#                 is_prime = False
#                 break
#             divisor += 2
#         if is_prime:
#             yield prime
#         prime += 2

# list comprehension (генерация списков)
# List comprehension - это компактный способ обработки списков.
# Основные преимущества List comprehension перед обычной конструкцией(цикл for + if +обработка):
# скорость(List comprehension быстрее, чем for )
# краткость(в 1 строку можно записать довольно развесистую конструкцию, некоторые считают её лучше читаемой)
# Примером List comprehension может служить конструкция вида: [n_test for n_test in range(1, 10000) if n_test % 2 == 0]
# При этом условия может и не быть, например: [str(n_test) for n_test in range(10)]
# Примеры list comprehension
# Простая генерация списка:
# x = [-2, -1, 0, 1, 2]
# y = [i * i for i in x]
# print(y)
# Генерация с использованием условия в конце:
# x = [-2, -1, 0, 1, 2]
# y = [i * i for i in x if i > 0]
# print(y)
# Более сложная конструкция:
# z = [(x, y) for x in range(3) for y in range(3) if y >= x]
# print(z)
# Данная конструкция будет эквивалентна следующему коду:
# z = []
# for x in range(3):
#     for y in range(3):
#         if y >= x:
#             z.append((x, y))
# print(z)
# Если мы эту конструкцию поместим не квадратные скобки, а в круглые, то мы получим генератор, который будет перебирать
# подходящие под условие объекты:
# z = ((x, y) for x in range(3) for y in range(3) if y >= x)
# print(z)
# print(next(z))
# print(next(z))
# Кроме списков и генераторов, такой же синтаксис в Python 3 возможен для множеств и словарей (перебирать можно
# элементы любого "итератора") :
# import builtins
# x = {ord(x) for x in 'spaam'}  # генерируем set {112, 115, 109, 97}
# y = {x: ord(x) for x in 'spaam'}  # генерируем dictionary {'s': 115, 'm': 109, 'p': 112, 'a': 97}
# print(x)
# print(y)
# Если список содержит последовательно пары name value, то так можно преобразовать в словарь:
# d = ['Dota', 'sucks', 'Python', 'rules', 'Saperavi', 'depends']
# dictus = {d[x]: d[x+1] for x in range(0, len(d), 2)}
# print(dictus)
# Кстати, генератор можно использовать внутри функции без дополнительных скобок:
# mylist = [1, 2, 3]
# mysum = summa(x**2 for x in mylist)
# print(mysum)  # 14
# Условие if не всегда идет вначале. Иногда полезна такая конструкция
# [int(x) if x.isdigit() else x for x in a].  x.isdigit() - тут как пример
# Да, странно что не упомянули что выражение-генератор можно проитерировать(обойти) только один раз.
# То есть, если ниже в коде вы захотите обойти этот генератор z, из примера в видео, два раза, например циклом for
# ,то ничего не получится.
# Проверка времени исполнения показывает, что listcomp действительно формирует список быстрей
# def ko():
#     m = [(x, y) for x in range(3) for y in range(3) if y >= x]
# if __name__ == '__main__':
#     from timeit import Timer
#     t = Timer("ko()", "from __main__ import ko")
#     print(t.timeit())

# x = [-2, -1, 0, 1, 2]
# z = (i for i in'abvcf')
# print(z) # <generator object <genexpr> at 0x000001725FE7CC80>
# print(type(z)) # <class 'generator'>
# def pr():
#     for i in range(5):
#         yield i
# print(pr) # <function pr at 0x000001725F99A040>
# print(type(pr)) # <class 'function'>
# print(type(pr())) # <class 'generator'>
# print(pr()) # <generator object pr at 0x000001E37BEF0890>
# def pro_2():
#     for i in range(5):
#         return i
# print(type(pro_2())) # <class 'int'>
# print(next(pr())) # 0
# print(next(pr)) # TypeError: 'function' object is not an iterator
# Сама функция с yield все еще функция. Уже ,при вызове, возвращает генератор.

# a = iter([1, 2, 3])
# print(a) # <list_iterator object at 0x00000278FF682FA0>
# print(next(a)) # 1
# print(*a) # 2 3
# print(type(a)) # <class 'list_iterator'>
# print(next(pr())) # 0
# print(next(pr())) # 0
# print(*pr()) # 0 1 2 3 4
# print(next(a)) # StopIteration
# Тут видна разница генератора и итератора. Можно понять предыдущее задание. Когда yield в __iter__ пишем без __netx__.
# В а будем перемещаться, пока не словим ошибку. В __next__ прописуем стоп. Посмотрел в визуализаторе c __iter__ прыгает
# в __next__ и если не прописать стоп, будет бесконечный цикл.

# a = [i for i in range(5)][1:]
# a = list(i + 1 for i in range(4))
# print(a)

# Вы можете сами оценить время работы скрипта, используя простую конструкцию:
# start_time = time.time()  # вычисляем время на начало вычислений
# код, время выполнения которого Вы оцениваете
# elapsed_time = time.time() - start_time  # считаем сколько времени прошло с начала вычислений

# Итераторы и генераторы
# Итератор – это интерфейс, который позволяет перебирать элементы последовательности. Он используется, например, в
# цикле for ... in ..., но этот механизм скрыт от глаз разработчика. При желании итератор можно получить "в сыром виде",
# воспользовавшись функцией iter().
#
# Чтобы получить следующий элемент коллекции или строки, нужно передать итератор функции next().
#
# Под капотом функциональность реализуется в методах __iter__ и __next__.
# Пример простого итератора:
# class SimpleIterator:
#     def __iter__(self):
#         return self
#
#     def __init__(self, limit):
#         self.limit = limit
#         self.counter = 0
#
#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter += 1
#             return 1
#         else:
#             raise StopIteration

# На базе итераторов в языке появились новые элементы синтаксического сахара: выражения-генераторы и генераторы
# коллекций. Они позволяют устанавливать условия для отбора.
#
# numbers = range(10)
# squared = [n ** 2 for n in numbers if n % 2 == 0]
# print(squared)   # [0, 4, 16, 36, 64]
# В этом примере из списка чисел отбираются четные, а в финальную коллекцию вносятся их квадраты.
#
# Выражения-генераторы не создают целый список заданной длины сразу, а добавляют элементы по мере необходимости.
#
# Очевидно, что генераторы могут выполнять работу функций map и filter. Более того, они справляются с этой задачей
# эффективнее.