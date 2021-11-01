import csv
import sys
a='x'
while a =='x':
    print("Оберіть групу студентів: 1.Комп'ютерні науки 2.Інженерія програмного забезпечення 3.Системний аналіз")
    i=int(input())
    def studs():
        if i==1:
            return 'компнауки.txt'
        elif i==2:
            return 'інженерія.txt'
        elif i==3:
            return 'систаналіз.txt'
    studs=studs()
    b=int(input("Виберіть, що хочете зробити: 1.Прочитати файл 2. Перезаписати файл 3. Дозаписати у файл 4. Пошук у файлі 5. Сортування по середньому балу"))
    if b==1:
        f=open(studs, 'r', encoding = 'utf-8')
        reader=f.read()
        print(reader)
        f.close()
    elif b==2:
        f=open(studs, 'w', encoding='utf-8')
        f.write('Перезапис файлу')
        f.close()
    elif b==3:
        d=open(studs, 'a', encoding = 'utf-8')
        u=input("Введіть бал ЗНО")
        y=input("Введіть ПІБ")
        d.write('\n'+u+" "+y)
        d.close()
    elif b==4:
        search=input("Що хочете знайти?")
        f=open(studs, 'r', encoding = 'utf-8')
        reader=f.read()
        if search in reader:
            print("Знайдено")
        else:
            print("Не знайдено")
    elif b==5:
        f=open (studs, 'r', encoding = 'utf-8')
        for l in sorted(f):
            print(l, end = ' ')