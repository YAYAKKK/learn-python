#MEMBUAT DATABASE BESERTA FORMAT DIDALAMNYA 

#pertama kita akan memakai fungsi yanga da di file operasi

from . import Operasi
#membuat format database yang dikmasukkan 
DB_NAME= 'data.txt'

#selanjutnya kita akan buat dahulu tempatenya agar nanti saat melakukan proses penghapusan dll hanya menjadi satu kali kerja

#untuk membuat template menggunakan dictionari dan nnti didalamnya ada primary key karena ini bentuknya database agar tidak ada yang terduplikat


TEMPLATE={
    'pk':'XXXXXX', #ini dibuat dengan 6 digit agar tidak sama
    'date_add':'yyyy-mm-dd-',
    'judul':255* ' ',   #ini menjelaskan bahwa panjang dari judul maksimal atau secara standart banyak digunakan adalah 255 tidak bisa dibuat takhingga
    'penulis':255*' ',
    'tahun':'yyyy'
}

def init_console():
    try:
        with open('data.txt', 'r') as file:
            print('database tersedia')
    except:
        print('database kosong, silahkan buat databasee baru')
        Operasi.create_first_data()
        