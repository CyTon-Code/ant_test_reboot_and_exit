from events import *  # события


# приветствие
def upd_greeting(name, src):
    """
        :param src: папка в которой сейчас находится ANT
        :param name: имя пользователя - пока что без аккаунтов
        :return: greeting
    """

    return "[" + name + " " + src + "]$ "


# узнать текущую папку:
def name_folder(link: str) -> str:
    """
        :param link: адрес исполняемого файла, а точнее ссылка на ant
        :return: имя папки в которой находится файл.
    """

    return link.split(r"/")[-2]  # текущее расположение в терминале


# Запуск модуля:
def start(cmd: str) -> None:
    # нам нужно узнать имя скрипта и запустить его как скрипт на python

    cmd = cmd.split()  # получаем массив слов
    cmd[0] = r"python lib/" + cmd[0] + ".py"  # получаем первое слово и меняем
    # его на запуск используя его имя
    cmd = ' '.join(cmd)  # возвращаем весь массив слов обратно в командую
    # строку
    os.system(cmd)  # вызываем в терминале
