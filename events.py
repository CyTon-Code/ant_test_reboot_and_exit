import sys
import os
from constants import *  # все глобальные переменные


# выход из терминала:
def ant_exit():
    print("[Program Finished]")
    exit()


# перезапуск терминала:
def ant_restart():
    print("[Program Restarted]")
    os.execv(sys.executable, [sys.executable] + sys.argv)


# выход из терминала под предлогом ошибки:
def ant_error():
    print("error?")
    raise Exception


# очистка данных которые терминал выводил:
def ant_clear():

    pass  # TODO: реализация отсутствует... Доделать или убрать


# события:
def events(cmd: str) -> None:
    if cmd in ANT_RESTART:
        ant_restart()  # перезапуск
    elif cmd in ANT_EXIT:
        ant_exit()  # выход
    elif cmd in ANT_CLEAR:
        ant_clear()  # очистка
    else:
        ant_error()  # ошибка
