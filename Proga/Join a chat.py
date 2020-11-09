#Создоно 08.11.2020 версия1
#Черепанов Александр Михаилович
#Join a chat

file=open('Create a chat.txt','r')
key=file.read()
file.close()
cod=input("Введите кодовое слово для присоеденениz к чяту: ")
s=0

if str(cod) == str(key):
    print("")#Переход к чяту. Пока так.
else:
    print("\nКодовое слово не правельное.")

input("\n\nВведите Enter. чтобы выйти.")
