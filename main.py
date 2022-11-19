from Zodiac import Zodiac


def printMenu():
    print("Что вы хотите сделать ?\n"
          "1 - Вывести данные\n"
          "2 - Дополнить список\n"
          "3 - Сортировать по дате\n"
          "4 - Посик по фамилии\n"
          "5 - Запись списка в файл под тем же или новым именем\n"
          "6 - Завершить работу")


def saveNewArrayProduct(arrayZodiac):
    file = input("Введите имя файла, в который сохранить информацию ? ")
    f = open(file, 'w')
    for i in range(len(arrayZodiac)):
        f.writelines(arrayZodiac[i].getName() + " " +
                     arrayZodiac[i].getSurname() + " " +
                     arrayZodiac[i].getZodiac() + " " +
                     str(arrayZodiac[i].getBirthday()) + "\n")


def printZodiac(a):
    print("Данные из файла : ")
    print(len(a))
    for i in range(len(a)):
        print("Фамилия:", arrayZodiac[i].getName(),
              "Имя:", arrayZodiac[i].getSurname(),
              "Знак зодиака:", arrayZodiac[i].getZodiac(),
              "День рождения:", arrayZodiac[i].getBirthday())


def addZodiac(b):
    w = len(b)
    newZodiac = Zodiac("", "", "", 0, 0, 0)
    b.append(newZodiac)
    b[w].setName(input("Введите новое имя "))
    b[w].setSurname(input("Введите новую фамилию "))
    b[w].setZodiac(input("Введите новый знак зодиака "))
    b[w].setBirthday(input("Введите новый день рождения "), input("Введите новый месяц рождения "),
                     input("Введите новый год рождения "))


def search(name, arrayZodiac):
    for i in range(len(arrayZodiac)):
        if (arrayZodiac[i].getSurname() == name):
            print("Имя: ", arrayZodiac[i].getName(),
                  "Фамилия: ", arrayZodiac[i].getSurname(),
                  "Знак зодиака: ", arrayZodiac[i].getZodiac(),
                  "День рождения: ", arrayZodiac[i].getBirthday())


def sortBirthady(arrayZodiac):
    arrayZodiac.sort(key=lambda x: (x.birthday[2], x.birthday[1], x.birthday[0]), reverse=False)
    printZodiac(arrayZodiac)


Fin = open("Zodiac.txt") #чтение файла в папке с приложением
s = Fin.readlines()
count = len(s)
a = []
arrayZodiac = []

for i in range(count):
    a.append([""] * 5)

for i in range(len(s)):
    a[i] = s[i].split(" ")
for i in range(0, count):
    arrayZodiac.append(Zodiac(a[i][0], a[i][1], a[i][2], a[i][3], a[i][4], a[i][5]))

while (True):
    printMenu()
    inputUser = int(input())
    if inputUser == 1:
        printZodiac(arrayZodiac)
    elif inputUser == 2:
        addZodiac(arrayZodiac)
    elif inputUser == 3:
        sortBirthady(arrayZodiac)
    elif inputUser == 4:
        search(input("Введите имя товара "), arrayZodiac)
    elif inputUser == 5:
        saveNewArrayProduct(arrayZodiac)
    elif inputUser == 6:
        break

Fin.close()
