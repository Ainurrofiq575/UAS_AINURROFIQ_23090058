import pandas as pd

data_mahasiswa = []

while True:
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    
    data_mahasiswa.append({'NIM': nim, 'Nama': nama})
    
    tambah_lagi = input("Ingin tambah data lagi? (iya/tidak): ")
    if tambah_lagi.lower() != 'iya':
        break

df = pd.DataFrame(data_mahasiswa)
print("\nData Mahasiswa:")
print(df)

print("Selesai")