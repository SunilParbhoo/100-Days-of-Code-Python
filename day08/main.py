from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


def caesar(original_text, shift_amount, code_decode):
    updated_text = ""
    for char in original_text:
        if char not in alphabet:
            updated_text += char
        else:
            position = alphabet.index(char)
            if code_decode == "encode":
                new_position = position + shift_amount
                if new_position > 25:
                    new_letter = alphabet[new_position - 26]
                    updated_text += new_letter
                else:
                    new_letter = alphabet[new_position]
                    updated_text += new_letter
            elif code_decode == "decode":
                new_position = position - shift_amount
                if new_position < 0:
                    new_letter = alphabet[new_position + 26]
                    updated_text += new_letter
                else:
                    new_letter = alphabet[new_position]
                    updated_text += new_letter
    print(f"The {direction}d text is {updated_text}")


should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(original_text=text, shift_amount=shift, code_decode=direction)
    play_again = input(
        "Type 'yes' if you want to go again. Otherwise type 'no' \n").lower()
    if play_again == 'no':
        should_continue = False
        print("Goodbye")
