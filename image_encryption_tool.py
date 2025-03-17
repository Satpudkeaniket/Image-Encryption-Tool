from PIL import Image
import os

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    # Convert the image to RGB mode if it's not already
    if img.mode != 'RGB':
        img = img.convert('RGB')
    pixels = img.load()

    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Apply a basic mathematical operation to each pixel
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            pixels[x, y] = (r, g, b)

    encrypted_image_path = os.path.splitext(image_path)[0] + "_encrypted.png"
    img.save(encrypted_image_path)
    print(f"Image encrypted and saved as {encrypted_image_path}")
    return encrypted_image_path

def decrypt_image(encrypted_image_path, key):
    img = Image.open(encrypted_image_path)
    # Convert the image to RGB mode if it's not already
    if img.mode != 'RGB':
        img = img.convert('RGB')
    pixels = img.load()

    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Reverse the mathematical operation to decrypt
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            pixels[x, y] = (r, g, b)

    decrypted_image_path = os.path.splitext(encrypted_image_path)[0] + "_decrypted.png"
    img.save(decrypted_image_path)
    print(f"Image decrypted and saved as {decrypted_image_path}")
    return decrypted_image_path

def main():
    print("Image Encryption Tool")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = input("Choose an option (1 or 2): ")

    if choice not in ['1', '2']:
        print("Invalid choice. Please select 1 or 2.")
        return

    image_path = input("Enter the path to the image file: ")
    key = int(input("Enter the encryption/decryption key (an integer): "))

    if choice == '1':
        # Encrypt the image
        encrypted_image_path = encrypt_image(image_path, key)
        print("Encryption complete!")
    elif choice == '2':
        # Decrypt the image
        decrypted_image_path = decrypt_image(image_path, key)
        print("Decryption complete!")

if __name__ == "__main__":
    main()