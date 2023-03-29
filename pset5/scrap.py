from re import A
import string

shift = 2
shifted = {}

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase

for idx, letter in enumerate(lowercase):
    try:
        shifted[letter] = lowercase[idx + shift]
    except IndexError:
        shifted[letter] = lowercase[idx + shift - 26] 
print(shifted)


# message = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
# output_message = ""
# for char in message:

#     if char.isalpha():
#         output_message += shifted[char]
#     else:
#         output_message += char

# print(output_message)

from ps5 import PlaintextMessage, CiphertextMessage



# text = PlaintextMessage('cheat step mud study ditch please leave carry bow silver direct familiar religion cowardice reputation', 21)
# print(text.get_message_text_encrypted())

# dec_text = CiphertextMessage(text.get_message_text_encrypted())

# best_val, text_decipher = dec_text.decrypt_message()

# print(best_val)
# print(text_decipher)

text = PlaintextMessage('spill tie wire wheat by search permit coal describe type sheep standard preach choice suspect', 2)
print(text.get_message_text_encrypted())
dec_text = CiphertextMessage(text.get_message_text_encrypted())
best_val, text_decipher = dec_text.decrypt_message()
print(best_val)
print(text_decipher)