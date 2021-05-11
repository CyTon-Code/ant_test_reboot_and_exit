#!/usr/bin/env python
# -*- coding:utf-8 -*-

# default start:
console = True
scripts = True  # tmp! default = False



exit()
"""
# import sys


from configuration import *
from plugin import *

while True:
    # TODO: If the name or folder has changed since the end of the previous
    #  iteration, update our welcome variable.

    # приветствую вас, а также прошу ввести вашу команду и ее аргументы:
    cmd = input(upd_greeting(ANT_NAME, ANT_FOLDER))

    # если ваша команда есть в списке событий:
    if cmd in ANT_EVENTS:

        # TODO: сюда можно попасть только если не дать команде параметров, а их
        #  нужно было просто игнорировать. в противном случае:
        #  `exit 1` - будет читаться как модуль, а не как событие.
        #  в то время как `exit` - будет читаться как событие.
        #  это нужно позже исправить.

        break  # выйти из цикла, чтобы вызвать нужное событие
    else:  # иначе это модуль:
        start(cmd)
# print(sys.argv)
events(cmd)  # отвечает за: выход, перезапуск, ошибку и прочие события
"""
# особые события: или же вопросы и функции
"""
    переместить файл, пытаться переместить файл, и прочие...
    вопросы, а также функции
"""
