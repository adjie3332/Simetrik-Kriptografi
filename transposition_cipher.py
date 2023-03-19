# Description : Transposition Cipher

# Fungsi untuk mengenkripsi pesan dengan algoritma transposition cipher
def encrypt(plaintext, key):
    # Hitung panjang kunci
    key_len = len(key)
    # Hitung jumlah kolom matriks berdasarkan panjang kunci
    num_cols = key_len
    # Hitung jumlah baris matriks berdasarkan panjang pesan
    num_rows = len(plaintext) // num_cols
    if len(plaintext) % num_cols > 0: # Jika jumlah karakter pesan tidak habis dibagi dengan jumlah kolom
        num_rows += 1 # Tambahkan jumlah baris matriks
    # Tambahkan karakter padding jika jumlah karakter pesan tidak habis dibagi dengan jumlah kolom
    plaintext += (num_rows * num_cols - len(plaintext)) * '*'
    # Buat matriks berdasarkan jumlah baris dan kolom
    matrix = [list(plaintext[i:i+num_cols]) for i in range(0, num_rows*num_cols, num_cols)]
    # Inisialisasi variabel yang akan menampung pesan terenkripsi
    ciphertext = ''
    # Enkripsi pesan dengan menukar posisi kolom matriks sesuai urutan kunci
    for col in key: # Untuk setiap karakter pada kunci
        col_index = key.index(col) # Dapatkan indeks karakter pada kunci
        for row in matrix: # Untuk setiap baris matriks
            ciphertext += row[col_index] # Tambahkan karakter pada kolom matriks ke variabel ciphertext

    return ciphertext

# Fungsi untuk mendekripsi pesan yang telah dienkripsi dengan algoritma transposition cipher
def decrypt(ciphertext, key):
    # Hitung panjang kunci
    key_len = len(key)
    # Hitung jumlah kolom matriks berdasarkan panjang kunci
    num_cols = key_len
    # Hitung jumlah baris matriks berdasarkan panjang pesan terenkripsi
    num_rows = len(ciphertext) // num_cols
    # Buat matriks berdasarkan jumlah baris dan kolom
    matrix = [list(ciphertext[i:i+num_cols]) for i in range(0, num_rows*num_cols, num_cols)]
    # Inisialisasi variabel yang akan menampung pesan terdekripsi
    plaintext = ''
    # Dekripsi pesan dengan memindahkan karakter pada kolom matriks sesuai urutan kunci ke setiap baris matriks
    for row in matrix: # Untuk setiap baris matriks
        for col in key: # Untuk setiap karakter pada kunci
            col_index = key.index(col) # Dapatkan indeks karakter pada kunci
            plaintext += row[col_index] # Tambahkan karakter pada kolom matriks ke variabel plaintext

    return plaintext

# Fungsi utama
def main():
    plaintext = input('Masukkan teks: ')  # Input teks
    key = input('Masukkan key: ')  # Input key
    ciphertext = encrypt(plaintext, key)  # Enkripsi teks
    print('Teks yang telah dienkripsi: ', ciphertext)  # Cetak teks yang telah dienkripsi
    print('Teks yang telah didekripsi: ', decrypt(ciphertext, key))  # Cetak teks yang telah didekripsi

# Panggil fungsi utama
if __name__ == '__main__':
    main()
