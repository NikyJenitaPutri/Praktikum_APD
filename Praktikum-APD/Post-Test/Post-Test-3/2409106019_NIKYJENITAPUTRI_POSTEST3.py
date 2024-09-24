print("===Kalkulator Kebutuhan  Kalori Harian===")

berat_badan = int(input("Berat badan (dalam gr):"))
tinggi_badan = float(input("Tinggi badan (dalam km):"))
umur = int(input("Umur (dalam tahun):"))

print("Pilih Jenis Kelamin")
print("1. Pria")
print("2. Wanita")
jenis_kelamin = int(input("Pilihan (1 atau 2):"))

if jenis_kelamin == 1:
    bmr = (10*(berat_badan/1000)) + (6.25*(tinggi_badan*100000)) - (5*umur) + 5
elif jenis_kelamin == 2:
    bmr = (10*(berat_badan/1000)) + (6.25*(tinggi_badan*100000)) - (5*umur) + 161
else:
    print("Pilihan tidak valid")
    bmr = None

if bmr is not None:     
    print("Pilih Level Aktivitas Harian")
    print("1. Aktivitas minimal (jarang bergerak)")
    print("2. Aktivitas sedang (olahraga 1-3 kali seminggu)")
    print("3. Aktivitas tinggi (olahraga 4-7 kali seminggu)")
    level_aktivitas_harian = int(input("Pilihan (1/2/3):"))
    
    if level_aktivitas_harian == 1:
        tdee = bmr * 1.25
        print(f"Jadi, Kebutuhan Kalori Harian adalah {tdee:.2f} kalori")
    elif level_aktivitas_harian== 2:
        tdee = bmr * 1.36
        print(f"Jadi, Kebutuhan Kalori Harian adalah {tdee:.2f} kalori ")
    elif level_aktivitas_harian == 3:
        tdee = bmr * 1.72
        print(f"Jadi, Kebutuhan Kalori Harian adalah {tdee:.2f} kalori ")
    else:
        print("Pilihan tidak valid")