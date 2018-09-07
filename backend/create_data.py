'''
Cria alguns dados
'''
import requests


datas = [
    {'name': 'Blackberry', 'price': 999},
    {'name': 'Bip', 'price': 120},
    {'name': 'Walkman', 'price': 350},
    {'name': 'Discman', 'price': 450},
    {'name': 'Mini System 3 em 1', 'price': 950},
    {'name': 'Vinil', 'price': 380},
]


for data in datas:
    requests.post('http://localhost:5000/product/add', data=data)
