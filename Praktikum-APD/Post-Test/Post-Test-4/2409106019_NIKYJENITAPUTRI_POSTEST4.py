print("===BUAT AKUN===")
nama_panggilan = input("Masukan nama panggilan : ")
nim = int(input("Masukan 3 digit angka terakhir NIM (jika diawali 0 maka 0 tidak perlu dicantumkan) : "))

print("\nAkun berhasil dibuat!!")

print(f"\nUsername = {nama_panggilan}")
print(f"password = {nim}")

i = 0
while i < 3:
    print("\n===LOGIN===")
    username = input("Username : ")
    password = int(input("Password : "))

    if username == nama_panggilan and password == nim:
        print ("\nLogin berhasil!!!")
        
        while True:
            print("\n===KALKULATOR KEBUTUHAN KALORI HARIAN===")

            berat_badan = int(input("\nBerat badan (dalam gr):"))
            tinggi_badan = float(input("Tinggi badan (dalam km):"))
            umur = int(input("Umur (dalam tahun):"))

            print("\nPilih Jenis Kelamin")
            print("1. Pria")
            print("2. Wanita")
            jenis_kelamin = int(input("Pilihan (1 atau 2):"))
            
            if jenis_kelamin == 1:
                bmr = (10*(berat_badan/1000)) + (6.25*(tinggi_badan*100000)) - (5*umur) + 5
            elif jenis_kelamin == 2:
                bmr = (10*(berat_badan/1000)) + (6.25*(tinggi_badan*100000)) - (5*umur) - 161
            else:
                print("Pilihan tidak valid")
                break
            
            print("\nPilih Level Aktivitas Harian")
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
                break
        
            ulang = input("\nApakah Anda ingin menghitung lagi (iya/tidak) : ")
            if ulang != "iya":
                break
        break
    else:
        i += 1
        print("Login gagal, silahkan coba lagi")
    
if i == 3:
    print("Login gagal 3 kali. Program berhenti")

    