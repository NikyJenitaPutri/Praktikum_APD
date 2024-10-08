users = [ ]

data_hijab = [ ]

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
        admin_pengguna = input("Admin/Pengguna biasa : ")

        username_exists = False
        for user in users:
            if user["username"] == username:
                print("Username sudah terdaftar!!. Silahkan coba lagi")
                username_exists = True
                break
        
        if not username_exists:
            users.append({"username": username, "password": password, "role": admin_pengguna})
            print(f"Registrasi berhasil!! {username} telah ditambahkan sebagai {admin_pengguna}." )

    elif pilihan == '2':
        print("\n===Login===")
        username = input("Username : ")
        password = input("Password : ")

        user_found = False
        for user in users:
            if user["username"] == username and user["password"] == password:
                print(f"Login berhasil sebagai {user['role']}")
                user_found = True
                role = user["role"]
                break

        if not user_found:
            print("Login gagal!! Username atau password salah.")
            continue

        if role == 'pengguna biasa':
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
                pilihan_pengguna = input("Pilih menu : ")

                if pilihan_pengguna == '1':
                    if len(data_hijab) == 0:
                        print("Tidak ada produk hijab yang tersedia.")
                    else:
                        print("\n===Daftar Produk Hijab===")
                        for idx, item in enumerate(data_hijab):
                            print(f"{idx + 1}. \nNama: {item[0]} \nWarna: {item[1]} \nStok: {item[2]} \nHarga: Rp{item[3]}")
                
                elif pilihan_pengguna == '2':
                    print("Terimakasih")
                    break
                else:
                    print("Pilihan tidak valid!")

        elif role == 'admin':
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
                        data_hijab.append([nama, warna, int(stok), int(harga)])
                        print(f"\nHijab {nama} berhasil ditambahkan.")
                    else:
                        print("Stok dan harga harus berupa angka.")

                elif pilihan_admin == '2':
                    if len(data_hijab) == 0:
                        print("Tidak ada hijab yang tersedia.")
                    else:
                        print("===DAFTAR PRODUK HIJAB===")
                        for idx, item in enumerate(data_hijab):
                            print(f"{idx + 1}. \nNama: {item[0]} \nWarna: {item[1]} \nStok: {item[2]} \nHarga: Rp{item[3]}")

                elif pilihan_admin == '3':
                    if len(data_hijab) == 0:
                        print("Tidak ada hijab yang tersedia.")
                    else:
                        print("===DAFTAR PRODUK HIJAB===")
                        for idx, item in enumerate(data_hijab):
                            print(f"{idx + 1}. \nNama: {item[0]} \nWarna: {item[1]} \nStok: {item[2]} \nHarga: Rp{item[3]}")
                        
                        index = input("Pilih nomor produk yang ingin dirubah : ")
                        if index.isdigit():
                            index = int(index) - 1
                            if 0 <= index < len(data_hijab):
                                nama = input("Nama baru : ")
                                warna = input("Warna baru : ")
                                stok = input("Stok baru  : ")
                                harga = input("Harga baru : ")
                                if stok.isdigit() and harga.isdigit():
                                    data_hijab[index] = [nama, warna, int(stok), int(harga)]
                                    print(f"Hijab {index + 1} berhasil dirubah.")
                                else:
                                    print("Stok dan harga harus berupa angka.")

                            else:
                                print("Nomor produk tidak valid!!")
                        else:
                            print("Input harus berupa angka!!")

                elif pilihan_admin == '4':
                    if len(data_hijab) == 0:
                        print("Tidak ada hijab yang tersedia.")
                    else:
                        print("===DAFTAR PRODUK HIJAB===")
                        for idx, item in enumerate(data_hijab):
                            print(f"{idx + 1}. \nNama: {item[0]} \nWarna: {item[1]} \nStok: {item[2]} \nHarga: Rp{item[3]}")

                        index = input("Pilih nomor produk yang ingin dihapus : ")
                        if index.isdigit():
                            index = int(index) - 1
                            if 0 <= index < len(data_hijab):
                                deleted_item = data_hijab.pop(index)
                                print(f"Hijab {deleted_item[0]} berhasil dihapus")
                            else:
                                print("Nomor produk tidak valid!!")
                        else:
                            print("Input harus berupa angka!!")

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