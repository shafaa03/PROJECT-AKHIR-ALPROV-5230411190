import sqlite3
koneksi = sqlite3.connect('database_fauna.db')

koneksi.execute(f'''
                INSERT INTO FAUNA (NAMA_FAUNA, JENIS, ASAL, JUMLAH_SAAT_INI, TAHUN_TERAKHIR_DITEMUKAN)
                VALUES('Harimau Jawa', 'Mamalia', 'Jawa', '40', '2019')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (NAMA_FAUNA, JENIS, ASAL, JUMLAH_SAAT_INI, TAHUN_TERAKHIR_DITEMUKAN)
                VALUES('Kuskus Beruang', 'Mamalia', 'Sulawesi', '30', '2021')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (NAMA_FAUNA, JENIS, ASAL, JUMLAH_SAAT_INI, TAHUN_TERAKHIR_DITEMUKAN)
                VALUES('Beruang Madu', 'Mamalia', 'Sumatera', '1000', '2020')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (NAMA_FAUNA, JENIS, ASAL, JUMLAH_SAAT_INI, TAHUN_TERAKHIR_DITEMUKAN)
                VALUES('Pesut Mahakam', 'Mamalia', 'Kalimantan', '100', '2021')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (NAMA_FAUNA, JENIS, ASAL, JUMLAH_SAAT_INI, TAHUN_TERAKHIR_DITEMUKAN)
                VALUES('Burung Maleo', 'Burung', 'Sulawesi', '7000', '2023')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (NAMA_FAUNA, JENIS, ASAL, JUMLAH_SAAT_INI, TAHUN_TERAKHIR_DITEMUKAN)
                VALUES('Macan Dahan', 'Mamalia', 'Sumatera', '400', '2020')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (NAMA_FAUNA, JENIS, ASAL, JUMLAH_SAAT_INI, TAHUN_TERAKHIR_DITEMUKAN)
                VALUES('Kancil', 'Mamalia', 'Jawa', '60', '2022')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (NAMA_FAUNA, JENIS, ASAL, JUMLAH_SAAT_INI, TAHUN_TERAKHIR_DITEMUKAN)
                VALUES('Gajah Kalimantan', 'Mamalia', 'Kalimantan', '1500', '2021')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (NAMA_FAUNA, JENIS, ASAL, JUMLAH_SAAT_INI, TAHUN_TERAKHIR_DITEMUKAN)
                VALUES('Elang Jawa', 'Burung', 'Jawa', '200', '2021')
                ''')
koneksi.execute(f'''
                INSERT INTO FAUNA (NAMA_FAUNA, JENIS, ASAL, JUMLAH_SAAT_INI, TAHUN_TERAKHIR_DITEMUKAN)
                VALUES('Katak Borneo', 'Amfibi', 'Kalimantan', '2000', '2023')
                ''')

koneksi.commit()
koneksi.close()