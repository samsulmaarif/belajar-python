# definisi
def world():
    print("Hello World!")


# panggil di sini
# world()


class Kalkulator:
    """Contoh kelas kalkulator sederhana"""
    i = 12345

    def f(self):
        return 'Hello world'

    def tambah_angka(self, angka1, angka2):
        self.nilai = angka1 + angka2
        if self.nilai > 9:  # kalkulator sederhana hanya memroses sampai 9
            print('kalkulator sederhana melebihi batas angka: {}'.format(
                self.nilai))
        return self.nilai


class KalkulatorKali(Kalkulator):
    """Contoh mewarisi kelas kalkulator sederhana"""
    def kali_angka(self, angka1, angka2):
        self.nilai = angka1 * angka2
        return self.nilai

    # override method parent class
    # def tambah_angka(self, angka1, angka2):
    #     self.nilai = angka1 + angka2
    #     return self.nilai

    # override method parent class
    def tambah_angka(self, angka1, angka2):
        self.nilai = angka1 + angka2
        if self.nilai <= 9:
            super().tambah_angka(angka1, angka2)
        else:
            self.nilai = angka1 + angka2
        return self.nilai

kk = KalkulatorKali()
a = kk.kali_angka(2, 3)
print(a)

x = int(input("Masukkan angka yang gede: "))
y = int(input("Masukkan angka kecil: "))

b = kk.tambah_angka(x, y)
print(b)
