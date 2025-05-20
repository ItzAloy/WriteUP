def reverse_cipher(pesan):
    cipher_text = ""
    i = len(pesan) - 1
    while i >= 0:
        cipher_text += pesan[i]
        i -= 1
    return cipher_text

# Contoh penggunaan
pesan_asli = """Lorem Ipsum"""
cipher = reverse_cipher(pesan_asli)
print("Pesan Asli   :", pesan_asli)
print("Cipher Text  :", cipher)

