# Custom Decorator untuk mencatat aktivitas pemanggilan method
def log_aktivitas(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Menjalankan method: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


class Mahasiswa:
    # 1. CONSTRUCTOR (__init__)
    def __init__(self, nama, nim, ipk):
        self.nama = nama      # Otomatis melewati validasi setter nama
        self.nim = nim        # Otomatis melewati validasi setter nim
        self.ipk = ipk        # Otomatis melewati validasi setter ipk

    # 2. DECORATOR (@property & @setter) + 3. VALIDATION
    @property
    def nama(self):
        return self._nama

    @nama.setter
    def nama(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Nama tidak boleh kosong dan harus berupa teks.")
        self._nama = value.strip()

    @property
    def nim(self):
        return self._nim

    @nim.setter
    def nim(self, value):
        if not str(value).isdigit() or len(str(value)) < 8:
            raise ValueError("NIM harus berupa angka minimal 8 digit.")
        self._nim = str(value)

    @property
    def ipk(self):
        return self._ipk

    @ipk.setter
    def ipk(self, value):
        if not isinstance(value, (int, float)) or not (0.0 <= value <= 4.0):
            raise ValueError("IPK harus berupa angka antara 0.00 sampai 4.00.")
        self._ipk = float(value)

    # Method dengan Custom Decorator
    @log_aktivitas
    def tampilkan_data(self):
        print("=== PROFIL MAHASISWA ===")
        print(f"Nama : {self.nama}")
        print(f"NIM  : {self.nim}")
        print(f"IPK  : {self.ipk:.2f}")
        print("========================\n")


# --- EKSEKUSI PROGRAM ---
if __name__ == "__main__":
    # 1. Uji data valid melalui Constructor
    try:
        mhs1 = Mahasiswa("Yogi Paulus", "202501001", 3.75)
        mhs1.tampilkan_data()

        # Update nilai IPK yang valid melalui Setter Decorator
        mhs1.ipk = 3.90
        print(f"Update IPK berhasil: {mhs1.ipk:.2f}\n")
    except ValueError as err:
        print(f"Error: {err}\n")

    # 2. Uji Validation saat mengubah atribut dengan nilai salah
    try:
        mhs1.ipk = 4.50
    except ValueError as err:
        print(f"Validasi Update Gagal: {err}")

    # 3. Uji Validation saat instansiasi objek baru dengan data salah
    try:
        mhs2 = Mahasiswa("Nita Sari", "1234", 3.60)
    except ValueError as err:
        print(f"Validasi Constructor Gagal: {err}")
