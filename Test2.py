## В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами. 
## За каждой партой может сидеть два учащихся. 
## Известно количество учащихся в каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.
a = int(input('Количество учеников в 1м классе: '))
b = int(input('Количество учеников во 2м классе: '))
c = int(input('Количество учеников в 3м классе: '))
print(f'Необходимое количество парт: {((a+1)//2) + ((b+1)//2) + ((c+1)//2)}')

