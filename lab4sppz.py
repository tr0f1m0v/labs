import os
a = str()
if os.name == "nt":
    print("Тип ОС: Windows\n")
    menu = input("Выберите действие с ОС:\n1.Выйти из системы\n2.Завершить работу\n3.Перезагрузить систему\n")

    if menu == "1":
        f = input("Вы действительно хотите завершить сеанс?[y/n]:\n")
        if f == "y":
            os.system("shutdown /l")
        elif f == "n":
            print("Завершение сеанса отменено")
    if menu == "2":
        time = int(input("Введите время в минутах, через которое произвести действие(0 - без ожидания):"))
        time = time * 60
        os.system("shutdown /s /t " + str(time))
        a = input("Введите n, чтобы отменить завершение работы\n")
    if menu == "3":
        time = int(input("Введите время в минутах, через которое произвести действие(0 - без ожидания):"))
        time = time * 60
        os.system("shutdown /r /t " + str(time))
        a = input("Введите n, чтобы отменить перезагрузку системы\n")

    if a == "n":
        os.system('shutdown /a')
elif os.name == "posix":
    print("Тип ОС: Linux")
    menu = input("Выберите действие с ОС:\n1.Выйти из системы\n2.Завершить работу\n3.Перезагрузить систему\n")

    if menu == "1":
        f = input("Вы действительно хотите завершить сеанс?[y/n]:\n")
        if f == "y":
            os.system("killall -u " + os.getlogin())
        elif f == "n":
            print("Завершение сеанса отменено")
    if menu == "2":
        time = int(input("Введите время в минутах, через которое произвести действие(0 - без ожидания):"))
        os.system("shutdown -p +" + str(time))
        a = input("Введите n, чтобы отменить завершение работы\n")
    if menu == "3":
        time = int(input("Введите время в минутах, через которое произвести действие(0 - без ожидания):"))
        time = time
        os.system("shutdown -r +" + str(time))
        a = input("Введите n, чтобы отменить перезагрузку системы\n")
    if a == "n":
       os.system('shutdown -с')