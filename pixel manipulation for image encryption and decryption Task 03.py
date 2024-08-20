def xor_encrypt_decrypt(image_path, key):
    try:
    
        with open(image_path, 'rb') as fin:
            image = bytearray(fin.read())

        for index in range(len(image)):
            image[index] ^= key

        with open(image_path, 'wb') as fout:
            fout.write(image)

        print('successfully.')

    except Exception as e:
        print('Error caught:', str(e))


def main():
    operation = input("Do you want to Encrypt or Decrypt(e/d) the image ? ").lower()
    if operation not in ['e', 'd']:
        print("Invalid choice. Please select 'e' to encrypt or 'd' to decrypt.")
        return

    image_path = input('Enter image path: ')
    key = int(input('Enter key for encryption/decryption: '))

    print('The path of the file:', image_path)
    print('Note: Encryption key and Decryption key must be the same.')
    print('Key for operation:', key)

    xor_encrypt_decrypt(image_path, key)


if __name__ == "__main__":
    main()