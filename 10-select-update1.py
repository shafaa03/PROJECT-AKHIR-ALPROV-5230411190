import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()


kursor.execute(f"UPDATE FAUNA SET JUMLAH_SAAT_INI = 650 WHERE ID_FAUNA = 10 ")
koneksi.commit()

# cek apakah data berhasil diubah atau belum
if kursor.rowcount > 0: # cek berdasarkan adanya baris atau tidak
    print(f"Data berhasil Diubah!")
else:
    print(f"Tidak ada data dengan ID tersebut!")
    
    
koneksi.close()
