from function import *
from mysql.connector import MySQLConnection
from kumpulanClass import *

bayuTanggal = "2-3-2022"
bayuAlamat = "Bangli"
bayuKendaraan = "motor"
def bayuPamer():
    print("Kendaraanku adalah " + bayuKendaraan)

aldiTanggal = "1-1-2000"
aldiAlamat = "Blahbatuh"
aldiKendaraan = "mobil"
def aldiPamer():
    print("Kendaraanku adalah " + aldiKendaraan)

class person:
    def __init__(self,nama, tanggal, alamat, kendaraan):
        self.nama = nama
        self.tanggal = tanggal
        self.alamat = alamat
        self.kendaraan = kendaraan
    def pamer(self):
        print("kendaraanku adalah " + self.kendaraan)


bayu = person(nama="bayu", tanggal="2-3-2022", alamat="Bangli", kendaraan="motor")
aldi = person(nama="aldi", tanggal="2-3-2022", alamat="Blahbatuh", kendaraan="mobil")

newBook = buku(
    judul= "Alex is gay",
    penulis= "Gaylex",
    tahunTerbit="2022",
    etalase="ET001",
    sinopsis="Suatu hari, alex kesambar petir dan berubah jadi gay. Apakah kalian penasaran dengan kelanjutannya? jika kalian gay, maka saksikanlan kelanjutannya"
)
newBook.daftarDatabase()