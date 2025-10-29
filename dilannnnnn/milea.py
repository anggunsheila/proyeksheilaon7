#integer
#is a whole number.positef or negatif,wthout decinals, of unlimited lenght
#adalah semua angka,positif atau negatif,tanpa desimal,tanpa batas panjang
x = 20
y = 17

print("hasil penjumlahan adalh :",x+y)

tinggi= 15
alas = 8

print(tinggi)
print(alas)

#float :
#is a number,positif or negatif, containing one or more decimals
#adalah sebuah angka,positif atau negatif,yang mengandung satu atau lebih denial 

pi = 3.14
r=30

print(pi)
print(r)
#tipe data number bisa dikenalkan,operator aritmatika()ariabel di integer
#menghitung luas segitiga menggnakan v
luas_segitiga =(alas*tinggi)/2
print("luas_segitiga adalah :",luas_segitiga)
#menghitung luas lingkaran menggunakan variabel di float
luas_lingkaran = pi*(r*r)
print("luas lingkaran adalah :",luas_lingkaran)
#string
#is surrounded by either single quotation marks,or dounle quotation marks.
#data yang dapat diapit oleh tanda kutip  (single(kutip 1)atau double (kutip 2))
nama_depan = "raihan"
nama_belakang = "anggun"
print("nama depan saya adalah :",nama_depan)
print("nama belakang saya adalah :",nama_belakang)
#huruf besar
print("huruf besar :",nama_depan.upper(),nama_belakang.upper())
#huruf kecil
print("huruf kecil :",nama_depan.upper(),nama_belakang.upper() )
#list, dictorionary,tuple,set
#prosudal,oop,ofcenal
#list:
#used to store multiple items in a single variable,ordered,changeable,and allow duplicate valeus
#digunakan untuk menyimpan beberapa item (data) dalam satu variabel,berurutan,dapat di ubah dan memperbolehkan nilai duplikat (mirip/sama/ganda)
nama_teman_temanku = ["nailah", "haikar", "dewi", "anggun", "najiel", "mattew"]
umur_teman_temanku = [15, 16, 16, 15, 16, 13.0, 19.0, 7.9]
#        index           0          1         2        3         4         5

#KARENA ADANYA MEMILIKI INDEX : 0,1,2,3,4,5
#menambah data dalam list (Append) (en)--> Menambah (id))
nama_teman_temanku.append("nailah")
print(nama_teman_temanku)

#mengubah data di dalam list
nama_teman_temanku[2] = "raihan"
print(nama_teman_temanku)
#MENAMBAH TEMAN BARU DI INDEX TERTENTU
#namavariabel_list.insert(nomorindex yang dituju,value)
nama_teman_temanku.insert(4,"anjung")
print(nama_teman_temanku)

#MENGHAPUS
#menghapus nerdasarkan value
nama_teman_temanku.remove("nailah")
print(nama_teman_temanku)
#yang di hapus adalah yang pertama kali di dapat

#menghapus berdasarkan index
nama_teman_temanku.pop(5)
print(nama_teman_temanku)

#len ---> Length ---->memngatahui panjang list
print("jumlah data dalam list adalah :", len(nama_teman_temanku))


#menghapus berdasarkan index
#dictionary
#dictionaries are used to store data values in key:value pairs.
#A dictionary is a collation which ordered*,changead and do not allow duplickets


# boolean :
# represent one of  two values ot false
#mempresentasikan salah satu nilai : benar (true) atau (false)

apakah_benar = True
apakah_salah = False

sudah_login = 'True'
sudah_logout = "True"

#1. perhatikan list berikut

nama_public_figur = ["Rafi Ahmad","Maudy Ayunda","Rossa","Vincent Rompies","David Beckham"]

print(nama_public_figur)
nama_public_figur [2] = "agnes mo"
print(nama_public_figur)

print("jumlah data dalam list adalah :", len(nama_public_figur))



#A.cetak nama pertama dan terakhir yang terdapat di list
#B. ganti nama di dalam indeks ke 2 dengan nama agnes mo
#c. tampilkan seluruh isi list setelah diubah


#2. perhatikan list berikut 
nama_makanan_favorit = ["rendang","bakso",'mie ayam',"popmie","steak","ice cream"]
nama_dessert_favorit = ["pudding","parfait","omelete","crepes","waffles"]


nama_dessert_favorit.insert(0,"chocolate")
nama_dessert_favorit.insert(5,"stawberry")
print(nama_dessert_favorit)

nama_makanan_favorit.remove("ice cream")
print(nama_makanan_favorit)

nama_dessert_favorit[5]="ice cream"
print(nama_dessert_favorit)

nama_dessert_favorit.remove("omelete")
print(nama_dessert_favorit)

nama_makanan_favorit.insert(6,"omelete")
print(nama_makanan_favorit)
#a. tambahkan 2 makanan baru --
#  chocolate dan stawberry di awal dan akhir list nama_dessert_favorit
#b.hapus nama ice cream dari nama_makanan_favorit
#  lalu pindahkan ke nama_dessert_favorit
#c. hapus nama omelete dari nama_dessert_favorit
#   pindahkan ke makanan  ke nama_dessert_favorit


































































































































































































































































































































































