data_tiket=[]

while True:
    print("\n=== SISTEM PENGELOLAAN TIKET FESTIVAL ===")
    print("1. Tambah Data Tiket")
    print("2. Tampilkan Data Tiket")
    print("3. Ubah Data Tiket")
    print("4. Hapus Data Tiket")
    print("5. Keluar") 

    pilihan = input ("Pilih Apa? (1-5): ")
    if pilihan == "1":
        print("\n=== TAMBAH DATA TIKET ===")
        nama = input("Masukkan nama tiket: ")
        kategori = input("Masukkan kategori tiket:")

        while True: 
            harga_input=input("Masukkan harga tiket:")
            if harga_input.isdigit():
                harga=int(harga_input) 
                break
            else:
                print("Harga harus berupa angka!")
        data=[nama, kategori, harga]
        data_tiket.append(data)
        print("Data tiket berhasil ditambahkan^^")

    elif pilihan == "2":
        print("\n=== DATA TIKET FESTIVAL ===")

        if len(data_tiket) == 0:
            print("Belum ada data tiket.")
        else: 
            for i in range(len(data_tiket)):
                print("\nData ke-", i+1)
                print("Nama : ",data_tiket[i][0])
                print("Kategori : ",data_tiket[i][1])
                print("Harga : Rp",data_tiket[i][2])

    elif pilihan == "3":
        print("\n=== UBAH DATA TIKET ===")
        if len(data_tiket) == 0:
            print("Belum ada data tiket yang dapat diubah...")
        else:
            for i in range(len(data_tiket)):
                print(i + 1, ".", data_tiket[i][0])

            while True:
                nomor_input = input("Pilih nomor data yang ingin diubah:")
                if nomor_input.isdigit():
                    nomor = int(nomor_input)
                    if 1 <= nomor <= len(data_tiket):
                        break
                    else:
                        print("Nomor data tidak tersedia TwT")

                else:
                    print("Input harus berupa angka ^^")

            nama_baru = input("Masukkan nama tiket baru: ")
            kategori_baru = input("Masukkan kategori tiket baru:")

            while True:
                harga_input = input("Masukkan harga tiket baru: ")
                if harga_input.isdigit():
                    harga_baru = int(harga_input)
                    break
                else:
                    print("Harga harus berupa angka yaa")

            data_tiket[nomor - 1] = [nama_baru, kategori_baru, harga_baru]
            print("Data tiket berhasil diubah ^^")

    elif pilihan == "4":
        print("\n=== HAPUS DATA TIKET ===")
        if len(data_tiket) == 0:
            print("Belum ada data tiket yang dapat dihapus nich...")
        else:
            for i in range(len(data_tiket)):
                print(i + 1, ".", data_tiket[i][0])

            while True:
                nomor_input = input("Pilih nomor data yang ingin dihapus: ")
                if nomor_input.isdigit():
                    nomor = int(nomor_input)
                    if 1 <= nomor <= len(data_tiket):
                        break
                    else:
                        print("Nomor data tidak tersedia TwT")

                else:
                    print("input harus berupa angka yaa^^")

            data_tiket.pop(nomor - 1)
            print("data tiket berhasil dihapus hehe")

    elif pilihan == "5":
        print("\nTerimakasih telah mampir yaa^^")
        break

    else:
        print("Pilihan menu tidak ada..TwT pilihannya 1-5 yaa")

            
        

