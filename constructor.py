class BankAccount:
    def __init__(self, no, saldo=0):
        # validasi saldo
        if saldo < 0:
            raise ValueError("Saldo tidak boleh negatif")
        
        self.no = no
        self.saldo = saldo

print("--- Proses Rekening Budi ---")
try:
    budi = BankAccount("1234567890", 1000)
    print(f"Status Budi: SUKSES. Rekening berhasil dibuat dengan saldo {budi.saldo}")
except ValueError as e:
    print(f"Status Budi: ERROR. {e}")

print("\n--- Proses Rekening Eko ---")
try:
    eko = BankAccount("0987654321", -1000)
    print(f"Status Eko: SUKSES. Rekening berhasil dibuat dengan saldo {eko.saldo}")
except ValueError as e:
    print(f"Status Eko: GAGAL. {e}")