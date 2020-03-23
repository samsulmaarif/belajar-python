# Define a function
def world():
    print("Hello world!")

nama = "Dicoding"

class Reviewer:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

    def review(self):
        print("Reviewer " + self.nama + " bertanggung jawab di kelas " + self.kelas)

class Kalkulator:
    """Contoh kelas kalkulator sederhana"""

    def f(self):
        return 'hellow world'

    @classmethod
    def tambah_angka(cls, angka1, angka2):
        return '{} + {} = {}'.format(angka1, angka2, angka1 + angka2)
    
    @staticmethod
    def kali_angka(angka1, angka2):
        return '{} x {} = {}'.format(angka1, angka2, angka1 * angka2)