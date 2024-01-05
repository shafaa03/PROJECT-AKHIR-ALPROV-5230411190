import sqlite3
koneksi = sqlite3.connect('database_fauna.db')

koneksi.execute('''
                CREATE TABLE FAUNA(
                    ID_FAUNA INTEGER PRIMARY KEY AUTOINCREMENT,
                    NAMA_FAUNA VARCHAR(50),
                    JENIS VARCHAR(50),
                    ASAL VARCHAR(50),
                    JUMLAH_SAAT_INI INTEGER(10),
                    TAHUN_TERAKHIR_DITEMUKAN INTEGER(10)
                )    
                 
                ''')
koneksi.close()