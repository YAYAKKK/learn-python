from .  import Operasi


def read_console():
    dataCollect = Operasi.read()

    #membuat tanpilan lebih rapih

    index = 'No'
    judul = 'Judul'
    penulis = 'Penulis'
    tahun = 'Tahun'

    #Membuat tampilan Header

    print('\n'+'='*100)
    print(f"{index:.4} |{judul:.40}|{penulis:.40}|{tahun} ", end=' ')
    print("===============================================================")

    #menampilkan data datanya

    for index,data in enumerate (dataCollect):
        pisahKoma = data.split(',')
        pk = pisahKoma[0]
        date_add = pisahKoma[1]
        penulis = pisahKoma[2]
        judul= pisahKoma[3]
        tahun = pisahKoma[4]
        print(f"{index:.4} |{judul:.40}|{penulis:.40}|{tahun: .4}", end=' ')

    