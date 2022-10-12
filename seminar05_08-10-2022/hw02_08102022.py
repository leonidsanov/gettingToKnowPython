# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D0%B4%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5_%D0%B4%D0%BB%D0%B8%D0%BD_%D1%81%D0%B5%D1%80%D0%B8%D0%B9#:~:text=run%2Dlength%20encoding%2C%20RLE),%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D1%89%D0%B0%D1%8F%20%D0%B8%D0%B7%20%D0%BD%D0%B5%D1%81%D0%BA%D0%BE%D0%BB%D1%8C%D0%BA%D0%B8%D1%85%20%D0%BE%D0%B4%D0%B8%D0%BD%D0%B0%D0%BA%D0%BE%D0%B2%D1%8B%D1%85%20%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%D0%BE%D0%B2.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('file_encode.txt', 'w') as data:
    data.write('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')

with open('file_encode.txt', 'r') as data:
    string = data.readline()

def rleEncode(decoded_string):
    encoded_string = ''
    count = 1
    char = decoded_string[0]
    for i in range(1, len(decoded_string)):
        if decoded_string[i] == char:
            count += 1
        else:
            encoded_string = encoded_string + str(count) + char
            char = decoded_string[i]
            count = 1
            encoded_string = encoded_string + str(count) + char
    return encoded_string


def rleDecode(encoded_string):
    decoded_string = ''
    char_amount = ''
    for i in range(len(encoded_string)):
        if encoded_string[i].isdigit():
            char_amount += encoded_string[i]
        else:
            decoded_string += encoded_string[i] * int(char_amount)
        char_amount = ''
    print(decoded_string)

    return decoded_string


with open('file_encode.txt', 'r') as file:
    decoded_string = file.read()

with open('file_decode.txt', 'w') as file:
    encoded_string = rleEncode(decoded_string)
    file.write(encoded_string)

print('Decoded string: \t' + decoded_string)
print('Encoded string: \t' + rleEncode(decoded_string))
print(f'Compress ratio: \t{round(len(decoded_string) / len(encoded_string), 1)}')