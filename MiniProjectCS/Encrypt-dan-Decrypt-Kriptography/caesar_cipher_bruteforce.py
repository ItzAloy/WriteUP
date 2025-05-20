def caesar_brute_force(cipher_text):
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for key in range(len(LETTERS)):
        translated = ""
        for symbol in cipher_text:
            if symbol.upper() in LETTERS:
                num = LETTERS.find(symbol.upper()) - key
                if num < 0:
                    num += len(LETTERS)
                translated += LETTERS[num] if symbol.isupper() else LETTERS[num].lower()
            else:
                translated += symbol
        print(f"Key {key}: {translated}")
        
def main():
    cipher_text = """Lorem Ipsum"""
    print("Cipher Text:", cipher_text)
    print("Brute Force Result:")
    caesar_brute_force(cipher_text)

if __name__ == "__main__":
    main()
