import os
import CRUD as CRUD

#untuk membuat program lebih rapi di python saat diperasikan
#dan pada variabel sistem operasi itu untuk mendeteksi sistem operasi yang digunakan
if __name__=="__main__":
    sistem_operation = os.name

    match sistem_operation:
            #mendeteksi untuk windows
            case 'nt': os.system('cls')
            #mendeteksi untuk mac dan linux
            case 'posix': os.system('clear')
        
    print('SELAMAT DATANG DI DATABASE PERPUSTAKAAN SEDERHANA')
    print('================================================= \n')

    #check apakah database sudah ada atau belum

    CRUD.init_console()
    while(True):
        match sistem_operation:
            #mendeteksi untuk windows
            case 'nt': os.system('cls')
            #mendeteksi untuk mac dan linux
            case 'posix': os.system('clear')

        print('SELAMAT DATANG DI DATABASE PERPUSTAKAAN SEDERHANA')
        print('================================================= \n')

        
        print('1. Read Data')
        print('2. Create Data')
        print('3. Update Data')
        print('4. Delete Data\n')

        userOption = input(f'Apa yang ingin kamu lakukan:')
        print('\n')

        match userOption:
            case '1': CRUD.read_console()   #membuat operasi di console
            case '2': print('Create Data')
            case '3': print('Update Data')
            case '4': print('Delete Data')

        print('===============================')

        isDone = input('Apakah anda ingin melanjutkan (y/n): ')

        if isDone == 'n' or isDone=='N':
            break





