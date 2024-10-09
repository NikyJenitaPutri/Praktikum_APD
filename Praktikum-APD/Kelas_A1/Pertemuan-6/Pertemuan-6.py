# daftar_buku = {
#     #key        #value
#     "Buku1" : "Harry Potter",
#     "Buku2" : "Percy Jackson",
#     "Buku3" : "Twillight"
# }

# print(daftar_buku["Buku1"])
# print(daftar_buku) 


# # memiliki key yang sama
# daftar_buku = {
#     #key        #value
#     "Buku1" : "Harry Potter",
#     "Buku1" : "Percy Jackson",
#     "Buku3" : "Twillight"
# }

# print(daftar_buku["Buku1"])


# games = dict(Sekiro = "Action", Pokemon = "Adventure", Valorant = "FPS")
# print(games)


# Biodata = {
# "Nama" : "Aldy Ramadhan Syahputra", #string
# "NIM" : 2109106079, #integer
# "KRS" : ["Program Web", "Struktur Data", "Basis Data"], #list
# "Mahasiswa_Aktif" :True, #bolean
# "Social Media" : { #dictionary
#     "Instagram" : "@aldyrmdhns_",
#     "Discord" : "\'Izanami#6848"
#     }
# }

# #Mengakses Item dengan kurung siku
# print(Biodata["KRS"])
# print(Biodata["KRS"][1])

# #Mengakses Item dengan get()
# print(Biodata.get("Nama"))

#Mengakses Item yang tidak ada
# print(Biodata.get("Alamat"))
# print(Biodata.get("Alamat"), "kosong bang")


# #perulangan
# Biodata = {
# "Nama" : "Aldy Ramadhan Syahputra", #string
# "NIM" : 2109106079, #integer
# "KRS" : ["Program Web", "Struktur Data", "Basis Data"], #list
# "Mahasiswa_Aktif" :True, #bolean
# "Social Media" : { #dictionary
#     "Instagram" : "@aldyrmdhns_",
#     "Discord" : "\'Izanami#6848"
#     }
# }

# for i in Biodata:
#     print(i)

# for i,j in Biodata.items():
#     print(f"Key = {i} dan Value = {j}")


# #menambah item 
# Film = {
#     "Avenger Endgame" : "Action",
#     "Sherlock Holmes" : "Mystery",
#     "The Conjuring" : "Horror"
# }

# print(Film)

# #menggunakan kurung siku
# Film["Zombieland"] = "Comedy"
# print(Film)

# #menggunakan update()
# Film.update({"Hour" : "Thriller"})
# print(Film)


# #menghapus item
# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# print(Film)

# #menggunakan del
# del Film["The Conjuring"]
# print(Film)

# #menggunakan pop
# hapus = Film.pop(Film["The Conjuring"])
# print(Film)
# print(f"Key yang dihapus = {hapus}")

# #menggunakan clear
# Film.clear()
# print(Film)


# data = {
# "Nama" : "Aldy",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# print("Jumlah Data = ", len(data))



# Biodata = {
# "Nama" : "Aldy Ramadhan Syahputra", #string
# "NIM" : 2109106079, #integer
# "KRS" : ["Program Web", "Struktur Data", "Basis Data"], #list
# "Mahasiswa_Aktif" :True, #bolean
# "Social Media" : { #dictionary
#     "Instagram" : "@aldyrmdhns_",
#     "Discord" : "\'Izanami#6848"
#     }
# }

# pinjam = Biodata.copy()
# print("Dictionary yang Telah Disalin : ", pinjam)


# key = "apel", "jeruk", "mangga"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)



# Film = {
#     "Avenger Endgame" : "Action",
#     "Sherlock Holmes" : "Mystery",
#     "The Conjuring" : "Horror"
# }

# #menggunakan keys
# for i in Film.keys():
#     print(i)
#     print("")

# #menggunakan value
# for i in Film.values():
#     print(i)


# Musik = {
#     "The Chainsmoker" : ["All we Know", "The Paris"],
#     "Alan Walker" : ["Alone", "Lily"],
#     "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j:
#         print(song)
#     print("")


# mahasiswa = {
#     101 : {"Nama" : "Aldy", "Umur" : 19},
#     111 : {"Nama" : "Abdul", "Umur" : 18}
# }

# for i, j in mahasiswa.items():
#     print(f"ID Mahasiswa : {i}")
#     for i_a, j_a in j.items():
#         print (i_a, " : ", j_a)

# print(f"sebelum : {mahasiswa}")
# mahasiswa[101]["Angkatan"] = 2023
# print(f"sesudah : {mahasiswa}")

# print(f"sebelum : {mahasiswa}")
# del mahasiswa[111]["Umur"]
# print(f"sesudah : {mahasiswa}")


# mahasiswa = { 
#     "Nama": "Niky Jenita Putri",
#     "Nim" : "2409106019",
#     "Kelas" : "A2024",
#     "Prodi": "Informatika",
#     "Fakultas": "Teknik"
# }
# print(mahasiswa)
# print(f"Niky ada di kelas {mahasiswa.get('Kelas')}")

# mahasiswa.update({"Fakultas" : "Fakultas Teknik"})
# print(mahasiswa)
