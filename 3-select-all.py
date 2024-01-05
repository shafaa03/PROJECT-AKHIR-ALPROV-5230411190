import sqlite3
koneksi = sqlite3.connect('database_fauna.db')

kursor = koneksi.cursor()

kursor.execute("SELECT *FROM FAUNA")
#Tampilkan dalam bentuk baris
baris_tabel = kursor.fetchall()

#Membuat format tabel dengan method format()
print("TABEL FAUNA")
print("="*120)
print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20}".format("ID FAUNA", "NAMA FAUNA", "JENIS", "ASAL", "JUMLAH SAAAT INI", "TAHUN TERKHIR DITEMUKAN"))
print("-"*120)
# Tampilkan data sesuai format tabel dengan perulangan
for baris in baris_tabel:
    print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))
    
koneksi.close()