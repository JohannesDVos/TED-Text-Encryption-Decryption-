import random

text = input("Enter the text: ")
shift_amount = random.randint(1, 25) # Use a random shift for variety and security

mode = input("Choose your mode:\n[1] Encrypt\n[2] Decrypt\nPlease Enter 1 or 2: \n").strip()

while mode != "1" and mode != "2":
    print("Invalid mode. Please choose 1 or 2.")
    mode = input("Choose your mode:\n[1] Encrypt\n[2] Decrypt\nPlease Enter 1 or 2: \n").strip()

result_text = ""

if mode == "1":
    for char in text:
        new_unicode = ord(char) + shift_amount
        result_text += chr(new_unicode)

elif mode == "2":
    shift_amount = int(input("Enter the shift amount to decrypt: \n"))
    
    for char in text:
        original_unicode = ord(char) - shift_amount
        result_text += chr(original_unicode)

print("Original Text:", text)
print(f"Shift Amount: {shift_amount}")
print("Result:", result_text)
