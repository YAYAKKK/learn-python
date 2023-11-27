#menghubungkan dengan database dan memakainya karena ini sebagai operasi dari semua database

from . import Database
from .Util import random_string
import time
from . import view

def create_first_data():
    #karena di database kita harus memiliki penulis judul dll maka kita buat disini

    data = Database.TEMPLATE.copy()     #copy digunakan agar bisa di otak atik

    penulis = input('Penulis: ')
    judul = input('Judul: ')
    tahun = input('Tahun: ')

    #selanjutnya kita akan kaitkan menjadi data ke database dengan template yang sudah ada di database


    #membuat pk(primary key)
    data['pk']= random_string(6)
    data['date_add']= time.strftime('%Y-%m-%d-%H-%M-%S%Z', time.gmtime()) #unutk membuat data waktu dari komputer kita
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['tahun'] = tahun

    data_str = f'{data['pk']}, {data['date_add']}, { data['penulis'] }, {data['judul'] }, {data['tahun']} \n'

    print(data_str)
    try:
        with open(Database.DB_NAME, 'w', encoding='utf-8') as file:
            file.write(data_str)
        print (data_str)
    except:
        print('capek anjing dari tadi sore ini')
        

def read():
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            print(content)
            return content
    except:
        print('cape belajar')
        return False