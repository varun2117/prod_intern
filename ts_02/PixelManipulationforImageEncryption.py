from PIL import Image

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    width, height = image.size
    encrypted_image = Image.new(image.mode, (width, height))

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            encrypted_pixel = tuple((p + key) % 256 for p in pixel)
            encrypted_image.putpixel((x, y), encrypted_pixel)

    return encrypted_image

def decrypt_image(image_path, key):
    print("decrypted Value:",key)
    return encrypt_image(image_path, -key)
    
def main():
    image_path = input("Enter the path to the image file: ")
    key = int(input("Enter the encryption/decryption key (an integer): "))

    encrypted_image = encrypt_image(image_path, key)
    encrypted_image.show()
    encrypted_image.save("encrypted_image.png")

    decrypted_image = decrypt_image("encrypted_image.png", key)
    decrypted_image.show()

if __name__ == "__main__":
    main()
