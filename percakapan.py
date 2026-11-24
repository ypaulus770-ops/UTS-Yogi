class Mahasiswa :
      nim = 0
      nama =""

      def perkenalan(self):
            print(f"Yogi : Halo nama saya {self.nama}")

      def hello(self,nama):
            print(f"Abi : halo {self.nama},nama saya {nama}")

mahasiswa = Mahasiswa()
mahasiswa.nama ="Yogi"
mahasiswa.perkenalan()
mahasiswa.hello("Abi") 