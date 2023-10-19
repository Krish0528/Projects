from art import logo


morse_dict = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.',
              '0': '-----', ', ': '--..--', '.': '.-.-.-',
              '?': '..--..', '/': '-..-.', '-': '-....-',
              '(': '-.--.', ')': '-.--.-'}


def encrypt_text(message):
    code = ""
    for char in message:
        if char in morse_dict:
            code += morse_dict[char] + " "
        elif char not in morse_dict:
            if char == " ":
                code += "   "
            else:
                code += char + " "
    print(f"Here's the encrypted result: {code}")


def decrypt_code(code):
    message = ""
    code_list = code.split("   ")
    for num in range(len(code_list)):
        char_list = code_list[num].split(" ")
        for char in char_list:
            for letter, code in morse_dict.items():
                if code == char:
                    message += letter

        message += " "

    print(f"Here's the decrypted result: {message}")


print(logo)

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction == "encode":
        users_input = input("Type the text/sentence you want to encrypt?: ").upper()
        encrypt_text(message=users_input)
    else:
        users_input = input("Type the morse code you want to decrypt?: ")
        decrypt_code(code=users_input)

    restart = input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        should_end = True
        print("\nGoodbye.")
