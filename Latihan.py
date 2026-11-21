class Mahasiswa:
kampus1 = Kampus()
kampus2 = Kampus()

print(type(kampus1))
print(type(kampus2))

mahasiswa1 = Mahasiswa()
mahasiswa2 = Mahasiswa()

print(type(mahasiswa1))
print(type(mahasiswa2))



#instance attribute
class Kampus:

mahasiswa1 = Mahasiswa()
mahasiswa1.nim = 123456
mahasiswa1.nama = "ayu"

print(mahasiswa1.nim)
print(mahasiswa1.nama)

mahasiswa2 = Mahasiswa()
mahasiswa2.nim = 123457
mahasiswa2.nama = "jenny"

print(mahasiswa2.nim)
print(mahasiswa2.nama)


#class methods
class Kampus:
    nama = ""
    alamat = ""

kampus = Kampus()
print(kampus.nama)
print(kampus.alamat)

class Mahasiswa:
    nim = 0
    nama = ""

mahasiswa = Mahasiswa()
print(mahasiswa.nim)
print(mahasiswa.nama)


#class marameter
class Mahasiswa:
    nim = 0
    nama = ""

    def perkenalan(self):
        print(f"Halo nama saya {self.nama}")


mahasiswa = Mahasiswa()
mahasiswa.nama = "ayu"
mahasiswa.perkenalan()


#class naming conventionsS
class Mahasiswa:
    nim = 0
    nama = ""

    def perkenalan(self):
        print(f"Halo nama saya {self.nama}")

    def hello(self, nama):
        print(f"Halo {nama}, nama saya {self.nama}")


mahasiswa = Mahasiswa()
mahasiswa.nama = "jenny"
mahasiswa.perkenalan()
mahasiswa.hello("tazkiyah")