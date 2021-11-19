import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Console Attacks")
print("Your console site")
from time import gmtime, strftime, sleep
from random import randint
sleep(10)
while True:
    attacks_count = randint(10, 1000)
    print(f"""{strftime("%Y-%m-%d %H:%M:%S", gmtime())} The site was not hacked!
    Number of attacks per period: {attacks_count}, successfully reflected: {attacks_count}""")
    sleep(10)
