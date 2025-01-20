import os
import getpass

path = "/Users/" + getpass.getuser() + "/TurboMac/"

os.chdir(path)

os.system("clear")
os.system("chmod +x load.sh")
os.system("./load.sh")

done = input("Операция прошла успешно! Нажмите Enter для закрытия окна ")