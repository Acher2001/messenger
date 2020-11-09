#Создоно 08.11.2020 версия1
#Черепанов Александр Михаилович
#Create a chat

cod=input("Введите кодовое слово для создания чята: ")

file=open('Create a chat.txt','w')
file.write(str(cod))
file.close()

input("\n\nВведите Enter. чтобы выйти.")
