class PDKT:
    def __init__(self, nama1,nama2):
        self.orang_pertama = nama1
        self.orang_kedua = nama2

    def topik_pertama(self):
        print(f"{self.nama1}: Nit, malam ini sibuk enggak?")
        print(f"{self.nama2}: Enggak sih emangnya kenapa?")
        print(f"{self.nama1}: Oke, Nanti malem aku Jemput yah:)")
        print(f"{self.nama2}: boleh..\n")

    def topik_kedua(self):

        print(f"{self.nama2}: Emangnya Kita Mau kemana ya..?")
        print(f"{self.nama1}: Mau Ngajak Kamu Makan, Kamu Belum Makan kan?")
        print(f"{self.nama2}: Ko kamu Tau!")
        print(f"{self.nama1}: iyah dong apasih yang Yogi Gak tau Soal Kamu")
        print(f"{self.nama2}: hmmm Bisa aja :)") 
        print(f"{self.nama1}: Nah Gimana kalau kita cobain kedai ramen baru dekat sekolahku dulu? Katanya enak banget rasanya.")
        print(f"{self.nama2}: Wah, pas banget! Aku suka makanan yang kaldunya kental, terus pesen gyoza juga buat tambahannya ya.\n")
        print(f"{self.nama1}: Siap, Amannn")

    def topik_ketiga(self):
        print(f"{self.nama2}: hmmmm enak juga yah ramennya!")
        print(f"{self.nama1}: Makanya, aku kan tau aja tempat makan yang enak buat kamu.")
        print(f"{self.nama2}: Iya deh, jago banget pilih tempatnya. Makasih ya buat malam ini, Yog.")
        print(f"{self.orang_pertama}: Sama-sama, Nita. Asal kamu senang, aku juga ikut senang.\n")

    def topik_keempat(self):
        print(f"{self.nama1}: Eh, udah mau sampai rumah kamu nih. Nanti malam jangan lupa istirahat ya.")
        print(f"{self.nama2}: Siap, Pak Driver! Kamu juga hati-hati ya pulangnya.")
        print(f"{self.nama1}: Pasti dong. Besok-besok kita jalan lagi mau kan?")
        print(f"{self.nama2}: Hahaha, boleh... kabarin lagi aja ya. Good night, Yogi!")
        print(f"{self.nama1}: Malam juga, Nit. Mimpi indah ya! :)\n--- PDKT BERHASIL LEVEL UP ---" )
PDKT = PDKT ("Yogi", "Nita")
PDKT.topik_pertama()
PDKT.topik_kedua()
PDKT.topik_ketiga()
PDKT.topik_keempat()