class Item:
    def __init__(self, kode, nama, jumlah):
        self.kode = kode
        self.nama = nama
        self.jumlah = jumlah

    def __str__(self):
        return f"Kode: {self.kode}, Nama: {self.nama}, Jumlah: {self.jumlah}"


class InventoryManager:
    def __init__(self):
        self.inventaris = []

    def tambah_item(self):
        print("\n--- Tambah Item ---")
        kode = input("Masukkan kode item: ")
        nama = input("Masukkan nama item: ")
        jumlah = int(input("Masukkan jumlah item: "))
        item = Item(kode, nama, jumlah)
        self.inventaris.append(item)
        print("Item berhasil ditambahkan!")

    def edit_item(self):
        print("\n--- Edit Item ---")
        kode = input("Masukkan kode item yang akan diedit: ")
        for item in self.inventaris:
            if item.kode == kode:
                print(f"Item ditemukan: {item}")
                item.nama = input("Masukkan nama baru: ")
                item.jumlah = int(input("Masukkan jumlah baru: "))
                print("Item berhasil diperbarui!")
                return
        print("Item tidak ditemukan!")

    def hapus_item(self):
        print("\n--- Hapus Item ---")
        kode = input("Masukkan kode item yang akan dihapus: ")
        for item in self.inventaris:
            if item.kode == kode:
                self.inventaris.remove(item)
                print("Item berhasil dihapus!")
                return
        print("Item tidak ditemukan!")

    def lihat_inventaris(self):
        print("\n--- Daftar Inventaris ---")
        if not self.inventaris:
            print("Inventaris kosong.")
        else:
            for item in self.inventaris:
                print(item)

    def menu(self):
        while True:
            print("\n--- Menu Inventaris ---")
            print("1. Tambah Item")
            print("2. Edit Item")
            print("3. Hapus Item")
            print("4. Lihat Inventaris")
            print("5. Keluar")
            pilihan = input("Pilih menu (1-5): ")

            if pilihan == "1":
                self.tambah_item()
            elif pilihan == "2":
                self.edit_item()
            elif pilihan == "3":
                self.hapus_item()
            elif pilihan == "4":
                self.lihat_inventaris()
            elif pilihan == "5":
                print("Keluar dari program. Terima kasih!")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")


# Menjalankan program
if __name__ == "__main__":
    inventory_manager = InventoryManager()
    inventory_manager.menu()
