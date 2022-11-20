#latihan 1
#Nama:Muammar
#Nim:21/2006/0057/TSD/14
#Prodi: S2-MTI"

"""
1. Buatlah fungsi atau sub program untuk mengkonversi nilai angka menjadi nilai huruf
mengembangkan kasus praktik no 5. petunjuk def ubahNilai(nilai):
"""

def ubahNilai(nilai):
  import os 
  os.system('cls') #bersihkan layar
  lagi="Y"
  while lagi =="Y" or lagi=="y":
    os.system('cls') #bersihkan layar
    if nilai >=0 and nilai <=19:
      print("Nilai Anda E")
                
    elif nilai >=20 and nilai <=44:
      print("Nilai Anda D")
            
    elif nilai >=45 and nilai <=64:
      print("Nilai Anda C")
                
    elif nilai >=65 and nilai <=79:
      print("Nilai Anda B")
            
    elif nilai >=80 and nilai <=100:
      print("Nilai Anda A")
            
    else:
      print("Maaf Anda Salah Input")
    print("")    
    lagi=input("Mencoba lagi [Y/T]:")
    
        
  print(">>>>> Terima Kasih Anda Telah Menggunakan program ini <<<<<")                  
            
ubahNilai(int(input("Masukan Nilai Angka [0..100]:")))
   