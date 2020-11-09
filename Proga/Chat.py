#Создоно 9.11.2020 версия1
#Черепанов Александр Михаилович
#Chat
import hashlib
import os

txt=""

while txt != "End...":
    
    txt=str(input())

    if txt != "End...":
        chat=open('cat.txt','a')
        chat.write("""
        
        """+txt)
    elif txt == "End...":
        chat=open('cat.txt','w')
        chat.write(txt)
chat.close()

input("\n\nВведите Enter. чтобы выйти.")
