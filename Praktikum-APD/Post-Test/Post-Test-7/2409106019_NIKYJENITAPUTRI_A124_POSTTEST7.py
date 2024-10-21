#Variabel Global
users ={}
data_hijab = {}
akun_admin = {'username' : 'admintokohijab', 'password' : 'admin12345', 'role' : 'admin'}

#Fungsi
def registrasi_user(username, password):
    if username in users:
        raise ValueError("Username telah terdaftar!!")
    users[username] = {
        "password" : password,
        "role" : "pengguna biasa"
    }
    print(f"Registrasi berhasil, {username} telah ditambahkan sebagai pengguna biasa.")

#Fungsi    
def login():
    username = input("Username : ") #Variabel Lokal
    password = input("Password : ") #Variabel Lokal
    if username in users and users[username]["password"] == password:
        return users[username]["role"]
    elif username == akun_admin['username'] and password == akun_admin['password']:
        return 'admin'
    else:
        raise ValueError("Login gagal!! Username atau password salah.")
    
 #Fungsi   
def tampilkan_produk():
    if not data_hijab:
        print("Tidak ada produk hijab yang tersedia.")
    else:
        for kode_produk, item in data_hijab.items():
            print(f"{kode_produk}. Nama : {item['nama']} \nWarna : {item['warna']} \nStok : {item['stok']} \nHarga : Rp{item['harga']}")

#Prosedur
def tambah_produk():
    try:
        nama = input("Nama : ") #Variabel Lokal
        warna = input("Warna : ") #Variabel Lokal
        stok = int(input("Stok : ")) #Variabel Lokal
        harga = int(input("Harga : ")) #Variabel Lokal
        kode_produk = str(len(data_hijab) + 1) #Variabel Lokal
        data_hijab[kode_produk] = {
            "nama" : nama,
            "warna" : warna,
            "stok" : stok,
            "harga" : harga
        }
        print(f"\nHijab {nama} berhasil ditambahkan.")
    except ValueError:
        print("Stok dan harga harus berupa angka!.")

#Fungsi
def ubah_produk():
    try:
        if not data_hijab:
            print("Tidak ada produk hijab yang tersedia.")
            return False
        tampilkan_produk()
        nomor_produk = input("Pilih nomor produk yang ingin diubah : ") #Variabel Lokal
        if nomor_produk in data_hijab:
            nama_baru = input("Nama baru : ") #Variabel Lokal
            warna_baru = input("Warna baru : ") #Variabel Lokal
            stok_baru = int(input("Stok baru : ")) #Variabel Lokal
            harga_baru = int(input("Harga baru : ")) #Variabel Lokal
            data_hijab[nomor_produk] = {
                "nama" : nama_baru,
                "warna" : warna_baru,
                "stok" : stok_baru,
                "harga" : harga_baru  
            }
            print(f"Hijab {nomor_produk} berhasil diubah.")
            return True
        else:
            print("Nomor produk tidak valid!!")
            return False
    except ValueError:
        print("Stok dan harga harus berupa angka.")
        return False

#Prosedur
def hapus_produk():
    try:
        if not data_hijab:
            print("Tidak ada produk hijab yang tersedia.")
            return
        tampilkan_produk()
        nomor_produk = input("Pilih nomor produk yang ingin dihapus : ") #Variabel Lokal
        if nomor_produk in data_hijab:
            deleted_item = data_hijab.pop(nomor_produk)
            print(f"Hijab {deleted_item['nama']} berhasil dihapus.")
        else:
            print("Nomor produk tidak valid!!")
    except Exception as e:
        print(f"Error : {e}")

#Fungsi Rekursif
def menu_pengguna_biasa():
    print("""
    ====================================
    |        MENU PENGGUNA BIASA       |
    ====================================
    |     1. TAMPILKAN PRODUK HIJAB    |  
    |     2. KELUAR                    |
    ====================================
    """)
    pilihan_pengguna_biasa = input("Pilih menu : ") #Variabel Lokal
    if pilihan_pengguna_biasa == '1':
        tampilkan_produk()
        menu_pengguna_biasa()
    elif pilihan_pengguna_biasa == '2':
        print("Terimakasih")
    else:
        print("Pilihan tidak valid!!")
        menu_pengguna_biasa()

#Fungsi Rekursif
def menu_admin():
    print("""
    ====================================
    |           MENU ADMIN             |
    ====================================
    |     1. TAMBAH PRODUK HIJAB       |
    |     2. TAMPILKAN PRODUK HIJAB    |  
    |     3. UBAH PRODUK HIJAB         |
    |     4. HAPUS PRODUK HIJAB        |    
    |     5. KELUAR                    |
    ====================================
    """)
    pilihan_admin = input("Pilih menu : ") #Variabel Lokal
    if pilihan_admin == '1':
        tambah_produk()
        menu_admin()
    elif pilihan_admin == '2':
        tampilkan_produk()
        menu_admin()
    elif pilihan_admin == '3':
        ubah_produk()
        menu_admin()
    elif pilihan_admin == '4':
        hapus_produk()
        menu_admin()
    elif pilihan_admin == '5':
        print("Terimakasih")
    else:
        print("Pilihan tidak valid!!")
        menu_admin()

 #Menu Utama       
while True:
    try:
        print("""
        ===================================
        |        SISTEM TOKO HIJAB        |
        ===================================
        |          1. REGISTRASI          |
        |          2. LOGIN               |    
        |          3. KELUAR              |
        ===================================
        """)
        pilihan = input("Pilih menu : ")

        if pilihan == '1':
            print("\n====REGISTRASI===")
            username = input("Username : ")
            password = input("Password : ")
            registrasi_user(username, password)
        elif pilihan == '2':
            print("\n===LOGIN===")
            role = login()
            if role == 'pengguna biasa':
                menu_pengguna_biasa()
            elif role == 'admin':
                menu_admin()
        elif pilihan == '3':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid!!")
    except Exception as e:
        print(f"Error : {e}")

