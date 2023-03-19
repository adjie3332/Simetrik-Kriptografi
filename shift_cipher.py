# Description: Shift Cipher

# Fungsi untuk mengenkripsi pesan dengan algoritma shift cipher
def encrypt(message, key):
    cipher = ''  # inisialisasi variabel cipher
    for char in message:
        if char.isalpha():  # jika karakter saat ini adalah alfabet
            cipher += chr((ord(char) - 65 + key) % 26 + 65)  # tambahkan karakter yang telah dienkripsi ke variabel cipher
        else:  # jika karakter saat ini bukan alfabet
            cipher += char  # tambahkan karakter asli ke variabel cipher
    return cipher

# Fungsi untuk mendekripsi pesan yang telah dienkripsi dengan algoritma shift cipher
def decrypt(cipher, key):
    message = ''  # inisialisasi variabel message
    for char in cipher:
        if char.isalpha():  # jika karakter saat ini adalah alfabet
            message += chr((ord(char) - 65 - key) % 26 + 65)  # tambahkan karakter yang telah didekripsi ke variabel message
        else:  # jika karakter saat ini bukan alfabet
            message += char  # tambahkan karakter asli ke variabel message
    return message

# Fungsi utama
def main():
    message = input('Masukkan pesan: ')  # input pesan
    # NIM L200204219
    # Menggunakan shift 19, dikarenakan 2 Digit terakhir NIM saya adalah 19
    key = 19  # inisialisasi variabel key
    cipher = encrypt(message, key)  # enkripsi pesan
    print('Pesan yang telah dienkripsi: ', cipher)  # cetak pesan yang telah dienkripsi
    print('Pesan yang telah didekripsi: ', decrypt(cipher, key))  # cetak pesan yang telah didekripsi

# Panggil fungsi utama
if __name__ == '__main__': 
    main()