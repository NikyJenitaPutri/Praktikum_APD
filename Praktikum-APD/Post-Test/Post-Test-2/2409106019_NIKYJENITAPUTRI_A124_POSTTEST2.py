Nama_Lengkap = input("Nama Lengkap: ")
Nama_Panggilan = input("Nama Panggilan: ")
Prodi = input("Prodi: ")
NIM = int(input("NIM: "))
Universitas = (input("Universitas:"))
Umur = int(input("Umur: "))
Tempat_Lahir = input("Tempat Lahir: ")
Tanggal_Lahir = input("Tanggal Lahir (format: DD-MM-YYYY): ")
Tinggi_Badan = float(input("Tinggi Badan (dalam meter): "))

Tiga_Angka_Terakhir = NIM % 1000
Hasil_Modulus = Tiga_Angka_Terakhir % 6 

print(f"\nBiodata saya adalah sebagai berikut ini: ")
print(f'''Nama lengkap saya adalah {Nama_Lengkap}, biasa dipanggil {Nama_Panggilan}. 
Saya adalah salah satu mahasiswa program studi {Prodi} dengan NIM {NIM} di {Universitas}.
Sekarang saya berumur {Umur}. Saya lahir di {Tempat_Lahir} pada tanggal {Tanggal_Lahir}. Saya memiliki tinggi badan {Tinggi_Badan} meter. 
Tiga angka terakhir NIM saya adalah {Tiga_Angka_Terakhir}, dan jika dimoduluskan dengan 6 hasilnya adalah {Hasil_Modulus}.''')
