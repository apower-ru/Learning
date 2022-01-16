# Документация как устроены ссылки и другие Uniform Resource Identifiers : https://tools.ietf.org/html/rfc3986
# Как клиент и сервер обмениваются информацией? http является текстовым протоколом. Поэтому сначала клиент посылает
# запрос в текстовом формате определенного вида. А затем к нему приходит ответ - также в текстовом формате.
# Метод GET означает, что мы хотим получить данный ресурс.
# Если ресурс является html страницей, то с помощью метода GET мы получим html код данной страницы. Если запрашиваем
# картинку, то получим бинарные данные этой картинки.
# Чаще всего метод GET никаким образом не изменяет сами данные, которые хранятся на сервере.
# А вот метод POST для этого и предназначен. Он изменяет данные, которые мы запрашиваем. Например, в форме смены пароля,
# когда мы его заполняем и нажимаем кнопку Enter, чаще всего будет использоваться метод POST. Также он используется для
# банковских транзакций, связанный с вашей картой.
# HTML - это язык разметки гипертекста (hyper text markup language). Используется, прежде всего, для составления
# веб-страниц.

# Проверим ответ страницы https://docs.python.org/3/ и тип ее содержимого:
# import requests
# res = requests.get('https://docs.python.org/3.5/')
# print(res.status_code)
# print(res.headers['Content-Type'])
# requests возвращает нам Response object.
# Response - это класс, который описан внутри библиотеки requests и он содержит в себе описание ответа сервера.
# Чтобы получить тело ответа, можем использовать атрибут content
# print(res.content)
# Он возвращает бинарные данные
# Этот метод полезен для чтения изображений, музыки и т.д.
# Однако, если мы уверены в том, что объект, который мы запрашиваем, является текстовым, то мы можем явно использовать
# атрибут text. Он выведет html содержимое страницы:
# print(res.text)
# Теперь вместо текста считаем картинку https://docs.python.org/3/_static/py.png и убедимся, что мы получим изображение
# в виде бинарного файла
# res = requests.get('https://docs.python.org/3.5/_static/py.png')
# print(res.headers['Content-Type'])
# print(res.content)
# Мы можем очень легко сохранить этот файл к себе на компьютер:
# with open('python.png', 'wb') as f:
#     f.write(res.content)
# В запросе можно использовать параметры. Они индивидуальные для каждого сайта:
# res = requests.get("https://yandex.ru/search/",
#                    metric={
#                        "text": "Stepic",
#                        # "test": "test1",
#                        # "name": "Name With Spaces",
#                        # "list": ["test1", "test2"]
#                    })
# print(res.status_code)
# print(res.headers['Content-Type'])
# print(res.url)

# Рекомендую поиграться с этим онлайн-конструктором регулярных выражений. https://regex101.com/r/rMAHrE/1 Указанный
# пример элементарно адаптируется под Питон. Но должен признать, что RE не слишком удобны для разбора HTML. Опытные
# коллеги рекомендуют для этой цели использовать более подходящие библиотеки: BeautifulSoup, HTMLParser и LXML.
# Уйму времени убил, пока не дошло, что requests.get().content по крайней мере в данной задаче не работает, как
# ожидалось, а нужно использовать  requests.get().text.  Даже преобразование str(requests.get().content) не помогло.

# Рассмотрим два HTML-документа A и B.
# Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно с
# дополнительными параметрами внутри тега.
# Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход и
# из C в B можно перейти за один переход.
# Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
# Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.
# Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.
# import requests
# import re
# a, b = input(), input()  # https://stepic.org/media/attachments/lesson/24472/sample0.html
# a = requests.get(a)
# new_res = []
# for i in re.findall(r'https.+?html', str(a.content)):
#     res = requests.get(i)
#     if res.status_code == 200:
#         new_res.extend(re.findall(r'https.+?html', str(res.content)))
# print('Yes' if b in new_res else "No")
#
# start_url = input()  # пример правильного решения: обратите внимание на регулярное выражение проверки html-ссылки
# end_url = input()
# found = False
# link_pattern = re.compile(r'<a[^>]*?href="(.*?)"[^>]*?>')
# resp = requests.get(start_url).text  # <a href="https://stepic.org/media/attachments/lesson/24472/sample1.html">1</a>
# for url in link_pattern.findall(resp):  # ['https://stepic.org/media/attachments/lesson/24472/sample1.html']
#     cur_resp = requests.get(url).text
#     if end_url in link_pattern.findall(cur_resp):
#         found = True
#         break
# print("Yes" if found else "No")
#
# urls = [input() for cmd in range(2)]
# p = 'No'
# for i in re.findall(r'<a.*href="(.*)">', requests.get(urls[0]).text):
#     if urls[1] in re.findall(r'<a.*href="(.*)">', requests.get(i).text):
#         p = 'Yes'
#         break
# print(p)

# hrefs = lambda url: re.findall(r'<a .*?\bhref="(.*?)"', requests.get(url).text)
# url1, url2 = input(), input()
# print('Yes' if any(b == url2 for a in hrefs(url1) for b in hrefs(a)) else 'No')

# Вашей программе на вход подается ссылка на HTML файл.
# Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов,
# на которые есть ссылка.
# Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность
# символов, которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть, за
# исключением случаев с относительными ссылками вида <a href="../some_path/index.html">.
# Сайты следует выводить в алфавитном порядке.

# Для того, чтобы группа не попадала в список возвращаемый findall, есть специальный синтаксис (?:выражение).
# В конце домена всегда идет один из знаков / : ' "
import requests, re
resp = requests.get(input()).text  # Адрес - http://pastebin.com/raw/7543p0ns
link_pattern = re.compile(r'<a[^>]*?href=[\"\'](?:\w*://)?(\w.*?)[/:\"\'][^>]*?>')
s = sorted(set((link_pattern.findall(resp))))
print(*s, sep='\n')
#
# page = requests.get(input())
# url_pattern = re.compile(r'<a.*?href=["|\'](.*?:\/\/)?(\w.*?)([/|:].*)?["|\'].*')
# links = sorted(set([link[1] for link in url_pattern.findall(page.text)]))
# print(*links, sep='\n_test')
#
# resp = requests.get(input()).text  # Пример правильного решения.Замечание авторов: это одна из самых сложных задач курса
# sites = set()
# for site in re.findall(r'<a.*?href=".*?:\/\/((?:\w|-)+(?:\.(?:\w|-)+)+)', resp):
#     sites.add(site)
# for site in sorted(sites):
#     print(site)

# Например, почти все споткнулись на ссылках:
# <a href="mailto:admin@gmail.com">
# <a href="/m.html" target="_blank">
# <a href="/talk/forum/post.php?f=11" class="text_orange">
# <a href="read.php?f=11&i=464012&t=464012&page=119" id="next_page">

# вот две регулярки, которые должны все обработать. По крайней мере, точно обрабатывают приведенный вами набор ссылок:
# 1. r'<a.*href=[\'\"]\w*?[:/]*([\w-]+\.(?!html)(?!php)[\w.-]+)[/:'\"]'
# 2. r'<a.*href=[\'\"](?:[\w-]+://)?([\w-]+(?:\.[\w-]+)+)+[/:\'\"]'

# Решение без регулярного выражения, но с помощью встроенных библиотек
#
# from html.parser import HTMLParser
# import requests
# import urllib.parse
#
# class MyParser(HTMLParser):
#     links = set()
#
#     def handle_starttag(self, tag, attrs):
#         if tag == 'a':
#             for tpl in attrs:
#                 _url = urllib.parse.urlparse(tpl[1])
#
#                 if _url[1] and _url[1][-1].isalpha():
#                     self.links.add(_url[1])
#
#     def print(self):
#         return self.links
#
# request = requests.get(input()).text
# parser = MyParser()
# parser.feed(request)
#
# for item in sorted(parser.print()):
#     print(item)

# Сделать запрос с помощью запросов очень просто.
# Начните с импорта модуля запросов:
# import requests
# Теперь давайте попробуем получить веб-страницу. Для этого примера возьмем общедоступную временную шкалу GitHub:
# r = requests.get('https://api.github.com/events')
# Теперь у нас есть Responseобъект с именем r. Мы можем получить всю необходимую информацию из этого объекта.
# Простой API запросов означает, что все формы HTTP-запросов столь же очевидны. Например, вот как вы делаете запрос
# HTTP POST:
# r = requests.post('https://httpbin.org/post', data={'name': 'value'})
# Красиво, правда? А как насчет других типов HTTP-запросов: PUT, DELETE, HEAD и OPTIONS? Все это так же просто:
# r = requests.put('https://httpbin.org/put', data={'name': 'value'})
# r = requests.delete('https://httpbin.org/delete')
# r = requests.head('https://httpbin.org/get')
# r = requests.options('https://httpbin.org/get')
# Это все хорошо, но это только начало того, что могут делать Requests.
# Передача параметров в URL
# Вы часто хотите отправить какие-то данные в строке запроса URL-адреса. Если бы вы создавали URL-адрес вручную, эти
# данные были бы представлены в виде пар ключ / значение в URL-адресе после вопросительного знака, например
# httpbin.org/get?name=val. Запросы позволяют вам предоставить эти аргументы в виде словаря строк, используя metric
# аргумент ключевого слова. В качестве примера, если вы хотите , чтобы пройти key1=value1 и key2=value2 к
# httpbin.org/get, можно использовать следующий код:
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get('https://httpbin.org/get', metric=payload)
# Вы можете увидеть, что URL-адрес был правильно закодирован, распечатав URL-адрес:
# print(r.url)  # https://httpbin.org/get?key2=value2&key1=value1
# Обратите внимание, что любой ключ словаря, значение которого равно None, не будет добавлен в строку запроса URL-адреса.
# Вы также можете передать список элементов в качестве значения:
# payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
# r = requests.get('https://httpbin.org/get', metric=payload)
# print(r.url)  # https://httpbin.org/get?key1=value1&key2=value2&key2=value3
# Содержание ответа
# Мы можем прочитать содержимое ответа сервера. Снова рассмотрим временную шкалу GitHub:
# import requests
# r = requests.get('https://api.github.com/events')
# r.text  # '[{"repository":{"open_issues":0,"url":"https://github.com/...
# Запросы будут автоматически декодировать контент с сервера. Большинство кодировок Unicode легко декодируются.
# Когда вы делаете запрос, Requests делает обоснованные предположения о кодировке ответа на основе заголовков HTTP.
# Кодировка текста, предполагаемая запросами, используется при доступе r.text. Вы можете узнать, какие запросы
# кодирования используются, и изменить их, используя r.encoding свойство:
# r.encoding  # 'utf-8'
# r.encoding = 'ISO-8859-1'
# Если вы измените кодировку, запросы будут использовать новое значение r.encoding всякий раз, когда вы вызываете
# r.text. Возможно, вы захотите сделать это в любой ситуации, когда вы можете применить специальную логику для
# определения того, какой будет кодировка контента. Например, HTML и XML могут указывать свою кодировку в своем теле.
# В подобных ситуациях вы должны использовать, r.contentчтобы найти кодировку, а затем установить r.encoding. Это
# позволит вам использовать r.textправильную кодировку.
# В запросах также будут использоваться пользовательские кодировки, если они вам понадобятся. Если вы создали свою
# собственную кодировку и зарегистрировали ее в codecs модуле, вы можете просто использовать имя кодека в качестве
# значения, r.encoding и запросы будут обрабатывать декодирование за вас.
# Содержимое двоичного ответа
# Вы также можете получить доступ к телу ответа в байтах для нетекстовых запросов:
# r.content  # b'[{"repository":{"open_issues":0,"url":"https://github.com/...
# В gzipи deflateпередаче-кодирования автоматически декодируются для вас.
# br Передачи кодирование автоматически декодируется для вас , если библиотека Brotli как brotli или brotlicffi
# установлена.
# Например, чтобы создать изображение из двоичных данных, возвращаемых запросом, вы можете использовать следующий код:
# from PIL import Image
# from io import BytesIO
# i = Image.open(BytesIO(r.content))
# Содержимое ответа JSON
# Также есть встроенный декодер JSON, если вы имеете дело с данными JSON:
# import requests
# r = requests.get('https://api.github.com/events')
# r.json()  # [{'repository': {'open_issues': 0, 'url': 'https://github.com/...
# В случае сбоя декодирования JSON r.json()возникает исключение. Например, если ответ получает 204 (Нет содержимого) или
# если ответ содержит недопустимый JSON, r.json()возникает попытка повышения requests.exceptions.JSONDecodeError. Это
# исключение оболочки обеспечивает взаимодействие для нескольких исключений, которые могут быть вызваны разными
# версиями Python и библиотеками сериализации json.
# Следует отметить , что успех вызова r.json()никак не указывает на успех ответа. Некоторые серверы могут возвращать
# объект JSON в неудачном ответе (например, сведения об ошибке с HTTP 500). Такой JSON будет декодирован и возвращен.
# Чтобы проверить успешность запроса, используйте r.raise_for_status()или проверьте r.status_codeто, что вы ожидаете.
# Необработанный контент ответа
# В том редком случае, когда вы хотите получить необработанный ответ сокета от сервера, вы можете получить доступ r.raw.
# Если вы хотите это сделать, убедитесь, что вы установили stream=True в своем первоначальном запросе. Как только вы это
# сделаете, вы можете сделать это:
# r = requests.get('https://api.github.com/events', stream=True)
# r.raw  # <urllib3.response.HTTPResponse object at 0x101194810>
# r.raw.read(10)  # '\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03'
# В целом, однако, вы должны использовать такой шаблон для сохранения потоковой передачи в файл:
# with open(filename, 'wb') as fd:
#     for chunk in r.iter_content(chunk_size=128):
#         fd.write(chunk)
# Использование Response.iter_contentбудет обрабатывать многое из того, с чем вам в противном случае пришлось бы
# справиться при Response.rawпрямом использовании . При потоковой передаче загрузки описанный выше способ получения
# содержимого является предпочтительным и рекомендуемым. Обратите внимание, что chunk_sizeего можно свободно изменить
# до числа, которое может лучше соответствовать вашим вариантам использования.
# Примечание
# Важное замечание об использовании Response.iter_content versus Response.raw. Response.iter_content будет автоматически
# декодировать кодировки gzipи deflate передачи. Response.raw представляет собой необработанный поток байтов - он не
# преобразует содержимое ответа. Если вам действительно нужен доступ к байтам в том виде, в каком они были возвращены,
# используйте Response.raw.
# Пользовательские заголовки
# Если вы хотите , чтобы добавить HTTP заголовков к запросу, просто передать в dictк headersпараметру.
# Например, в предыдущем примере мы не указали наш пользовательский агент:
# url = 'https://api.github.com/some/endpoint'
# headers = {'user-agent': 'my-app/0.0.1'}
# r = requests.get(url, headers=headers)
# Примечание. Пользовательские заголовки имеют меньший приоритет, чем более конкретные источники информации. Например:
# Заголовки авторизации, заданные с помощью headers =, будут отменены, если учетные данные указаны в .netrc, что, в свою
# очередь, будет отменено auth= параметром. Запросы будут искать файл netrc в ~ / .netrc , ~ / _netrc или по пути,
# указанному переменной среды NETRC .
# Заголовки авторизации будут удалены, если вы будете перенаправлены за пределы хоста.
# Заголовки Proxy-Authorization будут переопределены учетными данными прокси, указанными в URL-адресе.
# Заголовки Content-Length будут переопределены, когда мы сможем определить длину содержимого.
# Более того, Requests вообще не меняет своего поведения в зависимости от того, какие настраиваемые заголовки указаны.
# Заголовки просто передаются в окончательный запрос.
# Примечание. Все значения заголовка должны быть в string формате a , bytestring или unicode. Хотя это разрешено,
# рекомендуется избегать передачи значений заголовка Unicode.
# Более сложные запросы POST
# Как правило, вы хотите отправить некоторые закодированные в форме данные - очень похоже на HTML-форму. Для этого
# просто передайте в data аргумент словарь. Ваш словарь данных будет автоматически закодирован, когда будет сделан
# запрос:
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post("https://httpbin.org/post", data=payload)
# print(r.text)
# {
#   ...
#   "form": {
#     "key2": "value2",
#     "key1": "value1"
#   },
#   ...
# }
# data Аргумент может иметь несколько значений для каждого ключа. Это можно сделать, составив data список кортежей или
# словарь со списками в качестве значений. Это особенно полезно, когда в форме есть несколько элементов, использующих
# один и тот же ключ:
# payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
# r1 = requests.post('https://httpbin.org/post', data=payload_tuples)
# payload_dict = {'key1': ['value1', 'value2']}
# r2 = requests.post('https://httpbin.org/post', data=payload_dict)
# print(r1.text)
# {
#   ...
#   "form": {
#     "key1": [
#       "value1",
#       "value2"
#     ]
#   },
#   ...
# }
# r1.text == r2.text  # True
# Бывают случаи, когда вам может потребоваться отправить данные, не закодированные в форме. Если вы передадите a string
# вместо a dict, эти данные будут опубликованы напрямую.
# Например, GitHub API v3 принимает данные POST / PATCH в кодировке JSON:
# import json
# url = 'https://api.github.com/some/endpoint'
# payload = {'some': 'data'}
# r = requests.post(url, data=json.dumps(payload))
# Вместо того, чтобы кодировать dictсебя, вы также можете передать его напрямую, используя jsonпараметр (добавлен в
# версии 2.4.2), и он будет закодирован автоматически:
# url = 'https://api.github.com/some/endpoint'
# payload = {'some': 'data'}
# r = requests.post(url, json=payload)
# Обратите внимание: json параметр игнорируется, если передан либо data или files.
# Использование json параметра в запросе изменит значение Content-Type в заголовке на application/json.
# POST файл с  кодированием
# Запросы упрощают загрузку файлов с кодировкой Multipart:
# url = 'https://httpbin.org/post'
# files = {'file': open('report.xls', 'rb')}
#
# r = requests.post(url, files=files)
# r.text
# {
#   ...
#   "files": {
#     "file": "<censored...binary...data>"
#   },
#   ...
# }
# Вы можете явно указать имя файла, content_type и заголовки:
# url = 'https://httpbin.org/post'
# files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
#
# r = requests.post(url, files=files)
# r.text
# {
#   ...
#   "files": {
#     "file": "<censored...binary...data>"
#   },
#   ...
# }
# При желании вы можете отправлять строки для получения в виде файлов:
# rl = 'https://httpbin.org/post'
# files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
#
# r = requests.post(url, files=files)
# r.text
# {
#   ...
#   "files": {
#     "file": "some,data,to,send\\nanother,row,to,send\\n"
#   },
#   ...
# }
# Если вы отправляете в качестве multipart/form-data запроса очень большой файл , вы можете передать запрос в потоковом
# режиме. По умолчанию requestsне поддерживает это, но есть отдельный пакет, который поддерживает - requests-toolbelt.
# Вы должны прочитать документацию к toolbelt, чтобы узнать больше о том, как его использовать.
# Чтобы отправить несколько файлов в одном запросе, обратитесь к расширенному разделу.
# Предупреждение
# Настоятельно рекомендуется открывать файлы в двоичном режиме . Это связано с тем, что запросы могут пытаться
# предоставить вам Content-Length заголовок, и если это произойдет, это значение будет установлено равным количеству
# байтов в файле. Ошибки могут возникнуть, если вы откроете файл в текстовом режиме .
# Коды состояния ответа
# Мы можем проверить код статуса ответа:
# r = requests.get('https://httpbin.org/get')
# r.status_code  # 200
# Запросы также имеют встроенный объект поиска кода состояния для удобства использования:
# r.status_code == requests.codes.ok  # True
# Если мы сделали неверный запрос (ошибка клиента 4XX или ответ с ошибкой сервера 5XX), мы можем поднять его с помощью
# Response.raise_for_status():
# bad_r = requests.get('https://httpbin.org/status/404')
# bad_r.status_code  # 404
# bad_r.raise_for_status()
# Traceback (most recent call last):
#   File "requests/models.py", line 832, in raise_for_status
#     raise http_error
# requests.exceptions.HTTPError: 404 Client Error
# Но, поскольку наш status_codefor rбыл 200, когда мы вызываем, raise_for_status()мы получаем:
# r.raise_for_status()  # None
# Все хорошо.
# Заголовки ответов
# Мы можем просмотреть заголовки ответов сервера, используя словарь Python:
# r.headers
# {
#     'content-encoding': 'gzip',
#     'transfer-encoding': 'chunked',
#     'connection': 'close',
#     'server': 'nginx/1.0.4',
#     'x-runtime': '148ms',
#     'etag': '"e1ca502697e5c9317743dc078f67693f"',
#     'content-type': 'application/json'
# }
# Однако словарь особенный: он предназначен только для заголовков HTTP. Согласно RFC 7230 , имена заголовков HTTP
# нечувствительны к регистру.
# Итак, мы можем получить доступ к заголовкам, используя любые заглавные буквы:
# r.headers['Content-Type']  # 'application/json'
# r.headers.get('content-type')  # 'application/json'
# Это также особенность в том, что сервер мог отправлять один и тот же заголовок несколько раз с разными значениями, но
# запросы объединяют их, чтобы они могли быть представлены в словаре в рамках одного сопоставления, согласно RFC 7230 :
# Получатель МОЖЕТ объединить несколько полей заголовка с одним и тем же именем поля в одну пару «имя-поля:
# значение-поля» без изменения семантики сообщения, добавляя каждое последующее значение поля к объединенному значению
# поля по порядку, разделенное знаком запятая.
# Файлы cookie
# Если ответ содержит файлы cookie, вы можете быстро получить к ним доступ:
# url = 'http://example.com/some/cookie/setting/url'
# r = requests.get(url)
# r.cookies['example_cookie_name']  # 'example_cookie_value'
# Чтобы отправить свои файлы cookie на сервер, вы можете использовать cookies параметр:
# url = 'https://httpbin.org/cookies'
# cookies = dict(cookies_are='working')
# r = requests.get(url, cookies=cookies)
# r.text  # '{"cookies": {"cookies_are": "working"}}'
# Файлы cookie возвращаются в виде RequestsCookieJar, который действует как, dictно также предлагает более полный
# интерфейс, подходящий для использования в нескольких доменах или путях. Файлы cookie также могут передаваться в
# запросы:
# jar = requests.cookies.RequestsCookieJar()
# jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
# jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
# url = 'https://httpbin.org/cookies'
# r = requests.get(url, cookies=jar)
# r.text  # '{"cookies": {"tasty_cookie": "yum"}}'
# Перенаправление и история
# По умолчанию запросы будут выполнять перенаправление местоположения для всех глаголов, кроме HEAD.
# Мы можем использовать historyсвойство объекта Response для отслеживания перенаправления.
# Response.historyСписок содержит Responseобъекты , которые были созданы для того , чтобы завершить запрос. Список
# отсортирован от самого старого до самого последнего ответа.
# Например, GitHub перенаправляет все HTTP-запросы на HTTPS:
# r = requests.get('http://github.com/')
# r.url  # 'https://github.com/'
# r.status_code  # 200
# r.history  # [<Response [301]>]
# Если вы используете GET, OPTIONS, POST, PUT, PATCH или DELETE, вы можете отключить обработку перенаправления с помощью
# allow_redirects параметра:
# r = requests.get('http://github.com/', allow_redirects=False)
# r.status_code  # 301
# r.history  # []
# Если вы используете HEAD, вы также можете включить перенаправление:
# r = requests.head('http://github.com/', allow_redirects=True)
# r.url  # 'https://github.com/'
# r.history  # [<Response [301]>]
# Таймауты
# Вы можете указать запросам прекратить ожидание ответа через заданное количество секунд с помощью timeoutпараметра.
# Практически весь производственный код должен использовать этот параметр почти во всех запросах. В противном случае
# ваша программа может зависнуть на неопределенное время:
# requests.get('https://github.com/', timeout=0.001)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# requests.exceptions.Timeout: HTTPConnectionPool(host='github.com', port=80): Request timed my_input. (timeout=0.001)
# Примечание
# timeout не является ограничением по времени на загрузку всего ответа; скорее, возникает исключение, если сервер не
# отправил ответ в течение timeout нескольких секунд (точнее, если на базовый сокет в течение timeout секунд не было
# получено ни одного байта ). Если тайм-аут не указан явно, запросы не истекают.
# Ошибки и исключения
# В случае сетевой проблемы (например, сбой DNS, отказ в соединении и т. Д.) Запросы вызовут ConnectionError исключение.
# Response.raise_for_status()поднимет, HTTPError если HTTP-запрос вернул неудачный код состояния.
# Если запрос истекает, возникает Timeout исключение.
# Если запрос превышает настроенное максимальное количество перенаправлений, возникает TooManyRedirects исключение.
# Все исключения, которые явно вызывает Requests, наследуются от requests.exceptions.RequestException.

# Расширенное использование
# В этом документе описаны некоторые более сложные функции запросов.
# Объекты сеанса
# Объект Session позволяет сохранять определенные параметры в запросах. Он также сохраняется печеньем во всех запросах,
# сделанных из экземпляра сессии, и будет использовать urllib3«s пулы соединений . Поэтому, если вы делаете несколько
# запросов к одному и тому же хосту, базовое TCP-соединение будет повторно использовано, что может привести к
# значительному увеличению производительности (см. Постоянное соединение HTTP ).
# Объект Session имеет все методы основного API запросов.
# Давайте сохраним некоторые файлы cookie между запросами:
# s = requests.Session()
# s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
# r = s.get('https://httpbin.org/cookies')
# print(r.text)  # '{"cookies": {"sessioncookie": "123456789"}}'
# Сеансы также могут использоваться для предоставления данных по умолчанию методам запроса. Это делается путем
# предоставления данных свойствам объекта Session:
# s = requests.Session()
# s.auth = ('user', 'pass')
# s.headers.update({'x-test': 'true'})
# # both 'x-test' and 'x-test2' are sent
# s.get('https://httpbin.org/headers', headers={'x-test2': 'true'})
# Любые словари, которые вы передаете методу запроса, будут объединены с заданными значениями уровня сеанса. Параметры
# уровня метода переопределяют параметры сеанса.
# Однако обратите внимание, что параметры уровня метода не будут сохраняться в запросах, даже если используется сеанс.
# В этом примере файлы cookie будут отправляться только с первым запросом, но не со вторым:
# s = requests.Session()
# r = s.get('https://httpbin.org/cookies', cookies={'from-my': 'browser'})
# print(r.text)  # '{"cookies": {"from-my": "browser"}}'
# r = s.get('https://httpbin.org/cookies')
# print(r.text)  # '{"cookies": {}}'
# Если вы хотите вручную добавить файлы cookie в сеанс, используйте служебные функции Cookie для управления
# Session.cookies.
# Сеансы также могут использоваться как менеджеры контекста:
# with requests.Session() as s:
#     s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
# Это обеспечит закрытие сеанса сразу после with выхода из блока, даже если возникли необработанные исключения.
# Удаление значения из параметра Dict
# Иногда вам нужно опустить ключи уровня сеанса из параметра dict. Для этого вы просто устанавливаете значение этого
# ключа в параметр None уровня метода. Он будет автоматически пропущен.
# Все значения, содержащиеся в сеансе, доступны вам напрямую. См. Документацию по API сеанса, чтобы узнать больше.
# Объекты запроса и ответа
# Когда звонят requests.get()друзьям и друзьям, вы делаете две важные вещи. Сначала вы создаете Requestобъект, который
# будет отправлен на сервер для запроса или запроса какого-либо ресурса. Во-вторых, Response объект создается после
# того, как Requests получает ответ от сервера. ResponseОбъект содержит все данные , возвращаемые сервером , а также
# содержит Request объект, созданный первоначально. Вот простой запрос на получение очень важной информации с серверов
# Википедии:
# r = requests.get('https://en.wikipedia.org/wiki/Monty_Python')
# Если мы хотим получить доступ к заголовкам, которые сервер отправил нам, мы делаем следующее:
# r.headers
# {'content-length': '56170', 'x-content-type-options': 'nosniff', 'x-cache':
# 'HIT from cp1006.eqiad.wmnet, MISS from cp1010.eqiad.wmnet', 'content-encoding':
# 'gzip', 'age': '3080', 'content-language': 'en', 'vary': 'Accept-Encoding,Cookie',
# 'server': 'Apache', 'last-modified': 'Wed, 13 Jun 2012 01:33:50 GMT',
# 'connection': 'close', 'cache-control': 'private, s-maxage=0, max-age=0,
# must-revalidate', 'date': 'Thu, 14 Jun 2012 12:59:39 GMT', 'content-type':
# 'text/html; charset=UTF-8', 'x-cache-lookup': 'HIT from cp1006.eqiad.wmnet:3128,
# MISS from cp1010.eqiad.wmnet:80'}
# Однако, если мы хотим получить заголовки, которые мы отправили серверу, мы просто обращаемся к запросу, а затем к
# заголовкам запроса:
# r.request.headers
# {'Accept-Encoding': 'identity, deflate, compress, gzip',
# 'Accept': '*/*', 'User-Agent': 'python-requests/1.2.0'}
# Подготовленные запросы
# Каждый раз, когда вы получаете Responseобъект из вызова API или вызова сеанса, requestфактически PreparedRequest
# используется атрибут . В некоторых случаях вы можете захотеть проделать дополнительную работу с телом или заголовками
# (или чем-то еще) перед отправкой запроса. Простой рецепт для этого следующий:
# from requests import Request, Session
# s = Session()
# req = Request('POST', url, data=data, headers=headers)
# prepped = req.prepare()
# # do something with prepped.body
# prepped.body = 'No, I want exactly this as the body.'
# # do something with prepped.headers
# del prepped.headers['Content-Type']
# resp = s.send(prepped,
#     stream=stream,
#     verify=verify,
#     proxies=proxies,
#     cert=cert,
#     timeout=timeout
# )
# print(resp.status_code)
# Поскольку вы не делаете ничего особенного с Requestобъектом, вы немедленно его готовите и модифицируете
# PreparedRequest. Затем вы отправляете это с другими параметрами, которые вы отправили бы requests.*или Session.*.
# Однако приведенный выше код теряет некоторые преимущества наличия Sessionобъекта Requests . В частности, Sessionк
# вашему запросу не применяется состояние -уровня, такое как файлы cookie. Чтобы получить PreparedRequestс этим
# состоянием, замените вызов на Request.prepare() вызов Session.prepare_request(), например:
# from requests import Request, Session
# s = Session()
# req = Request('GET',  url, data=data, headers=headers)
# prepped = s.prepare_request(req)
# # do something with prepped.body
# prepped.body = 'Seriously, send exactly these bytes.'
# # do something with prepped.headers
# prepped.headers['Keep-Dead'] = 'parrot'
# resp = s.send(prepped,
#     stream=stream,
#     verify=verify,
#     proxies=proxies,
#     cert=cert,
#     timeout=timeout
# )
# print(resp.status_code)
# Когда вы используете подготовленный поток запросов, имейте в виду, что он не принимает во внимание среду. Это может
# вызвать проблемы, если вы используете переменные среды для изменения поведения запросов. Например: Самозаверяющие
# SSL-сертификаты, указанные в REQUESTS_CA_BUNDLE, не будут учитываться. В результате бросается. Вы можете обойти это
# поведение, явно объединив настройки среды в свой сеанс:SSL: CERTIFICATE_VERIFY_FAILED
# from requests import Request, Session
# s = Session()
# req = Request('GET', url)
# prepped = s.prepare_request(req)
# # Merge environment settings into session
# settings = s.merge_environment_settings(prepped.url, {}, None, None, None)
# resp = s.send(prepped, **settings)
# print(resp.status_code)
# Подтверждение сертификата SSL
# Запросы проверяют сертификаты SSL для запросов HTTPS, как и веб-браузер. По умолчанию проверка SSL включена, и запросы
# будут вызывать ошибку SSLError, если не удается проверить сертификат:
# requests.get('https://requestb.in')
# requests.exceptions.SSLError: hostname 'requestb.in' doesn't match either of '*.herokuapp.com', 'herokuapp.com'
# У меня нет настройки SSL в этом домене, поэтому возникает исключение. Отлично. Однако GitHub:
# requests.get('https://github.com')
# <Response [200]>
# Вы можете передать verifyпуть к файлу или каталогу CA_BUNDLE с сертификатами доверенных центров сертификации:
# requests.get('https://github.com', verify='/path/to/certfile')
# или стойкий:
# s = requests.Session()
# s.verify = '/path/to/certfile'
# Примечание
# Если verifyустановлен путь к каталогу, каталог должен быть обработан с помощью c_rehashутилиты, поставляемой с OpenSSL
# Этот список доверенных центров сертификации также можно указать с помощью REQUESTS_CA_BUNDLEпеременной среды. Если
# REQUESTS_CA_BUNDLEне установлен, CURL_CA_BUNDLEбудет использоваться как резерв.
# Запросы также могут игнорировать проверку сертификата SSL, если вы установите verifyзначение False:
# requests.get('https://kennethreitz.org', verify=False)
# <Response [200]>
# Обратите внимание, что когда verifyустановлено значение False, запросы будут принимать любой сертификат TLS,
# представленный сервером, и будут игнорировать несоответствия имени хоста и / или сертификаты с истекшим
# действия, что сделает ваше приложение уязвимым для атак типа «человек посередине» (MitM). Параметр verify to False
# может быть полезен при локальной разработке или тестировании.
# По умолчанию verifyустановлено значение True. Опция verifyприменима только к хост-сертификатам.
# Сертификаты на стороне клиента
# Вы также можете указать локальный сертификат для использования в качестве сертификата на стороне клиента, как
# отдельный файл (содержащий закрытый ключ и сертификат) или как кортеж путей к обоим файлам:
# requests.get('https://kennethreitz.org', cert=('/path/client.cert', '/path/client.name'))
# <Response [200]>
# или стойкий:
# s = requests.Session()
# s.cert = '/path/client.cert'
# Если вы укажете неверный путь или недействительный сертификат, вы получите ошибку SSLError:
# requests.get('https://kennethreitz.org', cert='/wrong_path/client.pem')
# SSLError: [Errno 336265225] _ssl.c:347: error:140B0009:SSL routines:SSL_CTX_use_PrivateKey_file:PEM lib
# Предупреждение
# Закрытый ключ к вашему локальному сертификату должен быть незашифрованным. В настоящее время Requests не поддерживает
# использование зашифрованных ключей.
# Сертификаты CA
# Запросы используют сертификаты из пакета certifi . Это позволяет пользователям обновлять свои доверенные сертификаты без изменения версии запросов.
# До версии 2.16 Requests объединял набор доверенных корневых центров сертификации, полученных из хранилища доверенных сертификатов Mozilla . Сертификаты обновлялись только один раз для каждой версии запросов. Когда certifiон не был установлен, это приводило к чрезвычайно устаревшим пакетам сертификатов при использовании значительно более старых версий запросов.
# В целях безопасности мы рекомендуем часто обновлять сертификаты!
# Рабочий процесс содержимого тела
# По умолчанию, когда вы делаете запрос, сразу же загружается тело ответа. Вы можете переопределить это поведение и отложить загрузку тела ответа до тех пор, пока не получите доступ к Response.content атрибуту с streamпараметром:
# tarball_url = 'https://github.com/psf/requests/tarball/main'
# r = requests.get(tarball_url, stream=True)
# На данный момент загружены только заголовки ответов, а соединение остается открытым, что позволяет нам сделать получение контента условным:
# if int(r.headers['content-length']) < TOO_LONG:
#   content = r.content
#   ...
# Вы можете дополнительно контролировать рабочий процесс путем использования Response.iter_content() и Response.iter_lines()методы. Кроме того, вы можете прочитать недекодированное тело из базового urllib3 по urllib3.HTTPResponseадресу Response.raw.
# Если установить streamв Trueпри создании запроса, запросы не могут освободить соединение обратно в пул , если вы не потребляете все данные , или позвоните по телефону Response.close. Это может привести к неэффективности подключений. Если вы обнаружите, что частично читаете тела запросов (или не читаете их вообще) во время использования stream=True, вы должны сделать запрос внутри withоператора, чтобы гарантировать, что он всегда закрыт:
# with requests.get('https://httpbin.org/get', stream=True) as r:
#     # Do things with the response here.
# Keep-Alive
# Отличные новости - благодаря urllib3, keep-alive 100% автоматический в течение сеанса! Любые запросы, которые вы
# делаете во время сеанса, будут автоматически повторно использовать соответствующее соединение!
# Обратите внимание, что соединения возвращаются в пул для повторного использования только после того, как все данные
# тела прочитаны; обязательно либо набор streamдля Falseили прочитать contentсвойство Responseобъекта.
# Потоковая загрузка загрузок
# Запросы поддерживают потоковую загрузку, что позволяет отправлять большие потоки или файлы, не считывая их в память.
# Для потоковой передачи и загрузки просто предоставьте объект в виде файла для своего тела:
# with open('massive-body', 'rb') as f:
#     requests.post('http://some.url/streamed', data=f)
# Предупреждение
# Настоятельно рекомендуется открывать файлы в двоичном режиме . Это связано с тем, что запросы могут пытаться
# предоставить вам Content-Lengthзаголовок, и если это произойдет, это значение будет установлено равным количеству
# байтов в файле. Ошибки могут возникнуть, если вы откроете файл в текстовом режиме .
# Запросы с  фрагментов
# Requests также поддерживает кодировку Chunked Transfer для исходящих и входящих запросов. Чтобы отправить запрос с
# кодировкой фрагментов, просто предоставьте генератор (или любой итератор без длины) для вашего тела:
# def gen():
#     yield 'hi'
#     yield 'there'
#
# requests.post('http://some.url/chunked', data=gen())
# Для фрагментированных ответов лучше всего перебирать данные, используя Response.iter_content(). В идеальной ситуации
# вы должны установить stream=True запрос, и в этом случае вы можете выполнять итерацию по частям, вызывая iter_content
# с chunk_size параметром None. Если вы хотите установить максимальный размер блока, вы можете установить для
# chunk_size параметра любое целое число.
# POST несколько файлов с многократным кодированием
# Вы можете отправить несколько файлов в одном запросе. Например, предположим, что вы хотите загрузить файлы изображений
# в HTML-форму с несколькими полями файлов 'images':
# <input type="file" name="images" multiple="true" required="true"/>
# Для этого просто установите для файлов список кортежей :(form_field_name, file_info)
# url = 'https://httpbin.org/post'
# multiple_files = [
#     ('images', ('foo.png', open('foo.png', 'rb'), 'image/png')),
#     ('images', ('bar.png', open('bar.png', 'rb'), 'image/png'))]
# r = requests.post(url, files=multiple_files)
# r.text
# {
#   ...
#   'files': {'images': 'data:image/png;base64,iVBORw ....'}
#   'Content-Type': 'multipart/form-data; boundary=3131623adb2043caaeb5538cc7aa0b3a',
#   ...
# }
# Предупреждение
# Настоятельно рекомендуется открывать файлы в двоичном режиме . Это связано с тем, что запросы могут пытаться
# предоставить вам Content-Lengthзаголовок, и если это произойдет, это значение будет установлено равным
# байтов в файле. Ошибки могут возникнуть, если вы откроете файл в текстовом режиме .
# Крючки для событий
# В Requests есть система ловушек, которую вы можете использовать для управления частями процесса запроса или обработки
# событий сигнала.
# Доступные крючки:
# response:
# Ответ, созданный на запрос.
# Вы можете назначить функцию перехвата для каждого запроса, передав словарь параметру запроса:
# {hook_name: callback_function}hooks
# hooks={'response': print_url}
# В callback_functionкачестве первого аргумента он получит фрагмент данных.
# def print_url(r, *args, **kwargs):
#     print(r.url)
# Ваша функция обратного вызова должна обрабатывать собственные исключения. Любое необработанное исключение не будет передаваться без уведомления и, следовательно, должно обрабатываться кодом, вызывающим запросы.
# Если функция обратного вызова возвращает значение, предполагается, что она заменяет переданные данные. Если функция ничего не возвращает, это не влияет ни на что другое.
# def record_hook(r, *args, **kwargs):
#     r.hook_called = True
#     return r
# Напечатаем некоторые аргументы метода запроса во время выполнения:
# requests.get('https://httpbin.org/', hooks={'response': print_url})
# https://httpbin.org/
# <Response [200]>
# Вы можете добавить несколько хуков к одному запросу. Назовем сразу два крючка:
# r = requests.get('https://httpbin.org/', hooks={'response': [print_url, record_hook]})
# r.hook_called
# True
# Вы также можете добавить хуки к Sessionэкземпляру. Любые добавленные хуки будут вызываться при каждом запросе к
# сеансу. Например:
# s = requests.Session()
# s.hooks['response'].append(print_url)
# s.get('https://httpbin.org/')
#  https://httpbin.org/
#  <Response [200]>
# У A Sessionможет быть несколько хуков, которые будут вызываться в порядке добавления.
# Пользовательская аутентификация
# Запросы позволяют указать собственный механизм аутентификации.
# Любой вызываемый объект, который передается в качестве authаргумента методу запроса, будет иметь возможность изменить
# запрос до его отправки.
# Реализации аутентификации являются подклассами AuthBase, и их легко определить. Запросы предоставляют две
# распространенные реализации схемы аутентификации в requests.auth: HTTPBasicAuthи HTTPDigestAuth.
# Представим, что у нас есть веб-сервис, который будет отвечать только в том случае, если в X-Pizzaзаголовке установлено
# значение пароля. Маловероятно, но просто смирись.
# from requests.auth import AuthBase
# class PizzaAuth(AuthBase):
#     """Attaches HTTP Pizza Authentication to the given Request object."""
#     def __init__(self, username):
#         # setup any auth-related data here
#         self.username = username
#
#     def __call__(self, r):
#         # modify and return the request
#         r.headers['X-Pizza'] = self.username
#         return r
# Затем мы можем сделать запрос, используя нашу Pizza Auth:
# requests.get('http://pizzabin.org/admin', auth=PizzaAuth('kenneth'))
# <Response [200]>
# Потоковые запросы
# С Response.iter_lines()его помощью вы можете легко перебирать потоковые API, такие как Twitter Streaming API . Просто
# установите streamна Trueи итерацию по реакции с iter_lines:
# import json
# import requests
# r = requests.get('https://httpbin.org/stream/20', stream=True)
# for line in r.iter_lines():
#     # filter my_input keep-alive new lines
#     if line:
#         decoded_line = line.decode('utf-8')
#         print(json.loads(decoded_line))
# При использовании decode_unicode = True с Response.iter_lines()или Response.iter_content()вы захотите предоставить
# резервную кодировку на случай, если сервер ее не предоставляет:
# r = requests.get('https://httpbin.org/stream/20', stream=True)
# if r.encoding is None:
#     r.encoding = 'utf-8'
# for line in r.iter_lines(decode_unicode=True):
#     if line:
#         print(json.loads(line))
# Предупреждение
# iter_linesне является безопасным для повторного входа. Многократный вызов этого метода приводит к потере некоторых
# полученных данных. Если вам нужно вызвать его из нескольких мест, используйте вместо этого полученный объект итератора
# lines = r.iter_lines()
# # Save the first line for later or just skip it
# first_line = next(lines)
# for line in lines:
#     print(line)
# Прокси
# Если вам нужно использовать прокси, вы можете настроить отдельные запросы с proxiesаргументом для любого метода
# запроса:
# import requests
# proxies = {
#   'http': 'http://10.10.1.10:3128',
#   'https': 'http://10.10.1.10:1080',
# }
# requests.get('http://example.org', proxies=proxies)
# В качестве альтернативы вы можете настроить его один раз для всего Session:
# import requests
# proxies = {
#   'http': 'http://10.10.1.10:3128',
#   'https': 'http://10.10.1.10:1080',
# }
# session = requests.Session()
# session.proxies.update(proxies)
# session.get('http://example.org')
# Когда конфигурация прокси не переопределена в питоне , как показано выше, запросы по умолчанию полагается на прокси -
# конфигурации , определенной с помощью стандартного переменного окружения http_proxy, https_proxy, no_proxy и
# curl_ca_bundle. Также поддерживаются варианты этих переменных в верхнем регистре. Поэтому вы можете настроить их для
# настройки запросов (установите только те, которые соответствуют вашим потребностям):
# $ export HTTP_PROXY="http://10.10.1.10:3128"
# $ export HTTPS_PROXY="http://10.10.1.10:1080"
# $ python
# >>> import requests
# >>> requests.get('http://example.org')
# Чтобы использовать базовую аутентификацию HTTP с вашим прокси, используйте синтаксис http: // user: password @ host /
# в любой из приведенных выше записей конфигурации:
# $ export HTTPS_PROXY="http://user:pass@10.10.1.10:1080"
# $ python
# >>> proxies = {'http': 'http://user:pass@10.10.1.10:3128/'}
# Предупреждение
# Хранение конфиденциальной информации об имени пользователя и пароле в переменной среды или файле с контролем версий
# представляет собой угрозу безопасности и настоятельно не рекомендуется.
# Чтобы предоставить прокси для конкретной схемы и хоста, используйте форму scheme: // hostname для ключа. Это будет
# соответствовать любому запросу для данной схемы и точного имени хоста.
# proxies = {'http://10.20.1.128': 'http://10.10.1.10:5323'}
# Обратите внимание, что URL-адреса прокси должны включать схему.
# Наконец, обратите внимание, что использование прокси для https-соединений обычно требует, чтобы ваш локальный
# компьютер доверял корневому сертификату прокси. По умолчанию список сертификатов, которым доверяют запросы, можно
# найти с помощью:
# from requests.utils import DEFAULT_CA_BUNDLE_PATH
# print(DEFAULT_CA_BUNDLE_PATH)
# Вы переопределяете этот набор сертификатов по умолчанию, задав для стандартной curl_ca_bundleпеременной среды другой
# путь к файлу:
# $ export curl_ca_bundle="/usr/local/myproxy_info/cacert.pem"
# $ export https_proxy="http://10.10.1.10:1080"
# $ python
# >>> import requests
# >>> requests.get('https://example.org')
# НОСКИ
# Новое в версии 2.10.0.
# Помимо основных HTTP-прокси, Requests также поддерживает прокси, использующие протокол SOCKS. Это дополнительная
# функция, для которой перед использованием необходимо установить дополнительные сторонние библиотеки.
# Вы можете получить зависимости для этой функции из pip:
# $ python -m pip install requests[socks]
# После того, как вы установили эти зависимости, использовать прокси-сервер SOCKS так же просто, как использовать
# прокси-сервер HTTP:
# proxies = {
#     'http': 'socks5://user:pass@host:port',
#     'https': 'socks5://user:pass@host:port'
# }
# Использование схемы socks5приводит к тому, что разрешение DNS происходит на клиенте, а не на прокси-сервере. Это
# соответствует curl, который использует схему, чтобы решить, выполнять ли разрешение DNS на клиенте или прокси. Если
# вы хотите разрешить домены на прокси-сервере, используйте socks5hв качестве схемы.
# Соответствие
# Запросы предназначены для соответствия всем соответствующим спецификациям и RFC, если это соответствие не вызовет
# затруднений для пользователей. Такое внимание к спецификации может привести к некоторому поведению, которое может
# показаться необычным для тех, кто не знаком с соответствующей спецификацией.
# Кодировки
# Когда вы получаете ответ, Requests делает предположение о кодировке, которую нужно использовать для декодирования
# ответа при доступе к Response.text атрибуту. Запросы сначала проверяют кодировку в заголовке HTTP, и, если его нет,
# будут использовать charset_normalizer или chardet, чтобы попытаться угадать кодировку.
# Если chardet установлен, requests использует его, однако для python3 chardet больше не является обязательной
# зависимостью chardet Библиотека является LGPL лицензии зависимости , и некоторые пользователи запросов не могут
# зависеть от обязательных зависимостей LGPL лицензии.
# Если вы устанавливаете request без указания [use_chardet_on_py3]]дополнительных параметров и chardet еще не
# установлено, requests используется charset-normalizer (с лицензией MIT) для определения кодировки. Для Python 2
# requests используется только chardet и является обязательной зависимостью.
# Единственный раз , когда запросы не догадаются кодировка , если нет явной кодировки присутствует в HTTP заголовках и
# Content-Type заголовок содержит text. В этой ситуации RFC 2616 указывает, что кодировка по умолчанию должна быть
# ISO-8859-1. В этом случае запросы следует спецификации. Если вам требуется другая кодировка, вы можете вручную
# установить Response.encoding свойство или использовать необработанный Response.content.
# HTTP-глаголы
# Запросы обеспечивают доступ почти ко всему спектру HTTP-глаголов: GET, OPTIONS, HEAD, POST, PUT, PATCH и DELETE.
# приведены подробные примеры использования этих различных команд в запросах с использованием GitHub API.
# Мы начнем с наиболее часто используемого глагола: GET. HTTP GET - это идемпотентный метод, который возвращает ресурс
# по заданному URL-адресу. В результате это глагол, который вы должны использовать при попытке получить данные из
# веб-сайта. Пример использования - попытка получить информацию о конкретном коммите из GitHub. Предположим, мы хотим
# зафиксировать a050faf запросы. У нас получилось бы так:
# import requests
# r = requests.get('https://api.github.com/repos/psf/requests/git/commits/a050faf084662f3a352dd1a941f2c7c9f886d4ad')
# Мы должны подтвердить, что GitHub ответил правильно. Если да, мы хотим выяснить, что это за контент. Сделайте это так:
# if r.status_code == requests.codes.ok:
#     print(r.headers['content-type'])
# application/json; charset=utf-8
# Итак, GitHub возвращает JSON. Отлично, мы можем использовать этот r.jsonметод для разбора его на объекты Python.
# commit_data = r.json()
# print(commit_data.keys())
# ['committer', 'author', 'url', 'tree', 'sha', 'parents', 'message']
# print(commit_data['committer'])
# {'date': '2012-05-10T11:10:50-07:00', 'email': 'me@kennethreitz.com', 'name': 'Kenneth Reitz'}
# print(commit_data['message'])
# makin' history
# Пока все просто. Что ж, давайте немного разберемся с GitHub API. Теперь мы могли бы взглянуть на документацию, но,
# возможно, мы получим немного больше удовольствия, если вместо этого будем использовать запросы. Мы можем
# воспользоваться командой Requests OPTIONS, чтобы узнать, какие типы HTTP-методов поддерживаются на только что используемом URL-адресе.
# verbs = requests.options(r.url)
# verbs.status_code
# 500
# Что? Это бесполезно! Оказывается, GitHub, как и многие поставщики API, на самом деле не реализует метод OPTIONS. Это
# досадная оплошность, но ничего страшного, мы можем просто воспользоваться скучной документацией. Однако, если GitHub
# правильно реализовал ОПЦИИ, они должны возвращать разрешенные методы в заголовках, например
# verbs = requests.options('http://a-good-website.com/api/cats')
# print(verbs.headers['allow'])
# GET,HEAD,POST,OPTIONS
# Обращаясь к документации, мы видим, что единственный другой разрешенный метод для коммитов - это POST, который создает
# новый коммит. Поскольку мы используем репозиторий Requests, нам, вероятно, следует избегать неуклюжих POSTS. Вместо
# этого давайте поиграем с функцией Issues на GitHub.
# Эта документация была добавлена в ответ на ошибку № 482 . Учитывая, что эта проблема уже существует, мы будем
# использовать ее в качестве примера. Начнем с его получения.
# r = requests.get('https://api.github.com/repos/psf/requests/issues/482')
# r.status_code
# 200
# issue = json.loads(r.text)
# print(issue['title'])
# Feature any http verb in docs
# print(issue['comments'])
# 3
# Круто, у нас есть три комментария. Давайте посмотрим на последний из них.
# r = requests.get(r.url + '/comments')
# r.status_code
# 200
# comments = r.json()
# print(comments[0].keys())
# ['body', 'url', 'created_at', 'updated_at', 'user', 'id']
# print(comments[2]['body'])
# Probably in the "advanced" section
# Что ж, это кажется глупым местом. Напишем комментарий, в котором говорится, что он глупый. А кто вообще такой плакат?
# print(comments[2]['user']['login'])
# kennethreitz
# Хорошо, давайте скажем этому парню Кеннету, что, по нашему мнению, этот пример должен быть включен в руководство по
# быстрому запуску. Согласно документу API GitHub, это можно сделать с помощью POST в потоке. Давай сделаем это.
# body = json.dumps({u"body": u"Sounds great! I'll get right on it!"})
# url = u"https://api.github.com/repos/psf/requests/issues/482/comments"
# r = requests.post(url=url, data=body)
# r.status_code
# 404
# Ха, это странно. Вероятно, нам нужно пройти аутентификацию. Это будет больно, правда? Неправильный. Запросы упрощают
# использование многих форм аутентификации, включая очень распространенную базовую аутентификацию.
# from requests.auth import HTTPBasicAuth
# auth = HTTPBasicAuth('fake@example.com', 'not_a_real_password')
# r = requests.post(url=url, data=body, auth=auth)
# r.status_code
# 201
# content = r.json()
# print(content['body'])
# Sounds great! I'll get right on it.
# Блестяще. Ой, подожди, нет! Я хотел добавить, что это займет у меня некоторое время, потому что мне нужно пойти
# покормить свою кошку. Если бы я только мог отредактировать этот комментарий! К счастью, GitHub позволяет нам
# использовать другой HTTP-глагол, PATCH, для редактирования этого комментария. Давайте сделаем это.
# print(content[u"id"])
# 5804413
# body = json.dumps({u"body": u"Sounds great! I'll get right on it once I feed my cat."})
# url = u"https://api.github.com/repos/psf/requests/issues/comments/5804413"
# r = requests.patch(url=url, data=body, auth=auth)
# r.status_code
# 200
# Отлично. Теперь, просто чтобы помучить этого парня Кеннета, я решил дать ему попотеть и не говорить ему, что я
# работаю над этим. Это означает, что я хочу удалить этот комментарий. GitHub позволяет нам удалять комментарии,
# используя метод DELETE с невероятно удачным названием. Давай избавимся от этого.
# r = requests.delete(url=url, auth=auth)
# r.status_code
# 204
# r.headers['status']
# '204 No Content'
# Отлично. Все ушли. Последнее, что я хочу знать, это то, какую часть моего предела частоты я использовал. Давайте
# разберемся. GitHub отправляет эту информацию в заголовках, поэтому вместо загрузки всей страницы я отправлю запрос
# HEAD для получения заголовков.
# r = requests.head(url=url, auth=auth)
# print(r.headers)
# 'x-ratelimit-remaining': '4995'
# 'x-ratelimit-limit': '5000'
# Отлично. Пора написать программу на Python, которая злоупотребляет API GitHub всеми интересными способами, еще 4995 раз.
# Пользовательские глаголы
# Время от времени вы можете работать с сервером, который по какой-либо причине позволяет или даже требует использования
# HTTP-глаголов, не описанных выше. Одним из примеров этого может быть метод MKCOL, который используют некоторые серверы
# WEBDAV. Не волнуйтесь, их все еще можно использовать с запросами. Они используют встроенный .request метод. Например:
# r = requests.request('MKCOL', url, data=data)
# r.status_code
# 200 # Assuming your call was correct
# Используя это, вы можете использовать любую команду метода, которую позволяет ваш сервер.
# Заголовки ссылок
# Многие HTTP API содержат заголовки ссылок. Они делают API-интерфейсы более самоописываемыми и легко обнаруживаемыми.
# GitHub использует их для разбивки на страницы в своем API, например:
# url = 'https://api.github.com/users/kennethreitz/repos?page=1&per_page=10'
# r = requests.head(url=url)
# r.headers['link']
# '<https://api.github.com/users/kennethreitz/repos?page=2&per_page=10>; rel="next", <https://api.github.com/users/
# kennethreitz/repos?page=6&per_page=10>; rel="last"'
# Запросы будут автоматически анализировать эти заголовки ссылок и делать их легко потребляемыми:
# r.links["next"]
# {'url': 'https://api.github.com/users/kennethreitz/repos?page=2&per_page=10', 'rel': 'next'}
# r.links["last"]
# {'url': 'https://api.github.com/users/kennethreitz/repos?page=7&per_page=10', 'rel': 'last'}
# Транспортные адаптеры
# Начиная с версии 1.0.0, Requests перешел на модульную внутреннюю структуру. Частично это было сделано для реализации
# транспортных адаптеров, первоначально описанных здесь . Транспортные адаптеры предоставляют механизм для определения
# методов взаимодействия для службы HTTP. В частности, они позволяют применять конфигурацию для каждой службы.
# Requests поставляется с одним транспортным адаптером, расширением HTTPAdapter. Этот адаптер обеспечивает
# взаимодействие запросов по умолчанию с HTTP и HTTPS с использованием мощной библиотеки urllib3 . Каждый раз, когда
# Session инициализируется запрос, один из них прикрепляется к Sessionобъекту для HTTP, а другой - для HTTPS.
# Запросы позволяют пользователям создавать и использовать свои собственные транспортные адаптеры, обеспечивающие
# определенные функции. После создания транспортный адаптер можно подключить к объекту сеанса вместе с указанием того,
# к каким веб-службам он должен применяться.
# s = requests.Session()
# s.mount('https://github.com/', MyAdapter())
# Вызов монтирования регистрирует конкретный экземпляр транспортного адаптера с префиксом. После монтирования любой
# HTTP-запрос, сделанный с использованием этого сеанса, URL-адрес которого начинается с данного префикса, будет
# использовать данный транспортный адаптер.
# Многие детали реализации транспортного адаптера выходят за рамки этой документации, но взгляните на следующий пример
# для простого варианта использования SSL. Более того, вы можете рассмотреть создание подкласса BaseAdapter.
# Пример: конкретная версия SSL
# Команда запросов сделала конкретный выбор в пользу использования той версии SSL, которая установлена по умолчанию в
# базовой библиотеке ( urllib3 ). Обычно это нормально, но время от времени вам может понадобиться подключиться к
# конечной точке службы, которая использует версию, несовместимую с версией по умолчанию.
# Для этого можно использовать транспортные адаптеры, взяв большую часть существующей реализации HTTPAdapter и добавив
# параметр ssl_version, который передается в urllib3 . Мы создадим транспортный адаптер, который инструктирует
# библиотеку использовать SSLv3:
# import ssl
# from urllib3.poolmanager import PoolManager
# from requests.adapters import HTTPAdapter
# class Ssl3HttpAdapter(HTTPAdapter):
#     """"Transport adapter" that allows us to use SSLv3."""
#
#     def init_poolmanager(self, connections, maxsize, block=False):
#         self.poolmanager = PoolManager(
#             num_pools=connections, maxsize=maxsize,
#             block=block, ssl_version=ssl.PROTOCOL_SSLv3)
# Блокирующий или неблокирующий?
# При наличии транспортного адаптера по умолчанию Requests не обеспечивает никакого неблокирующего ввода-вывода.
# Response.content Свойство будет блокировать , пока весь ответ не был загружен. Если вам требуется большая детализация,
# функции потоковой передачи библиотеки (см. Раздел «Потоковые запросы» ) позволяют получать меньшие количества ответов
# за раз. Однако эти вызовы все равно будут блокироваться.
# Если вас беспокоит использование блокировки ввода-вывода, существует множество проектов, в которых запросы сочетаются
# с одной из фреймворков асинхронности Python. Отличными примерами являются запросы-потоки , grequests ,
# запросы-фьючерсы и httpx .
# Порядок заголовков
# В необычных обстоятельствах вы можете захотеть предоставить заголовки в упорядоченном порядке. Если вы передаете
# OrderedDictк headersключевому слову аргумента, который будет предоставлять заголовки с упорядочением. Однако порядок
# заголовков по умолчанию, используемых запросами, будет предпочтительным, что означает, что если вы переопределите
# заголовки по умолчанию в headersаргументе ключевого слова, они могут отображаться не по порядку по сравнению с другими
# заголовками в этом аргументе ключевого слова.
# Если это проблематично, пользователям следует рассмотреть возможность установки заголовков по умолчанию для Session
# объекта, задав значение Sessioncustom OrderedDict. Такой порядок всегда будет предпочтительнее.
# Таймауты
# Для большинства запросов к внешним серверам должен быть привязан тайм-аут на случай, если сервер не отвечает
# своевременно. По умолчанию для запросов не истекает время ожидания, если явно не задано значение времени ожидания.
# Без тайм-аута ваш код может зависнуть на несколько минут или больше.
# Подключения таймаут количество секунд запросов будет ждать ваш клиент , чтобы установить соединение с удаленным компьютером (соответствующее соединение) ( ) вызова на сокете. Рекомендуется устанавливать время ожидания подключения немного больше, чем кратное 3, что является окном повторной передачи TCP-пакетов по умолчанию .
# После того, как ваш клиент подключился к серверу и отправил HTTP-запрос, таймаут чтения - это количество секунд, в течение которых клиент будет ждать, пока сервер отправит ответ. (В частности, это количество секунд, в течение которых клиент будет ждать между байтами, отправленными с сервера. В 99,9% случаев это время до того, как сервер отправит первый байт).
# Если вы укажете одно значение для тайм-аута, например:
# r = requests.get('https://github.com', timeout=5)
# Значение тайм-аута будет применяться как connectк read тайм-аутам, так и к тайм-аутам. Укажите кортеж, если вы хотите установить значения отдельно:
# r = requests.get('https://github.com', timeout=(3.05, 27))
# Если удаленный сервер работает очень медленно, вы можете указать запросам постоянно ждать ответа, передав None в
# качестве значения тайм-аута и затем получив чашку кофе.
# r = requests.get('https://github.com', timeout=None)

# Интерфейс разработчика
# Эта часть документации охватывает все интерфейсы запросов. Для частей, где запросы зависят от внешних библиотек, мы документируем наиболее важные прямо здесь и даем ссылки на каноническую документацию.
# Основной интерфейс
# Доступ ко всем функциям запросов можно получить с помощью этих 7 методов. Все они возвращают экземпляр Responseобъекта.
# Запросы. запрос ( метод , URL , ** kwargs )
# Создает и отправляет Request.
# Параметры
# метод - метод для нового Request объекта: GET, OPTIONS, HEAD, POST, PUT, PATCH, или DELETE.
# url - URL нового Requestобъекта.
# metric - (необязательно) Словарь, список кортежей или байтов для отправки в строке запроса для Request.
# data - (необязательно) словарь, список кортежей, байтов или файловый объект для отправки в теле Request.
# json - (необязательно) сериализуемый объект Python в формате JSON для отправки в теле файла Request.
# заголовки - (необязательно) Словарь заголовков HTTP для отправки с расширением Request.
# cookies - (необязательно) объект Dict или CookieJar для отправки с расширением Request.
# files - (необязательно) Словарь (или ) для загрузки составной кодировки. может быть кортежем из 2 , 3 или 4 кортежей,
# где - строка, определяющая тип содержимого данного файла, и dict-подобный объект, содержащий дополнительные заголовки,
# добавляемые для файла.'name': file-like-objects{'name': file-tuple}file-tuple('filename', fileobj)('filename', fileobj, 'content_type')('filename', fileobj, 'content_type', custom_headers)'content-type'custom_headers
# auth - (необязательно) кортеж Auth для включения Basic / Digest / Custom HTTP Auth.
# timeout ( float или tuple ) - (необязательно) Сколько секунд ждать, пока сервер отправит данные, прежде чем отказаться, как float или кортеж (время ожидания соединения, время ожидания чтения) .
# allow_redirects ( bool ) - (необязательно) логический. Включение / отключение перенаправления GET / OPTIONS / POST / PUT / PATCH / DELETE / HEAD. По умолчанию True.
# прокси - (необязательно) протокол сопоставления словаря с URL-адресом прокси.
# verify - (необязательно) Либо логическое значение, в этом случае оно определяет, проверяем ли мы сертификат TLS
# сервера, либо строку, и в этом случае это должен быть путь к используемому пакету CA. По умолчанию True.
# stream - (необязательно) если False, содержимое ответа будет немедленно загружено.
# cert - (необязательно), если String, путь к файлу сертификата клиента ssl (.pem). Если Tuple, пара ('cert', 'name').
# Возврат - # Response объект
# Тип возврата - # запросы.Ответ
# Использование:
# import requests
# req = requests.request('GET', 'https://httpbin.org/get')
# req
# <Response [200]>
# Запросы. голова ( url , ** kwargs )
# Отправляет запрос HEAD.
# Параметры
# url - URL нового Requestобъекта.
# ** kwargs - Необязательные аргументы, которые requestпринимает. Если allow_redirects не указан , будет установлено
# значение False (в отличие от requestповедения по умолчанию ).
# Возврат
# Response объект
# Тип возврата
# запросы.Ответ
# Запросы. get ( url , metric = None , ** kwargs )[источник]
# Отправляет запрос GET.
# Параметры
# url - URL нового Requestобъекта.
# metric - (необязательно) Словарь, список кортежей или байтов для отправки в строке запроса для Request.
# ** kwargs - Необязательные аргументы, которые requestпринимает.
# Возврат
# Response объект
# Тип возврата
# запросы.Ответ
# Запросы. post ( url , data = None , json = None , ** kwargs )[источник]
# Отправляет запрос POST.
# Параметры
# url - URL нового Requestобъекта.
# data - (необязательно) словарь, список кортежей, байтов или файловый объект для отправки в теле Request.
# json - (необязательно) данные json для отправки в теле файла Request.
# ** kwargs - Необязательные аргументы, которые request принимает.
# Возврат
# Response объект
# Тип возврата
# запросы.Ответ
# Запросы. положить ( url , data = None , ** kwargs )[источник]
# Отправляет запрос PUT.
# Параметры
# url - URL нового Request объекта.
# data - (необязательно) словарь, список кортежей, байтов или файловый объект для отправки в теле Request.
# json - (необязательно) данные json для отправки в теле файла Request.
# ** kwargs - Необязательные аргументы, которые requestпринимает.
# Возврат
# Response объект
# Тип возврата
# запросы.Ответ
# Запросы. патч ( url , data = None , ** kwargs )[источник]
# Отправляет запрос PATCH.
# Параметры
# url - URL нового Request объекта.
# data - (необязательно) словарь, список кортежей, байтов или файловый объект для отправки в теле Request.
# json - (необязательно) данные json для отправки в теле файла Request.
# ** kwargs - Необязательные аргументы, которые requestпринимает.
# Возврат
# Response объект
# Тип возврата
# запросы.Ответ
# Запросы. удалить ( URL , ** kwargs )[источник]
# Отправляет запрос на УДАЛЕНИЕ.
# Параметры
# url - URL нового Request объекта.
# ** kwargs - Необязательные аргументы, которые requestпринимает.
# Возврат
# Response объект
# Тип возврата
# запросы.Ответ
# Исключения
# запросы на исключение . RequestException ( * аргументы , ** kwargs )[источник]
# При обработке вашего запроса возникла неоднозначная исключительная ситуация.
# запросы на исключение . ConnectionError ( * аргументы , ** kwargs )[источник]
# Произошла ошибка подключения.
# запросы на исключение . HTTPError ( * аргументы , ** kwargs )[источник]
# Произошла ошибка HTTP.
# запросы на исключение . URLRequired ( * аргументы , ** kwargs )[источник]
# Для запроса требуется действующий URL.
# запросы на исключение . TooManyRedirects ( * аргументы , ** kwargs )[источник]
# Слишком много перенаправлений.
# запросы на исключение . ConnectTimeout ( * аргументы , ** kwargs )[источник]
# Истекло время ожидания запроса при попытке подключения к удаленному серверу.
# Запросы, вызвавшие эту ошибку, можно безопасно повторить.
# запросы на исключение . ReadTimeout ( * аргументы , ** kwargs )[источник]
# Сервер не отправил никаких данных за отведенное время.
# запросы на исключение . Тайм-аут ( * args , ** kwargs )[источник]
# Время ожидания запроса истекло.
#
# При обнаружении этой ошибки будут обнаружены как ошибки, так ConnectTimeoutи ReadTimeout.
#
# Запросить сеанс
# запросы класса . Сессия[источник]
# Сеанс запросов.
#
# Обеспечивает сохранение файлов cookie, создание пулов соединений и настройку.
#
# Основное использование:
#
# import requests
# s = requests.Session()
# s.get('https://httpbin.org/get')
# <Response [200]>
# Или как менеджер контекста:
#
# with requests.Session() as s:
#     s.get('https://httpbin.org/get')
# <Response [200]>
# auth
# Кортеж или объект аутентификации по умолчанию, к которому нужно присоединиться Request.
#
# сертификат
# Сертификат клиента SSL по умолчанию, если String, путь к файлу сертификата клиента ssl (.pem). Если Tuple, пара ('cert', 'name').
#
# закрыть ( )[источник]
# Закрывает все адаптеры и, таким образом, сеанс
#
# куки
# CookieJar, содержащий все невыполненные на данный момент файлы cookie, установленные в этом сеансе. По умолчанию это a RequestsCookieJar, но может быть любой другой cookielib.CookieJarсовместимый объект.
#
# удалить ( URL , ** kwargs )[источник]
# Отправляет запрос на УДАЛЕНИЕ. Возвращает Responseобъект.
#
# Параметры
# url - URL нового Requestобъекта.
#
# ** kwargs - Необязательные аргументы, которые requestпринимает.
#
# Тип возврата
# запросы.Ответ
#
# получить ( URL , ** kwargs )[источник]
# Отправляет запрос GET. Возвращает Responseобъект.
#
# Параметры
# url - URL нового Requestобъекта.
#
# ** kwargs - Необязательные аргументы, которые requestпринимает.
#
# Тип возврата
# запросы.Ответ
#
# get_adapter ( URL )[источник]
# Возвращает соответствующий адаптер подключения для данного URL-адреса.
#
# Тип возврата
# request.adapters.BaseAdapter
#
# get_redirect_target ( соответственно )
# Получает ответ. Возвращает URI перенаправления илиNone
#
# голова ( url , ** kwargs )[источник]
# Отправляет запрос HEAD. Возвращает Responseобъект.
#
# Параметры
# url - URL нового Requestобъекта.
#
# ** kwargs - Необязательные аргументы, которые requestпринимает.
#
# Тип возврата
# запросы.Ответ
#
# заголовки
# Словарь заголовков без учета регистра, который будет отправляться при каждой Requestотправке из этого Session.
#
# крючки
# Крючки для обработки событий.
#
# max_redirects
# Максимальное разрешенное количество перенаправлений. Если запрос превышает этот предел, возникает TooManyRedirectsисключение. По умолчанию используется значение requests.models.DEFAULT_REDIRECT_LIMIT, равное 30.
#
# merge_environment_settings ( URL , прокси , поток , проверка , сертификат )[источник]
# Проверьте среду и объедините ее с некоторыми настройками.
#
# Тип возврата
# диктовать
#
# крепление ( приставка , переходник )[источник]
# Регистрирует адаптер подключения к префиксу.
#
# Адаптеры отсортированы в порядке убывания длины префикса.
#
# варианты ( url , ** kwargs )[источник]
# Отправляет запрос OPTIONS. Возвращает Responseобъект.
#
# Параметры
# url - URL нового Requestобъекта.
#
# ** kwargs - Необязательные аргументы, которые requestпринимает.
#
# Тип возврата
# запросы.Ответ
#
# metric
# Словарь данных строки запроса для прикрепления к каждому Request. Значения словаря могут быть списками для представления многозначных параметров запроса.
#
# патч ( url , data = None , ** kwargs )[источник]
# Отправляет запрос PATCH. Возвращает Responseобъект.
#
# Параметры
# url - URL нового Requestобъекта.
#
# data - (необязательно) словарь, список кортежей, байтов или файловый объект для отправки в теле Request.
#
# ** kwargs - Необязательные аргументы, которые requestпринимает.
#
# Тип возврата
# запросы.Ответ
#
# post ( url , data = None , json = None , ** kwargs )[источник]
# Отправляет запрос POST. Возвращает Responseобъект.
#
# Параметры
# url - URL нового Requestобъекта.
#
# data - (необязательно) словарь, список кортежей, байтов или файловый объект для отправки в теле Request.
#
# json - (необязательно) json для отправки в теле файла Request.
#
# ** kwargs - Необязательные аргументы, которые requestпринимает.
#
# Тип возврата
# запросы.Ответ
#
# prepare_request ( запрос )[источник]
# Создает объект PreparedRequestдля передачи и возвращает его. У PreparedRequestнего есть настройки, объединенные из Requestэкземпляра и те из Session.
#
# Параметры
# request - Requestэкземпляр для подготовки с настройками этого сеанса.
#
# Тип возврата
# request.PreparedRequest
#
# прокси
# Протокол отображения словаря или протокол и хост к URL-адресу прокси (например, {'http': 'foo.bar:3128', 'http://host.name': 'foo.bar:4012'}), который будет использоваться на каждом Request.
#
# положить ( url , data = None , ** kwargs )[источник]
# Отправляет запрос PUT. Возвращает Responseобъект.
#
# Параметры
# url - URL нового Requestобъекта.
#
# data - (необязательно) словарь, список кортежей, байтов или файловый объект для отправки в теле Request.
#
# ** kwargs - Необязательные аргументы, которые requestпринимает.
#
# Тип возврата
# запросы.Ответ
#
# rebuild_auth ( подготовленный_запрос , ответ )
# При перенаправлении мы можем захотеть отключить аутентификацию из запроса, чтобы избежать утечки учетных данных. Этот метод разумно удаляет и повторно применяет аутентификацию, где это возможно, чтобы избежать потери учетных данных.
#
# rebuild_method ( подготовленный_запрос , ответ )
# При перенаправлении мы можем захотеть изменить метод запроса в зависимости от определенных спецификаций или поведения браузера.
#
# rebuild_proxies ( подготовленный_запрос , прокси )
# Этот метод повторно оценивает конфигурацию прокси, учитывая переменные среды. Если нас перенаправляют на URL, покрытый NO_PROXY, мы удаляем конфигурацию прокси. В противном случае мы устанавливаем отсутствующие ключи прокси для этого URL (на случай, если они были удалены предыдущим перенаправлением).
#
# При необходимости этот метод также заменяет заголовок Proxy-Authorization.
#
# Тип возврата
# диктовать
#
# request ( method , url , metric = None , data = None , headers = None , cookies = None , files = None , auth = None , timeout = None , allow_redirects = True , proxies = None , hooks = None , stream = None , verify =Нет , cert = Нет , json = Нет )[источник]
# Создает Request, подготавливает и отправляет. Возвращает Responseобъект.
#
# Параметры
# method - метод для нового Requestобъекта.
#
# url - URL нового Requestобъекта.
#
# metric - (необязательно) Словарь или байты, которые должны быть отправлены в строке запроса для Request.
#
# data - (необязательно) словарь, список кортежей, байтов или файловый объект для отправки в теле Request.
#
# json - (необязательно) json для отправки в теле файла Request.
#
# заголовки - (необязательно) Словарь заголовков HTTP для отправки с расширением Request.
#
# cookies - (необязательно) объект Dict или CookieJar для отправки с расширением Request.
#
# files - (необязательно) Словарь для загрузки многокомпонентных кодировок.'filename': file-like-objects
#
# auth - (необязательно) Кортеж Auth или вызываемый, чтобы включить базовую / дайджест / настраиваемую HTTP-аутентификацию.
#
# timeout (с плавающей запятой или кортежем ) - (необязательно) Как долго ждать, пока сервер отправит данные, прежде чем отказаться, в виде числа с плавающей запятой или кортежа (таймаут соединения, таймаут чтения) .
#
# allow_redirects ( bool ) - (необязательно) По умолчанию установлено значение True.
#
# прокси - (необязательно) протокол сопоставления словаря или протокол и имя хоста с URL-адресом прокси.
#
# stream - (необязательно) следует ли сразу загружать содержимое ответа. По умолчанию False.
#
# verify - (необязательно) Либо логическое значение, в этом случае оно определяет, проверяем ли мы сертификат TLS сервера, либо строку, и в этом случае это должен быть путь к используемому пакету CA. По умолчанию True. Если установлено значение False, запросы будут принимать любой сертификат TLS, представленный сервером, и будут игнорировать несоответствия имени хоста и / или сертификаты с истекшим сроком действия, что сделает ваше приложение уязвимым для атак типа «человек посередине» (MitM). Параметр verify to False может быть полезен при локальной разработке или тестировании.
#
# cert - (необязательно), если String, путь к файлу сертификата клиента ssl (.pem). Если Tuple, пара ('cert', 'name').
#
# Тип возврата
# запросы.Ответ
#
# resolve_redirects ( resp , req , stream = False , timeout = None , verify = True , cert = None , proxies = None , yield_requests = False , ** adapter_kwargs )
# Получает ответ. Возвращает генератор ответов или запросов.
#
# отправить ( запрос , ** kwargs )[источник]
# Отправить заданный PreparedRequest.
#
# Тип возврата
# запросы.Ответ
#
# should_strip_auth ( old_url , new_url )
# Решите, нужно ли удалять заголовок авторизации при перенаправлении
#
# поток
# По умолчанию содержимое ответа потока.
#
# trust_env
# Настройки доверенной среды для конфигурации прокси, аутентификации по умолчанию и т.п.
#
# проверить
# Проверка SSL по умолчанию. По умолчанию True , требуя запросов на проверку сертификата TLS на удаленном конце. Если для параметра verify установлено значение False , запросы будут принимать любой сертификат TLS, представленный сервером, и будут игнорировать несоответствия имени хоста и / или сертификаты с истекшим сроком действия, что сделает ваше приложение уязвимым для атак типа «человек посередине» (MitM). Установите значение False только для тестирования.
#
# Классы нижнего уровня
# запросы класса . Запрос ( method = None , url = None , headers = None , files = None , data = None , metric = None , auth = None , cookies = None , hooks = None , json = None )[источник]
# Объект, созданный пользователем Request.
#
# Используется для подготовки файла PreparedRequest, который отправляется на сервер.
#
# Параметры
# method - HTTP-метод для использования.
#
# url - URL для отправки.
#
# заголовки - словарь заголовков для отправки.
#
# files - словарь файлов {filename: fileobject} для многокомпонентной загрузки.
#
# data - тело, которое нужно приложить к запросу. Если предоставлен словарь или список кортежей , будет выполнено кодирование формы.[(name, value)]
#
# json - json для тела, которое нужно прикрепить к запросу (если файлы или данные не указаны).
#
# metric - параметры URL для добавления к URL. Если предоставлен словарь или список кортежей , будет выполнено кодирование формы.[(name, value)]
#
# auth - обработчик аутентификации или кортеж (user, pass).
#
# cookies - словарь или CookieJar файлов cookie для прикрепления к этому запросу.
#
# хуки - словарь хуков обратного вызова, для внутреннего использования.
#
# Использование:
#
# import requests
# req = requests.Request('GET', 'https://httpbin.org/get')
# req.prepare()
# <PreparedRequest [GET]>
# deregister_hook ( событие , крючок )
# Отмените регистрацию ранее зарегистрированного крючка. Возвращает True, если перехватчик существовал, и False, если нет.
#
# подготовить ( )[источник]
# Создает объект PreparedRequestдля передачи и возвращает его.
#
# register_hook ( событие , крючок )
# Правильно пропишите крючок.
#
# запросы класса . Ответ[источник]
# ResponseОбъект, который содержит ответ сервера на запрос HTTP.
#
# недвижимость apparent_encoding
# Очевидная кодировка, предоставляемая библиотеками charset_normalizer или chardet.
#
# закрыть ( )[источник]
# Освобождает соединение обратно с пулом. После того, как этот метод был вызван, к базовому rawобъекту больше нельзя обращаться.
#
# Примечание. Обычно не требуется вызывать явно.
#
# содержание недвижимости
# Содержимое ответа в байтах.
#
# куки
# CookieJar файлов cookie, отправленных сервером.
#
# прошло
# Время, прошедшее между отправкой запроса и получением ответа (в виде timedelta). Это свойство конкретно измеряет время, затрачиваемое между отправкой первого байта запроса и завершением синтаксического анализа заголовков. Поэтому на него не влияет использование содержимого ответа или значения streamаргумента ключевого слова.
#
# кодировка
# Кодировка для декодирования при доступе к r.text.
#
# заголовки
# Словарь заголовков ответов без учета регистра. Например, headers['content-encoding']вернет значение 'Content-Encoding'заголовка ответа.
#
# история
# Список Responseобъектов из истории Запроса. Все ответы на переадресацию будут здесь. Список отсортирован от самого старого к самому последнему запросу.
#
# свойство is_permanent_redirect
# Истинно, если этот ответ является одной из постоянных версий перенаправления.
#
# свойство is_redirect
# Истинно, если этот ответ представляет собой правильно сформированное перенаправление HTTP, которое могло быть обработано автоматически (с помощью Session.resolve_redirects).
#
# iter_content ( chunk_size = 1 , decode_unicode = False )[источник]
# Перебирает данные ответа. Когда для запроса установлено значение stream = True, это позволяет избежать чтения содержимого сразу в память для больших ответов. Размер блока - это количество байтов, которое он должен прочитать в память. Это не обязательно длина каждого возвращаемого элемента, поскольку может происходить декодирование.
#
# chunk_size должен иметь тип int или None. Значение None будет работать по-разному в зависимости от значения потока . stream = True будет считывать данные по мере их поступления независимо от размера полученных фрагментов. Если stream = False, данные возвращаются как один фрагмент.
#
# Если decode_unicode имеет значение True, содержимое будет декодировано с использованием наилучшей доступной кодировки на основе ответа.
#
# iter_lines ( chunk_size = 512 , decode_unicode = False , delimiter = None )[источник]
# Перебирает данные ответа по одной строке за раз. Когда для запроса установлено значение stream = True, это позволяет избежать чтения содержимого сразу в память для больших ответов.
#
# Примечание
# Этот метод небезопасен для повторного входа.
#
# json ( ** kwargs )[источник]
# Возвращает содержимое ответа в кодировке json, если оно есть.
#
# Параметры
# ** kwargs - Необязательные аргументы, которые json.loadsпринимает.
#
# Поднимает
# request.exceptions.JSONDecodeError - Если тело ответа не содержит допустимого json.
#
# ссылки на недвижимость
# Возвращает проанализированные ссылки заголовка ответа, если таковые имеются.
#
# недвижимость рядом
# Возвращает PreparedRequest для следующего запроса в цепочке перенаправления, если таковой имеется.
#
# собственность в порядке
# Возвращает True, если status_codeменьше 400, и False, если нет.
#
# Этот атрибут проверяет, находится ли код состояния ответа от 400 до 600, чтобы узнать, была ли ошибка клиента или сервера. Если код состояния находится между 200 и 400, это вернет True. Это не проверка правильности кода ответа .200 OK
#
# Raise_for_status ( )[источник]
# Повышает HTTPError, если таковой имел место.
#
# сырье
# Файловое объектное представление ответа (для расширенного использования). Использование rawтребует, чтобы это stream=Trueбыло установлено по запросу. Это требование не распространяется на внутреннее использование запросов.
#
# причина
# Текстовая причина ответа HTTP-статуса, например, «Не найдено» или «ОК».
#
# запрос
# PreparedRequestОбъект , к которому это ответ.
#
# status_code
# Целочисленный код ответа HTTP-статуса, например 404 или 200.
#
# текст свойства
# Содержание ответа в юникоде.
#
# Если Response.encoding - None, кодировка будет угадана с помощью charset_normalizerили chardet.
#
# Кодировка содержимого ответа определяется исключительно на основе заголовков HTTP, в точности следуя RFC 2616. Если вы можете воспользоваться знаниями, не связанными с HTTP, чтобы лучше угадать кодировку, вам следует установить r.encodingсоответствующие настройки перед доступом к этому свойству.
#
# url
# Конечный URL-адрес ответа.
#
# Классы  -нижнего уровня
# запросы класса . PreparedRequest[источник]
# Полностью изменяемый PreparedRequestобъект, содержащий точные байты, которые будут отправлены на сервер.
#
# Экземпляры создаются из Requestобъекта и не должны создаваться вручную; это может вызвать нежелательные эффекты.
#
# Использование:
#
# import requests
# req = requests.Request('GET', 'https://httpbin.org/get')
# r = req.prepare()
# r
# <PreparedRequest [GET]>
#
# s = requests.Session()
# s.send(r)
# <Response [200]>
# тело
# тело запроса для отправки на сервер.
#
# deregister_hook ( событие , крючок )
# Отмените регистрацию ранее зарегистрированного крючка. Возвращает True, если перехватчик существовал, и False, если нет.
#
# заголовки
# словарь заголовков HTTP.
#
# крючки
# словарь перехватчиков обратного вызова для внутреннего использования.
#
# метод
# HTTP-глагол для отправки на сервер.
#
# свойство path_url
# Создайте URL-адрес пути для использования.
#
# подготовить ( method = None , url = None , headers = None , files = None , data = None , metric = None , auth = None , cookies = None , hooks = None , json = None )[источник]
# Подготавливает весь запрос с заданными параметрами.
#
# prepare_auth ( авт , URL = '' )[источник]
# Подготавливает указанные данные HTTP-аутентификации.
#
# prepare_body ( данные , файлы , json = Нет )[источник]
# Подготавливает данные тела HTTP.
#
# prepare_content_length ( тело )[источник]
# Подготовить заголовок Content-Length на основе метода и тела запроса
#
# prepare_cookies ( файлы cookie )[источник]
# Подготавливает данные HTTP cookie.
#
# Эта функция в конечном итоге генерирует Cookieзаголовок из заданных файлов cookie с помощью cookielib. Из-за конструкции cookielib заголовок не будет регенерирован, если он уже существует, что означает, что эта функция может быть вызвана только один раз за время существования PreparedRequestобъекта. Любые последующие вызовы не prepare_cookiesбудут иметь фактического эффекта, если заголовок «Cookie» не будет удален заранее.
#
# prepare_headers ( заголовки )[источник]
# Подготавливает заданные заголовки HTTP.
#
# prepare_hooks ( крючки )[источник]
# Готовит данные крючки.
#
# prepare_method ( метод )[источник]
# Подготавливает данный HTTP-метод.
#
# prepare_url ( URL , параметры )[источник]
# Подготавливает указанный URL-адрес HTTP.
#
# register_hook ( событие , крючок )
# Правильно пропишите крючок.
#
# url
# URL-адрес HTTP для отправки запроса.
#
# класс requests.adapters. BaseAdapter[источник]
# Базовый транспортный адаптер
#
# закрыть ( )[источник]
# Очищает определенные элементы адаптера.
#
# send ( запрос , поток = False , тайм-аут = None , verify = True , cert = None , proxies = None )[источник]
# Отправляет объект PreparedRequest. Возвращает объект ответа.
#
# Параметры
# запрос - PreparedRequestОтправляемый.
#
# stream - (необязательно) следует ли передавать содержимое запроса в потоковом режиме.
#
# timeout (с плавающей запятой или кортежем ) - (необязательно) Как долго ждать, пока сервер отправит данные, прежде чем отказаться, в виде числа с плавающей запятой или кортежа (таймаут соединения, таймаут чтения) .
#
# verify - (необязательно) Либо логическое значение, в этом случае оно определяет, проверяем ли мы сертификат TLS сервера, либо строку, и в этом случае это должен быть путь к пакету CA для использования
#
# cert - (необязательно) любой доверенный сертификат SSL, предоставленный пользователем.
#
# прокси - (необязательно) словарь прокси, применяемый к запросу.
#
# класс requests.adapters. HTTPAdapter ( pool_connections = 10 , pool_maxsize = 10 , max_retries = 0 , pool_block = False )[источник]
# Встроенный HTTP-адаптер для urllib3.
#
# Предоставляет общий интерфейс для сеансов запросов для связи с URL-адресами HTTP и HTTPS путем реализации интерфейса транспортного адаптера. Этот класс обычно создается Sessionклассом под прикрытием.
#
# Параметры
# pool_connections - количество пулов соединений urllib3 для кеширования.
#
# pool_maxsize - максимальное количество соединений для сохранения в пуле.
#
# max_retries - максимальное количество попыток, которое должно предпринять каждое соединение. Обратите внимание: это относится только к неудачным поискам DNS, соединениям сокетов и тайм-аутам соединения, но никогда к запросам, по которым данные попали на сервер. По умолчанию Requests не пытается повторять неудачные подключения. Если вам нужен детальный контроль над условиями, при которых мы повторяем запрос, импортируйте Retryкласс urllib3 и передайте его вместо этого.
#
# pool_block - должен ли пул подключений блокироваться для подключений.
#
# Использование:
#
# import requests
# s = requests.Session()
# a = requests.adapters.HTTPAdapter(max_retries=3)
# s.mount('http://', a)
# add_headers ( запрос , ** kwargs )[источник]
# Добавьте заголовки, необходимые для соединения. Начиная с версии 2.0 по умолчанию это ничего не делает, но оставлено для отмены пользователями, которые создают подкласс HTTPAdapter.
#
# Это не должно вызываться из пользовательского кода и доступно только для использования при создании подкласса HTTPAdapter.
#
# Параметры
# request - PreparedRequestобъект, в который нужно добавить заголовки.
#
# kwargs - аргументы ключевого слова из вызова send ().
#
# build_response ( req , resp )[источник]
# Строит Responseобъект из ответа urllib3. Это не должно вызываться из пользовательского кода и предоставляется только для использования при создании подкласса HTTPAdapter
#
# Параметры
# req - PreparedRequestиспользуется для генерации ответа.
#
# resp - объект ответа urllib3.
#
# Тип возврата
# запросы.Ответ
#
# cert_verify ( Conn , URL , проверьте , CERT )[источник]
# Проверьте сертификат SSL. Этот метод не следует вызывать из пользовательского кода, его можно использовать только при создании подкласса HTTPAdapter.
#
# Параметры
# Конн - The urllib3 объект соединения , связанный с серт.
#
# url - запрошенный URL.
#
# verify - Либо логическое значение, в этом случае оно определяет, проверяем ли мы сертификат TLS сервера, либо строку, и в этом случае это должен быть путь к пакету CA для использования
#
# cert - сертификат SSL для проверки.
#
# закрыть ( )[источник]
# Избавляется от любого внутреннего состояния.
#
# В настоящее время это закрывает PoolManager и любой активный ProxyManager, который закрывает все объединенные соединения.
#
# get_connection ( url , proxies = None )[источник]
# Возвращает соединение urllib3 для данного URL. Это не должно вызываться из пользовательского кода и доступно только для использования при создании подкласса HTTPAdapter.
#
# Параметры
# url - URL-адрес для подключения.
#
# proxies - (необязательно) словарь прокси в стиле запросов, используемых в этом запросе.
#
# Тип возврата
# urllib3.ConnectionPool
#
# init_poolmanager ( соединения , maxsize , block = False , ** pool_kwargs )[источник]
# Инициализирует urllib3 PoolManager.
#
# Этот метод не следует вызывать из пользовательского кода, его можно использовать только при создании подкласса HTTPAdapter.
#
# Параметры
# соединения - количество пулов соединений urllib3 для кеширования.
#
# maxsize - максимальное количество соединений для сохранения в пуле.
#
# block - блокировать, когда нет свободных подключений.
#
# pool_kwargs - Дополнительные аргументы ключевого слова, используемые для инициализации диспетчера пула.
#
# proxy_headers ( прокси )[источник]
# Возвращает словарь заголовков для добавления к любому запросу, отправляемому через прокси. Это работает с магией urllib3, чтобы гарантировать, что они правильно отправляются на прокси, а не в туннелированном запросе, если используется CONNECT.
#
# Это не должно вызываться из пользовательского кода и доступно только для использования при создании подкласса HTTPAdapter.
#
# Параметры
# proxy - URL-адрес прокси, используемого для этого запроса.
#
# Тип возврата
# диктовать
#
# proxy_manager_for ( прокси , ** proxy_kwargs )[источник]
# Вернуть urllib3 ProxyManager для данного прокси.
#
# Этот метод не следует вызывать из пользовательского кода, его можно использовать только при создании подкласса HTTPAdapter.
#
# Параметры
# proxy - прокси, для которого требуется вернуть urllib3 ProxyManager.
#
# proxy_kwargs - Дополнительные аргументы ключевого слова, используемые для настройки Proxy Manager.
#
# Возврат
# ProxyManager
#
# Тип возврата
# urllib3.ProxyManager
#
# request_url ( запрос , прокси )[источник]
# Получите URL-адрес, который будет использоваться при окончательном запросе.
#
# Если сообщение отправляется через прокси-сервер HTTP, необходимо использовать полный URL-адрес. В противном случае мы должны использовать только часть пути URL-адреса.
#
# Это не должно вызываться из пользовательского кода и доступно только для использования при создании подкласса HTTPAdapter.
#
# Параметры
# запрос - PreparedRequestОтправляемый.
#
# прокси - словарь схем или схем и хостов для URL-адресов прокси.
#
# Тип возврата
# ул.
#
# send ( запрос , поток = False , тайм-аут = None , verify = True , cert = None , proxies = None )[источник]
# Отправляет объект PreparedRequest. Возвращает объект ответа.
#
# Параметры
# запрос - PreparedRequestОтправляемый.
#
# stream - (необязательно) следует ли передавать содержимое запроса в потоковом режиме.
#
# timeout ( float или tuple или urllib3 Timeout object ) - (необязательно) Как долго ждать, пока сервер отправит данные, прежде чем отказаться, в виде числа с плавающей запятой или кортежа (время ожидания соединения, таймаут чтения) .
#
# verify - (необязательно) Либо логическое значение, в этом случае оно определяет, проверяем ли мы сертификат TLS сервера, либо строку, и в этом случае это должен быть путь к пакету CA для использования
#
# cert - (необязательно) любой доверенный сертификат SSL, предоставленный пользователем.
#
# прокси - (необязательно) словарь прокси, применяемый к запросу.
#
# Тип возврата
# запросы.Ответ
#
# Аутентификация
# класс requests.auth. AuthBase[источник]
# Базовый класс, от которого наследуются все реализации аутентификации
#
# класс requests.auth. HTTPBasicAuth ( имя пользователя , пароль )[источник]
# Присоединяет базовую аутентификацию HTTP к заданному объекту запроса.
#
# класс requests.auth. HTTPProxyAuth ( имя пользователя , пароль )[источник]
# Присоединяет HTTP-аутентификацию прокси к заданному объекту запроса.
#
# класс requests.auth. HTTPDigestAuth ( имя пользователя , пароль )[источник]
# Присоединяет дайджест-аутентификацию HTTP к заданному объекту запроса.
#
# Кодировки
# request.utils. get_encodings_from_content ( контент )[источник]
# Возвращает кодировки из заданной строки содержимого.
#
# Параметры
# content - строка байтов, из которой нужно извлечь кодировки.
#
# request.utils. get_encoding_from_headers ( заголовки )[источник]
# Возвращает кодировки из заданного HTTP-заголовка Dict.
#
# Параметры
# заголовки - словарь, из которого нужно извлечь кодировку.
#
# Тип возврата
# ул.
#
# request.utils. get_unicode_from_response ( г )[источник]
# Возвращает запрошенный контент обратно в юникоде.
#
# Параметры
# r - объект ответа, из которого нужно получить содержимое Unicode.
#
# Пытался:
#
# кодировка из типа содержимого
#
# отступить и заменить все символы Юникода
#
# Тип возврата
# ул.
#
# Файлы cookie
# request.utils. dict_from_cookiejar ( cj )[источник]
# Возвращает словарь "ключ-значение" из CookieJar.
#
# Параметры
# cj - объект CookieJar, из которого нужно извлечь файлы cookie.
#
# Тип возврата
# диктовать
#
# request.utils. add_dict_to_cookiejar ( cj , cookie_dict )[источник]
# Возвращает CookieJar из словаря ключ / значение.
#
# Параметры
# cj - CookieJar для вставки файлов cookie.
#
# cookie_dict - набор ключей / значений для вставки в CookieJar.
#
# Тип возврата
# CookieJar
#
# request.cookies. cookiejar_from_dict ( cookie_dict , cookiejar = None , overwrite = True )[источник]
# Возвращает CookieJar из словаря ключ / значение.
#
# Параметры
# cookie_dict - набор ключей / значений для вставки в CookieJar.
#
# cookiejar - (необязательно) cookiejar для добавления файлов cookie.
#
# overwrite - (необязательно) Если False, файлы cookie, уже находящиеся в банке, не заменяются новыми.
#
# Тип возврата
# CookieJar
#
# класс requests.cookies. RequestsCookieJar ( policy = None )[источник]
# Класс совместимости; является cookielib.CookieJar, но предоставляет интерфейс dict.
#
# Это CookieJar, который мы создаем по умолчанию для запросов и сеансов, в которых он не указан, поскольку некоторые клиенты могут ожидать, что response.cookies и session.cookies будут поддерживать операции dict.
#
# Запросы не используют внутренний интерфейс dict; это просто для совместимости с внешним клиентским кодом. Весь код запросов должен работать из коробки с экземплярами, предоставленными извне CookieJar, например, LWPCookieJarи FileCookieJar.
#
# В отличие от обычного CookieJar, этот класс можно мариновать.
#
# Предупреждение
# словарные операции, которые обычно являются O (1), могут быть O (n).
#
# add_cookie_header ( запрос )
# Добавьте в запрос правильный заголовок Cookie: (объект urllib.request.Request).
#
# Заголовок Cookie2 также добавляется, если policy.hide_cookie2 не истинно.
#
# clear ( domain = None , path = None , name = None )
# Удалите некоторые файлы cookie.
#
# Вызов этого метода без аргументов приведет к удалению всех файлов cookie. Если указан один аргумент, будут удалены только файлы cookie, принадлежащие этому домену. Если задано два аргумента, файлы cookie, принадлежащие указанному пути в этом домене, удаляются. Если задано три аргумента, cookie с указанным именем, путем и доменом удаляется.
#
# Вызывает ошибку KeyError, если соответствующий файл cookie не существует.
#
# clear_expired_cookies ( )
# Отменить все просроченные куки.
#
# Вероятно, вам не нужно вызывать этот метод: просроченные файлы cookie никогда не отправляются обратно на сервер (при условии, что вы используете DefaultCookiePolicy), этот метод время от времени вызывается самим CookieJar, а метод .save () не будет в любом случае сохранить просроченные куки (если вы не попросите иначе, передав истинный аргумент ignore_expires).
#
# clear_session_cookies ( )
# Отменить все файлы cookie сеанса.
#
# Обратите внимание, что метод .save () в любом случае не будет сохранять файлы cookie сеанса, если вы не укажете иное, передав истинный аргумент ignore_discard.
#
# копия ( )[источник]
# Верните копию этого RequestsCookieJar.
#
# extract_cookies ( ответ , запрос )
# Извлеките файлы cookie из ответа, если это допустимо для данного запроса.
#
# get ( имя , по умолчанию = Нет , домен = Нет , путь = Нет )[источник]
# Dict-подобный get (), который также поддерживает необязательные аргументы домена и пути, чтобы разрешить конфликты имен из-за использования одной банки cookie в нескольких доменах.
#
# Предупреждение
# операция O (n), а не O (1).
#
# get_dict ( домен = Нет , путь = Нет )[источник]
# Принимает в качестве аргумента необязательный домен и путь и возвращает простой старый Python dict пар имя-значение файлов cookie, которые соответствуют требованиям.
#
# Тип возврата
# диктовать
#
# get_policy ( )[источник]
# Вернуть использованный экземпляр CookiePolicy.
#
# предметы ( )[источник]
# Dict-like items (), который возвращает список кортежей значения имени из jar. Позволяет клиентскому коду вызывать dict(RequestsCookieJar)и получать ванильный Python dict пар ключ-значение.
#
# Смотрите также
# ключи () и значения ().
#
# iteritems ( )[источник]
# Dict-подобный iteritems (), который возвращает итератор кортежей значений имени из jar.
#
# Смотрите также
# iterkeys () и itervalues ​​().
#
# iterkeys ( )[источник]
# Dict-подобный iterkeys (), который возвращает итератор имен файлов cookie из jar.
#
# Смотрите также
# itervalues ​​() и iteritems ().
#
# itervalues ( )[источник]
# Dict-подобный itervalues ​​(), который возвращает итератор значений файлов cookie из jar.
#
# Смотрите также
# iterkeys () и iteritems ().
#
# ключи ( )[источник]
# Dict-подобные keys (), которые возвращают список имен файлов cookie из jar.
#
# Смотрите также
# values ​​() и items ().
#
# list_domains ( )[источник]
# Служебный метод для вывода списка всех доменов в банке.
#
# list_paths ( )[источник]
# Служебный метод для вывода списка всех путей в банке.
#
# make_cookies ( ответ , запрос )
# Возвращает последовательность объектов Cookie, извлеченных из объекта ответа.
#
# multiple_domains ( )[источник]
# Возвращает True, если в банке несколько доменов. В противном случае возвращает False.
#
# Тип возврата
# bool
#
# поп ( K [ , д ] ) → V, удалить указанный ключ и возвращают в соответствующее значение.
# Если ключ не найден, возвращается d, если он задан, в противном случае возникает KeyError.
#
# popitem ( ) → (к, V), удалить и вернуть некоторые (ключ, значение) пара
# как 2-кортеж; но поднимите KeyError, если D пуст.
#
# набор ( имя , значение , ** kwargs )[источник]
# Dict-подобный set (), который также поддерживает необязательные аргументы домена и пути, чтобы разрешить конфликты имен из-за использования одной банки cookie в нескольких доменах.
#
# set_cookie ( cookie , * аргументы , ** kwargs )[источник]
# Установите cookie, не проверяя, нужно ли его устанавливать.
#
# set_cookie_if_ok ( cookie , запрос )
# Установите cookie, если политика разрешает это делать.
#
# setdefault ( k [ , d ] ) → D. get (k, d), также установите D [k] = d, если k не входит в D
# обновление ( другое )[источник]
# Обновляет эту банку с помощью файлов cookie из другого CookieJar или типа dict
#
# значения ( )[источник]
# Dict-like values ​​(), который возвращает список значений файлов cookie из jar.
#
# Смотрите также
# ключи () и предметы ().
#
# класс requests.cookies. CookieConflictError[источник]
# Есть два файла cookie, которые соответствуют критериям, указанным в банке файлов cookie. Используйте .get и .set и включите аргументы домена и пути, чтобы быть более конкретным.
#
# with_traceback ( )
# Exception.with_traceback (tb) - установить self .__ traceback__ на tb и вернуть self.
#
# Поиск кода состояния
# Запросы. коды
# псевдоним <lookup 'status_codes'>
#
# codesОбъект определяет отображение общих имен для HTTP статусов для их числовых кодов, доступны либо в виде атрибутов или в качестве словарных элементов.
#
# Пример:
#
# import requests
# requests.codes['temporary_redirect']
# 307
# requests.codes.teapot
# 418
# requests.codes['\o/']
# 200
# Некоторые коды имеют несколько имен, и разрешены версии имен как в верхнем, так и в нижнем регистре. Так , например, codes.ok, codes.OKи codes.okayвсе соответствуют коду состояния 200 HTTP.
#
# 100: continue
#
# 101: switching_protocols
#
# 102: processing
#
# 103: checkpoint
#
# 122: uri_too_long,request_uri_too_long
#
# 200: ok, okay, all_ok, all_okay, all_good, \o/,✓
#
# 201: created
#
# 202: accepted
#
# 203: non_authoritative_info,non_authoritative_information
#
# 204: no_content
#
# 205: reset_content,reset
#
# 206: partial_content,partial
#
# 207: multi_status, multiple_status, multi_stati,multiple_stati
#
# 208: already_reported
#
# 226: im_used
#
# 300: multiple_choices
#
# 301: moved_permanently, moved,\o-
#
# 302: found
#
# 303: see_other,other
#
# 304: not_modified
#
# 305: use_proxy
#
# 306: switch_proxy
#
# 307: temporary_redirect, temporary_moved,temporary
#
# 308: permanent_redirect, resume_incomplete,resume
#
# 400: bad_request,bad
#
# 401: unauthorized
#
# 402: payment_required,payment
#
# 403: forbidden
#
# 404: not_found,-o-
#
# 405: method_not_allowed,not_allowed
#
# 406: not_acceptable
#
# 407: proxy_authentication_required, proxy_auth,proxy_authentication
#
# 408: request_timeout,timeout
#
# 409: conflict
#
# 410: gone
#
# 411: length_required
#
# 412: precondition_failed,precondition
#
# 413: request_entity_too_large
#
# 414: request_uri_too_large
#
# 415: unsupported_media_type, unsupported_media,media_type
#
# 416: requested_range_not_satisfiable, requested_range,range_not_satisfiable
#
# 417: expectation_failed
#
# 418: im_a_teapot, teapot,i_am_a_teapot
#
# 421: misdirected_request
#
# 422: unprocessable_entity,unprocessable
#
# 423: locked
#
# 424: failed_dependency,dependency
#
# 425: unordered_collection,unordered
#
# 426: upgrade_required,upgrade
#
# 428: precondition_required,precondition
#
# 429: too_many_requests,too_many
#
# 431: header_fields_too_large,fields_too_large
#
# 444: no_response,none
#
# 449: retry_with,retry
#
# 450: blocked_by_windows_parental_controls,parental_controls
#
# 451: unavailable_for_legal_reasons,legal_reasons
#
# 499: client_closed_request
#
# 500: internal_server_error, server_error, /o\,✗
#
# 501: not_implemented
#
# 502: bad_gateway
#
# 503: service_unavailable,unavailable
#
# 504: gateway_timeout
#
# 505: http_version_not_supported,http_version
#
# 506: variant_also_negotiates
#
# 507: insufficient_storage
#
# 509: bandwidth_limit_exceeded,bandwidth
#
# 510: not_extended
#
# 511: network_authentication_required, network_auth,network_authentication
#
# Переход на 1.x
# В этом разделе подробно описаны основные различия между 0.x и 1.x, и он предназначен для облегчения боли при обновлении.
#
# Изменения API
# Response.json теперь вызывается, а не является свойством ответа.
#
# import requests
# r = requests.get('https://api.github.com/events')
# r.json()   # This *call* raises an exception if JSON decoding fails
# SessionAPI изменился. Объекты сеансов больше не принимают параметры. Sessionтеперь также пишется с заглавной буквы, но sessionдля обратной совместимости он все еще может быть инстанциирован в нижнем регистре .
#
# s = requests.Session()    # formerly, session took parameters
# s.auth = auth
# s.headers.update(headers)
# r = s.get('https://httpbin.org/headers')
# Все перехватчики запросов были удалены, кроме «ответа».
#
# Помощники аутентификации разбиты на отдельные модули. Смотрите запросы-oauthlib и запросы-kerberos .
#
# Параметр потоковой передачи запросов был изменен с prefetchна, streamа логика была инвертирована. Кроме того, streamтеперь требуется для чтения необработанного ответа.
#
# # in 0.x, passing prefetch=False would accomplish the same thing
# r = requests.get('https://api.github.com/events', stream=True)
# for chunk in r.iter_content(8192):
#     ...
# configПараметр метода запросов был удален. Некоторые из этих параметров теперь настроены, Sessionнапример, для проверки активности и максимального количества перенаправлений. Параметр подробности следует обрабатывать, настраивая ведение журнала.
#
# import requests
# import logging
#
# # Enabling debugging at http.client level (requests->urllib3->http.client)
# # you will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# # the only thing missing will be the response.body which is not logged.
# try: # for Python 3
#     from http.client import HTTPConnection
# except ImportError:
#     from httplib import HTTPConnection
# HTTPConnection.debuglevel = 1
#
# logging.basicConfig() # you need to initialize logging, otherwise you will not see anything from requests
# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True
#
# requests.get('https://httpbin.org/headers')
# Лицензирование
# Одно ключевое отличие, не имеющее ничего общего с API, - это изменение лицензии с лицензии ISC на лицензию Apache 2.0 . Лицензия Apache 2.0 гарантирует, что вклады в запросы также подпадают под действие лицензии Apache 2.0.
#
# Переход на 2.x
# По сравнению с выпуском 1.0 было относительно мало обратно несовместимых изменений, но все же есть несколько проблем, о которых следует помнить в этом основном выпуске.
#
# Дополнительные сведения об изменениях в этом выпуске, включая новые API-интерфейсы, ссылки на соответствующие проблемы GitHub и некоторые исправления ошибок, см. В блоге Кори по этой теме.
#
# Изменения API
# Было внесено несколько изменений в способ обработки исключений в Requests. RequestExceptionтеперь является подклассом, IOErrorа не тем, RuntimeErrorчто более точно классифицирует тип ошибки. Кроме того, неверная escape-последовательность URL теперь вызывает подкласс, RequestExceptionа не a ValueError.
#
# requests.get('http://%zz/')   # raises requests.exceptions.InvalidURL
# Наконец, httplib.IncompleteReadисключения, вызванные неправильной кодировкой по фрагментам, теперь будут вызывать запросы ChunkedEncodingError.
#
# Немного изменился API прокси. Теперь требуется схема для URL-адреса прокси.
#
# proxies = {
#   "http": "10.10.1.10:3128",    # use http://10.10.1.10:3128 instead
# }
#
# # In requests 1.x, this was legal, in requests 2.x,
# #  this raises requests.exceptions.MissingSchema
# requests.get("http://example.org", proxies=proxies)
# Изменения в поведении
# Ключи в headersсловаре теперь являются собственными строками во всех версиях Python, то есть строками байтов на Python 2 и unicode на Python 3. Если ключи не являются собственными строками (unicode на Python 2 или байтовыми строками на Python 3), они будут преобразованы в собственные строки введите в кодировке UTF-8.
#
# Значения в headers словаре всегда должны быть строками. Такова позиция проекта еще до 1.0, но недавнее изменение (начиная с версии 2.11.0) требует более строгого соблюдения. Рекомендуется по возможности избегать передачи значений заголовков в формате Unicode.


import asyncio


class Storage:
    """Класс для хранения метрик в памяти процесса"""

    def __init__(self):
        # используем словарь для хранения метрик
        self._data = {}

    def put(self, key, value, timestamp):
        if key not in self._data:
            self._data[key] = {}

        self._data[key][timestamp] = value

    def get(self, key):
        data = self._data

        # вовзращаем нужную метрику если это не *
        if key != "*":
            data = {
                key: data.get(key, {})
            }

        # для простоты мы храним метрики в обычном словаре и сортируем значения
        # при каждом запросе, в реальном приложении следует выбрать другую
        # структуру данных
        result = {}
        for key, timestamp_data in data.items():
            result[key] = sorted(timestamp_data.items())

        return result


class ParseError(ValueError):
    pass


class Parser:
    """Класс для реализации протокола"""

    def encode(self, responses):
        """Преобразование ответа сервера в строку для передачи в сокет"""
        rows = []
        for response in responses:
            if not response:
                continue
            for key, values in response.items():
                for timestamp, value in values:
                    rows.append(f"{key} {value} {timestamp}")

        result = "ok\n"

        if rows:
            result += "\n".join(rows) + "\n"

        return result + "\n"

    def decode(self, data):
        """Разбор команды для дальнейшего выполнения. Возвращает список команд для выполнения"""
        parts = data.split("\n")
        commands = []
        for part in parts:
            if not part:
                continue

            try:
                method, params = part.strip().split(" ", 1)
                if method == "put":
                    key, value, timestamp = params.split()
                    commands.append(
                        (method, key, float(value), int(timestamp))
                    )
                elif method == "get":
                    key = params
                    commands.append(
                        (method, key)
                    )
                else:
                    raise ValueError("unknown method")
            except ValueError:
                raise ParseError("wrong command")

        return commands


class ExecutorError(Exception):
    pass


class Executor:
    """Класс Executor реализует метод run, который знает как выполнять команды сервера"""

    def __init__(self, storage):
        self.storage = storage

    def run(self, method, *params):
        if method == "put":
            return self.storage.put(*params)
        elif method == "get":
            return self.storage.get(*params)
        else:
            raise ExecutorError("Unsupported method")


class EchoServerClientProtocol(asyncio.Protocol):
    """Класс для реализции сервера при помощи asyncio"""

    # Обратите внимание на то, что storage является атрибутом класса
    # Объект self.storage для всех экземмпляров класса EchoServerClientProtocol
    # будет являться одним и тем же объектом для хранения метрик.
    storage = Storage()

    def __init__(self):
        super().__init__()

        self.parser = Parser()
        self.executor = Executor(self.storage)
        self._buffer = b''

    def process_data(self, data):
        """Обработка входной команды сервера"""

        # разбираем сообщения при помощи self.parser
        commands = self.parser.decode(data)

        # выполняем команды и запоминаем результаты выполнения
        responses = []
        for command in commands:
            resp = self.executor.run(*command)
            responses.append(resp)

        # преобразовываем команды в строку
        return self.parser.encode(responses)

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        """Метод data_received вызывается при получении данных в сокете"""
        self._buffer += data
        try:
            decoded_data = self._buffer.decode()
        except UnicodeDecodeError:
            return

        # ждем данных, если команда не завершена символом \n
        if not decoded_data.endswith('\n'):
            return

        self._buffer = b''

        try:
            # обрабатываем поступивший запрос
            resp = self.process_data(decoded_data)
        except (ParseError, ExecutorError) as err:
            # формируем ошибку, в случае ожидаемых исключений
            self.transport.write(f"error\n{err}\n\n".encode())
            return

        # формируем успешный ответ
        self.transport.write(resp.encode())


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        EchoServerClientProtocol,
        host, port
    )
    server = loop.run_until_complete(coro)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == "__main__":
    # запуск сервера для тестирования
    run_server('127.0.0.1', 8888)









