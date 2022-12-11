import requests
import bs4
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = (int(input()))
deposit=[]
a = money*per_cent['ТКБ']
b = money*per_cent['СКБ']
c = money*per_cent['ВТБ']
d = money*per_cent['СБЕР']
deposit.append(a)
deposit.append(b)
deposit.append(c)
deposit.append(d)
print(list(deposit))
print("Максимальная сумма, которую вы можете заработать",max(deposit))



