#Создоно 16.11.2020 версия1
#Черепанов Александр Михаилович
#Text input
import hashlib
import os

x=input("Введите основное слово: ")#Изеочяльный текст
y=input("Введите кодовое слово: ")#Кодовое слово
z=""#Шифровоное слово
xmas=[]
ymas=[]
i=0
for i,c in enumerate(x):
    if c in 'аА':
        xmas.append('1')
    elif c in 'бБ':
        xmas.append('2')
    elif c in 'вВ':
        xmas.append('3')
    elif c in 'гГ':
        xmas.append('4')
    elif c in 'дД':
        xmas.append('5')
    elif c in 'еЕ':
        xmas.append('6')
    elif c in 'ёЁ':
        xmas.append('7')
    elif c in 'жЖ':
        xmas.append('8')
    elif c in 'зЗ':
        xmas.append('9')
    elif c in 'иИ':
        xmas.append('10')
    elif c in 'йЙ':
        xmas.append('11')
    elif c in 'кК':
        xmas.append('12')
    elif c in 'лЛ':
        xmas.append('13')
    elif c in 'мМ':
        xmas.append('14')
    elif c in 'нН':
        xmas.append('15')
    elif c in 'оО':
        xmas.append('16')
    elif c in 'пП':
        xmas.append('17')
    elif c in 'рР':
        xmas.append('18')
    elif c in 'сС':
        xmas.append('19')
    elif c in 'тТ':
        xmas.append('20')
    elif c in 'уУ':
        xmas.append('21')
    elif c in 'фФ':
        xmas.append('22')
    elif c in 'хХ':
        xmas.append('23')
    elif c in 'цЦ':
        xmas.append('24')
    elif c in 'чЧ':
        xmas.append('25')
    elif c in 'шШ':
        xmas.append('26')
    elif c in 'щЩ':
        xmas.append('27')
    elif c in 'ъЪ':
        xmas.append('28')
    elif c in 'ыЫ':
        xmas.append('29')
    elif c in 'ьЬ':
        xmas.append('30')
    elif c in 'эЭ':
        xmas.append('31')
    elif c in 'юЮ':
        xmas.append('32')
    elif c in 'яЯ':
        xmas.append('33')
    elif c in ' ':
        xmas.append('34')
    elif c in '.':
        xmas.append('35')
    elif c in ',':
        xmas.append('36')
    else:
        xmas.append('37')

for i,c in enumerate(y):
    if c in 'аА':
        ymas.append('1')
    elif c in 'бБ':
        ymas.append('2')
    elif c in 'вВ':
        ymas.append('3')
    elif c in 'гГ':
        ymas.append('4')
    elif c in 'дД':
        ymas.append('5')
    elif c in 'еЕ':
        ymas.append('6')
    elif c in 'ёЁ':
        ymas.append('7')
    elif c in 'жЖ':
        ymas.append('8')
    elif c in 'зЗ':
        ymas.append('9')
    elif c in 'иИ':
        ymas.append('10')
    elif c in 'йЙ':
        ymas.append('11')
    elif c in 'кК':
        ymas.append('12')
    elif c in 'лЛ':
        ymas.append('13')
    elif c in 'мМ':
        ymas.append('14')
    elif c in 'нН':
        ymas.append('15')
    elif c in 'оО':
        ymas.append('16')
    elif c in 'пП':
        ymas.append('17')
    elif c in 'рР':
        ymas.append('18')
    elif c in 'сС':
        ymas.append('19')
    elif c in 'тТ':
        ymas.append('20')
    elif c in 'уУ':
        ymas.append('21')
    elif c in 'фФ':
        ymas.append('22')
    elif c in 'хХ':
        ymas.append('23')
    elif c in 'цЦ':
        ymas.append('24')
    elif c in 'чЧ':
        ymas.append('25')
    elif c in 'шШ':
        ymas.append('26')
    elif c in 'щЩ':
        ymas.append('27')
    elif c in 'ъЪ':
        ymas.append('28')
    elif c in 'ыЫ':
        ymas.append('29')
    elif c in 'ьЬ':
        ymas.append('30')
    elif c in 'эЭ':
        ymas.append('31')
    elif c in 'юЮ':
        ymas.append('32')
    elif c in 'яЯ':
        ymas.append('33')
print(xmas)
print(len(xmas))
print(ymas)
print(len(ymas))



while True:
    if len(xmas)>len(ymas):
        ymas+=ymas
    elif len(ymas)>len(xmas):
        xmas.append('34')
    else:
        print(xmas)
        print(ymas)
        break

t=0
sh=[]
i=0
for i,c in enumerate(xmas):
     if not int(xmas[i]) in (34,35,36,37):
        if int(xmas[i])+int(ymas[i]) > 33:
            t=(int(xmas[i])+int(ymas[i]))-34
            sh+=str(t)
            t=0
        elif int(xmas[i])+int(ymas[i]) < 33:
            t=(int(xmas[i])+int(ymas[i]))-1
            sh+=str(t)
            t=0
     elif int(xmas[i]) in (34,35,36,37):
        sh+=xmas[i]
print(sh)



s=os.urandom(32)
file_salt=open('salt.txt','w')
file_salt.write(str(s))
file_salt.close()



f=open('salt.txt','r')
salt=f.read()
f.close()


hash1=''
for i,c in enumerate(sh):
    if c in '1':
        hash1+='а'
    elif c in '2':
        hash1+='б'
    elif c in '3':
        hash1+='в'
    elif c in '4':
        hash1+='г'
    elif c in '5':
        hash1+='д'
    elif c in '6':
        hash1+='е'
    elif c in '7':
        hash1+='ё'
    elif c in '8':
        hash1+='ж'
    elif c in '9':
        hash1+='з'
    elif c in '10':
        hash1+='и'
    elif c in '11':
        hash1+='й'
    elif c in '12':
        hash1+='к'
    elif c in '13':
        hash1+='л'
    elif c in '14':
        hash1+='м'
    elif c in '15':
        hash1+='н'
    elif c in '16':
        hash1+='о'
    elif c in '17':
        hash1+='п'
    elif c in '18':
        hash1+='р'
    elif c in '19':
        hash1+='с'
    elif c in '20':
        hash1+='т'
    elif c in '21':
        hash1+='у'
    elif c in '22':
        hash1+='ф'
    elif c in '23':
        hash1+='х'
    elif c in '24':
        hash1+='ц'
    elif c in '25':
        hash1+='ч'
    elif c in '26':
        hash1+='ш'
    elif c in '27':
        hash1+='щ'
    elif c in '28':
        hash1+='ъ'
    elif c in '29':
        hash1+='ы'
    elif c in '30':
        hash1+='ь'
    elif c in '31':
        hash1+='э'
    elif c in '32':
        hash1+='ю'
    elif c in '33':
        hash1+='я'
    elif c in '34':
        hash1+=' '
    elif c in '35':
        hash1+='.'
    elif c in '36':
        hash1+=','
    elif c in '37':
        hash1+='???'

hash2=''
for i,c in enumerate(hash1):
    hash2+=hash1[i]
print(hash2)



txt_hash=hashlib.pbkdf2_hmac('sha256', hash2.encode('utf-8'), salt.encode('utf-8'), 100000)
file=open('shifr.txt','w')
file.write(str(txt_hash))
file.close()
print(txt_hash)



input("\n\nВведите Enter. чтобы выйти.")
