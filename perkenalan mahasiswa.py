class Mahasiswa:
    def __init__(self, nama, jurusan, asal):
        self.nama = nama
        self.jurusan = jurusan
        self.asal = asal

    def perkenalan(self):
        print(f"{self.nama}: Aku {self.nama}, jurusan {self.jurusan}, dari {self.asal}.")

    def bicara(self, kalimat):
        print(f"{self.nama}: {kalimat}")

    def hello(self, nama):
        print(f"{self.nama}: Halo {nama}, aku {self.nama}.")


tazkiyah = Mahasiswa("Tazkiyah", "Sistem Informasi", "Balaraja, Kabupaten Tangerang")
ratu = Mahasiswa("Ratu", "Sistem Informasi", "Pabuaran, Kabupaten Serang")

print("Hari pertama kuliah di Universitas Bina Bangsa.")
print("Kelas Sistem Informasi, dosen belum datang.\n")

ratu.bicara("Eh, kursi ini kosong nggak?")
tazkiyah.bicara("Kosong, sini aja.")
ratu.bicara("Makasih. Ini kelas SI kan? Takut salah masuk aku.")
tazkiyah.bicara("Iya bener, tadi aku juga nanya orang dulu wkwk.")
ratu.bicara("Aku Ratu btw.")
tazkiyah.hello("Ratu")
tazkiyah.bicara("Kamu asli mana?")
ratu.bicara("Serang, Pabuaran. Tau nggak?")
tazkiyah.bicara("Nggak hehe. Aku Balaraja, Tangerang.")
ratu.bicara("Oh gitu. Kamu ngekos?")
tazkiyah.bicara("Iya, males bolak-balik. Tapi rumah deket sih, weekend pulang. Kamu?")
ratu.bicara("Nggak, pp. Tadi berangkat pagi.")
tazkiyah.bicara("Pagi banget dong? Rajin amat.")
ratu.bicara("Takut macet, hari pertama juga.")
tazkiyah.bicara("Dosennya siapa ya sekarang?")
ratu.bicara("Nggak tau, aku belum liat jadwal bener-bener.")
tazkiyah.bicara("Semoga nggak galak.")
ratu.bicara("Aamiin. Eh, itu kayaknya dosennya masuk.")
tazkiyah.bicara("Eh iya, lanjut nanti lg aja.")

print("\n(Dosen masuk, kelas dimulai.)")