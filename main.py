# impor
import hello

#panggil
hello.world()

# cetak
print(hello.nama)

#review
diko = hello.Reviewer("Diko", "Python")
diko.review()

k = hello.Kalkulator()

print(k.tambah_angka(1, 2))

print(k.kali_angka(20, 50))

a = k.kali_angka(6, 5)
print(a)

b = int(input("Masukkan angka pertama   : "))
c = int(input("Masukkan angka kedua     : "))

d = k.tambah_angka(b, c)
print("hasil penjumlahannya adalah : ", d)