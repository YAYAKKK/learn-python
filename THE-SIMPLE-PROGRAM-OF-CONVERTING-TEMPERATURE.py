# MEMBUAT PROGRAM KONVERSI SUHU SEDERHANA 
print('\n') 
print (f"THE SIMPLE PROGRAM FOR CONVERT TEMPERATURE")
print('==='*10)  


#FORMULA FOR CONVERTING TEMPERATURE FROM CELCIUS TO REAMUR 

def celcius_to_reamur(celcius):     
    return (4/5) * celcius

#FORMULA FOR CONVERTING TEMPERATURE FROM CELCIUS TO FAHRENHEIT 

def celcius_to_fahrenheit(celcius): 
    return (9/5) * celcius + 32

#FORMULA FOR CONVERTING TEMPERATURE FROM CELCIUS TO KELVIN

def celcius_to_kelvin (celcius):    
    return celcius + 273

#FORMULA FOR CONVERTING TEMPERATURE FROM FAHRENHEIT TO CELCIUS

def fahrenheit_to_celcius (fahrenheit): 
    return (fahrenheit - 32) * 5/9

#FORMULA FOR CONVERTING TEMPERATURE FROM FAHRENHEIT TO KELVIN

def fahrenheit_to_kelvin (fahrenheit):  
    return (fahrenheit - 32)* 5/9 +273

#RFORMULA FOR CONVERTING TEMPERATURE FROMFAHRENHEIT TO REAMUR

def fahrenheit_to_reamur (fahrenheit):  
    return (fahrenheit - 32) * 4/9

#FORMULA FOR CONVERTING TEMPERATURE FROM KELVIN TO CELCIUS

def kelvin_to_celcius (kelvin): 
    return (kelvin-273) * 4/5

#FORMULA FOR CONVERTING TEMPERATURE FROM KELVIN TO REAMUR

def kelvin_to_reamur (kelvin):  
    return (kelvin-273) * 4/5

#FORMULA FOR CONVERTING TEMPERATURE FROM KELVIN TO FAHRENHEIT
def kelvin_to_fahrenheit (kelvin):  
    return (kelvin-273)*9/5+32

#FORMULA FOR CONVERTING TEMPERATURE FROM REAMUR TO CELCIUS

def reamur_to_celcius (reamur): 
    return (5/4 * reamur)

#FORMULA FOR CONVERTING TEMPERATURE FROM REAMUR TO FAHRENHEIT

def reamur_to_fahrenheit (reamur):  
    return (9/4) *reamur + 32

#FORMULA FOR CONVERTING TEMPERATURE FROM REAMUR TO KELVIN

def reamur_to_kelvin (reamur):  
    return (5/4) * reamur + 273

#FUNCTION OF CONVERT SUHU
def convertSuhu():
    suhu = float(input(f"WHAT TEMPERATURE DO YOU WANT TO CONVERT?:"))
    print('\n')
    pilihan = input("INITIAL TEMPERATURE (C/F/K/R) : ")
    hasil = 0

    try:
        # CONDITION IF CHOOSE C
        if pilihan == 'C' or pilihan == 'c':
            pilihan2 = input(f"CONVERT TEMPERATURE TO (F/K/R): ")
            if pilihan2 == 'F' or pilihan2 == 'f':
                hasil = celcius_to_fahrenheit(suhu)
            elif pilihan2 == 'K' or pilihan2 == 'k':
                hasil = celcius_ke_kelvin(suhu)
            elif pilihan2 == 'R' or pilihan2 == 'r':
                hasil = celcius_ke_reamur(suhu)

        # CONDITION IF CHOOSE K
        elif pilihan == 'K' or pilihan == 'k':
            pilihan2 = input(f"CONVERT TEMPERATURE TO (F/C/R): ")
            if pilihan2 == 'C' or pilihan2 == 'c':
                hasil = kelvin_to_celcius(suhu)
            elif pilihan2 == 'F' or pilihan2 == 'f':
                hasil = kelvin_to_fahrenheit(suhu)
            elif pilihan2 == 'R' or pilihan2 == 'r':
                hasil = kelvin_to_reamur(suhu)

        # CONDITION IF CHOOSE R
        elif pilihan == 'R' or pilihan == 'r':
            pilihan2 = input(f"CONVERT TEMPERATURE TO (F/K/C): ")
            if pilihan2 == 'F' or pilihan2 == 'f':
                hasil = reamur_to_fahrenheit(suhu)
            elif pilihan2 == 'K' or pilihan2 == 'k':
                hasil = reamur_to_kelvin(suhu)
            elif pilihan2 == 'C' or pilihan2 == 'c':
                hasil = reamur_to_celcius(suhu)

        # CONDITION IF CHOOSE F
        elif pilihan == 'F' or pilihan == 'f':
            pilihan2 = input(f"CONVERT TEMPERATURE TO (K/C/R): ")
            if pilihan2 == 'C' or pilihan2 == 'c':
                hasil = fahrenheit_to_celcius(suhu)
            elif pilihan2 == 'K' or pilihan2 == 'k':
                hasil = fahrenheit_to_kelvin(suhu)
            elif pilihan2 == 'R' or pilihan2 == 'r':
                hasil = fahrenheit_to_reamur(suhu)

        # If none of the above conditions are met, raise an exception
        else:
            raise Exception("INITIAL TEMPERATURE YOU CHOSE IS NOT VALID")
            
    except Exception as e:
        print('\n')
        print(f"ERROR: {e}")
        print(f"PLEASE ENTER A VALID INITIAL TEMPERATURE (C/F/K/R). \n")
    else:
        # FINAL FROM THIS PROGRAM LIKE CONCLUSION
        print('\n')
        print(f"TEMPERATURE  {suhu}({pilihan})", end=", ")
        print(f"RESULT OF CONVERT: {hasil}({pilihan2}) \n")
        print(f"THANKS FOR USING THIS PROGRAM \n")
        print(f"HAVE A GREAT DAY \n")

convertSuhu()