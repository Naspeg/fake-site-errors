import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Console Attacks")
print("Ваша консоль сайта")
from time import gmtime, strftime, sleep
from random import randint
sleep(10)
while True:
    attacks_count = randint(10, 1000)
    print(f"""{strftime("%Y-%m-%d %H:%M:%S", gmtime())} Сайт не взломали!
    Количество атак за период: {attacks_count}, успешно отраженно: {attacks_count}""")
    sleep(10)
