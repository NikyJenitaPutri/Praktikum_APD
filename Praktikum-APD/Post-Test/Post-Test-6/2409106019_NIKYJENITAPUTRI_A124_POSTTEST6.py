users = {}

data_hijab = {}

while True:
    print( 
    """
    =============================
    |     SISTEM TOKO HIJAB     |
    =============================
    |       1. REGISTRASI       |           
    |       2. LOGIN            |          
    |       3. KELUAR           |      
    =============================
    """
    )
    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        print("\n===Register===")
        username = input("Username : ")
        password = input("Password : ")
        role = input("Role (pilih admin/pengguna biasa) : ")

        if username in users:
            print("Username telah terdaftar!!. Silahkan coba lagi")
        else:
            users[username] = {
                "password" : password,
                "role" : role
            }
            print(f"Registrasi berhasil {username} telah ditambahkan sebagai {role}.")

    elif pilihan == '2':
        print("\n===Login===")
        username = input("Username : ")
        password = input("Password : ")

        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
            print(f"Login berhasil sebagai {role}")
        else:
            print("Login gagal!! Username atau password salah.")
            continue

        if role.lower() == 'pengguna biasa':
            while True:
                print( 
                """
                ==================================
                | MENU PENGGUNA BIASA TOKO HIJAB |
                ==================================          
                |   1. TAMPILKAN PRODUK HIJAB    |          
                |   2. KELUAR                    |  
                ==================================
                """
                )
                pilihan_pengguna_biasa = input("Pilih menu : ")

                if pilihan_pengguna_biasa == '1':
                    if not data_hijab:
                        print("Tidak ada produk hijab yang tersedia.")
                    else:
                        print("\n===Daftar Produk Hijab===")
                        for kode_produk, item in data_hijab.items():
                            print(f"{kode_produk}. Nama: {item['nama']} \nWarna: {item['warna']} \nStok: {item['stok']} \nHarga: Rp{item['harga']}")
                
                elif pilihan_pengguna_biasa == '2':
                    print("Terimakasih")
                    break

                else:
                    print("Pilihan tidak valid!")

        elif role.lower()== 'admin':
            while True:
                print( 
                """
                =================================
                |     MENU ADMIN TOKO HIJAB     |
                =================================
                |   1. TAMBAH PRODUK HIJAB      |           
                |   2. TAMPILKAN PRODUK HIJAB   |          
                |   3. UBAH PRODUK HIJAB        |     
                |   4. HAPUS PRODUK HIJAB       |      
                |   5. KELUAR                   |  
                =================================
                """
                )
                pilihan_admin = input("Pilih menu : ")

                if pilihan_admin == '1':
                    print("\n===Tambah Produk===")
                    nama = input("Nama : ")
                    warna = input("Warna : ")
                    stok = input("Stok : ")
                    harga = input("Harga : ")
                    if stok.isdigit() and harga.isdigit():
                        kode_produk = str(len(data_hijab) + 1)
                        data_hijab[kode_produk] = {
                            "nama" : nama,
                            "warna" : warna,
                            "stok" : int(stok),
                            "harga" : int(harga)
                        }
                        print(f"\nHijab {nama} berhasil ditambahkan.")
                    else:
                        print("Stok dan harga harus berupa angka.")

                elif pilihan_admin == '2':
                    if not data_hijab:
                        print("Tidak ada hijab yang tersedia.")
                    else:
                        print("===DAFTAR PRODUK HIJAB===")
                        for kode_produk, item in data_hijab.items():
                            print(f"{kode_produk}. Nama: {item['nama']} \nWarna: {item['warna']} \nStok: {item['stok']} \nHarga: Rp{item['harga']}")

                elif pilihan_admin == '3':
                    if not data_hijab:
                        print("Tidak ada hijab yang tersedia.")
                    else:
                        print("===DAFTAR PRODUK HIJAB===")
                        for kode_produk, item in data_hijab.items():
                            print(f"{kode_produk}. \nNama : {item['nama']} \nWarna : {item['warna']} \nStok : {item['stok']} \nHarga : Rp{item['harga']}")
                        
                        nomor_produk = input("Pilih nomor produk yang ingin dirubah : ")
                        if nomor_produk in data_hijab:
                            nama_baru = input("Nama baru :")
                            warna_baru = input("Warna baru : ")
                            stok_baru = input("Stok baru  : ")
                            harga_baru = input("Harga baru : ")
                            if stok_baru.isdigit() and harga_baru.isdigit():
                                data_hijab[nomor_produk] = {
                                    "nama" : nama_baru,
                                    "warna" : warna_baru,
                                    "stok" : int(stok_baru),
                                    "harga" : int(harga_baru)
                                }
                                print(f"Hijab {nomor_produk} berhasil dirubah.")
                            else:
                                print("Stok dan harga harus berupa angka.")

                        else:
                            print("Nomor produk tidak valid!!")

                elif pilihan_admin == '4':
                    if not data_hijab:
                        print("Tidak ada hijab yang tersedia.")
                    else:
                        print("===DAFTAR PRODUK HIJAB===")
                        for kode_produk, item in data_hijab.items():
                            print(f"{kode_produk}. \nNama : {item['nama']} \nWarna : {item['warna']} \nStok : {item['stok']} \nHarga : Rp{item['harga']}")

                        nomor_produk = input("Pilih nomor produk yang ingin dihapus : ")
                        if nomor_produk in data_hijab:
                            deleted_item = data_hijab.pop(nomor_produk)
                            print(f"Hijab {deleted_item['nama']} berhasil dihapus")
                        else:
                            print("Nomor produk tidak valid!!")

                elif pilihan_admin == '5':
                    print("Terimakasih")
                    break
                else:
                    print("Pilihan tidak valid!")
    
    elif pilihan == '3':
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid!")
