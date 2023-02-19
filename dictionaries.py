# customer = {
#     'name': 'Rychu Sobol',
#     'weight': 160,
#     'verified': True
# }
# print(customer.get('verified')) # lub customer['verified']

# number_conversion = {
#     "1" : "One",
#     "2" : "Two",
#     "3" : "Three",
#     "4" : "Four",
#     "5" : "Five"
# }
#
# phone = input("Enter your phone number: ")
# phone_converted = ""
# for i in phone:
#     #phone_converted += number_conversion[i] + " "
#     phone_converted += number_conversion.get(i) + " "
# print(phone_converted)

# emoji converter
message = input('> ')
words = message.split(' ')
emojis = {
    ":)": "😊"
}
output = ''
for word in words:
    output += emojis.get(word, word) + ' '
print(output)


def emoji_converter(message):
    words = message.split(" ")
    emojis ={
        ":)" : "😊",
        ":(" : "😞"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


print(emoji_converter("Where did it all go? :("))
