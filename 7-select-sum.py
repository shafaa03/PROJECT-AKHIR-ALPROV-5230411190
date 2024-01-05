import sqlite3
koneksi = sqlite3.connect('database_fauna.db')
kursor = koneksi.cursor()

kursor.execute("SELECT SUM(JUMLAH_SAAT_INI) FROM FAUNA")
total_populasi = kursor.fetchone()[0] # ambil data gaji jadikan  baris baru dimulai dai indeks 0

print(f"Total Populasi Hewan Langka Saat Ini:{total_populasi} ")

koneksi.close()