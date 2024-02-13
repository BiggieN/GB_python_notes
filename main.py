import json
import os

isFileNotes = checkfile();
isFileID = checkfile();

n = 100
while (n!=0):
    print("Добро пожаловать!")
    print("Возможные операции:")
    print("1. Создать заметку")
    print("2. Вывести заметки")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("0. Завершить работу")
    n = int(input("Выберите операцию: "))
    if (n==1):
        create_note()
    elif (n==2):
        show_note()
    elif (n==3):
        edit_note()
    elif (n==4):
        delete_note()
    else:
        print("Выберите правильный вариант!")

def checkfile(path):
    

def create_note():
    note = {}
