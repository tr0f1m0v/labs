def result():
    result = float(t1*40*amStr2/100+t2*40*amStr1)
    resultfin = round(result)
    print("T1=", t1, ", T2=", t2, ", Смуг на головній дорозі: ", amStr1, ", Смуг на побічній дорозі: ", amStr2)
    print("Lмашини = 3м, Lпершої дороги = ", int(amStr1)*4, "м, Lдругої дороги = ", int(amStr2)*4, "м")
    print("Машин, що перехрестя пропустить за один цикл: ", resultfin)


amStr1 = int(input("Введіть к-сть смуг на головній дорозі:\n"))
amStr2 = int(input("Введіть к-сть смуг на побічній дорозі:\n"))
t1 = int(input("Введіть T зеленого світла першого світлофора:\n"))
t2 = int(input("Введіть T зеленого світла другого світлофора:\n"))

print("     │ ", end = "")
for i in range(amStr1):
    print("↕", end = " ")
print("│     ")
print("─────┘", end = " ")
for i in range(amStr1):
    print(" ", end = " ")
print("└─────",)
for i in range(amStr2):
    print("    ↔", end = "")
    for i in range(amStr1):
        print("   ", end = "")
    print("↔     ", end = "")
    print("\n", end = "")
print("─────┐", end = " ")
for i in range(amStr1):
    print(" ", end = " ")
print("┌─────",)
print("     │ ", end = "")
for i in range(amStr1):
    print("↕", end = " ")
print("│     ")

result()
