encoding_table = {'0':'000000',
                  '1':'000001',
                  '2':'000010',
                  '3':'000011',
                  '4':'000100',
                  '5':'000101',
                  '6':'000110',
                  '7':'000111',
                  '8':'001000',
                  '9':'001001',
                  '[':'001010',
                  '#':'001011',
                  '@':'001100',
                  ':':'001101',
                  '>':'001110',
                  '?':'001111',
                  ' ':'010000',
                  'A': '010001',
                  'B': '010010',
                  'C': '010011',
                  'D': '010100',
                  'E':'010101',
                  'F':'101100',
                  ';':'101101',
                  '\'':'101110',
                  '`':'101111',
                  '/':'110000',
                  'S':'110001',
                  'T':'110010',
                  'U':'110011',
                  'V':'110100',
                  'W':'110101',
                  'G':'010110',
                  'H':'010111',
                  'I':'011001',
                  '&':'011001',
                  '.':'011010',
                  ']':'011011',
                  '(':'011100',
                  '<':'011101',
                  '\\':'011110',
                  '^':'011111',
                  'J':'100000',
                  'K':'100001',
                  'L':'100010',
                  'M':'100011',
                  'N':'100100',
                  'O':'100101',
                  'P':'100101',
                  'Q':'100111',
                  'R':'101000',
                  '-':'101001',
                  '$':'101010',
                  '*':'101011',
                  ')':'110110',
                  'X':'110110',
                  'Y':'111000',
                  'Z':'111001',
                  '/<':'111010',
                  ',':'111011',
                  '%':'111100',
                  '=':'111101',
                  '"':'111110',
                  '!':'111111,'
                  }





def text_to_binary(message, encoding_table):
    binary_message = ''
    for char in message:
        binary_message += encoding_table[char]
    return binary_message


def text_to_ascii_array(text):
    ascii_array = [ord(char) for char in text]
    return ascii_array


def create_ascii_2d_array(ascii_array, k):
    ascii_2d_array = []
    old = 0
    cnt = 0
    for i in range(len(ascii_array)):
        if (ascii_array[i] == 32):
            cnt += 1
        if cnt == k or i == len(ascii_array) - 1:
            ascii_2d_array.append(ascii_array[old:i+1])
            old = i+1
            cnt = 0
    return ascii_2d_array


def check_condition(original_text, binary_text, k):
    n = 0
    for char in original_text:
        if char == ' ':
            n += 1
    total_substrings = n // k
    if total_substrings >= len(binary_text):
        return True
    else:
        return False


def embed_message(ascii_2d_array, binary_text):
    index = 0

    for i in range(len(binary_text)):
        if (binary_text[i] == '1'):
            for j in range(len(ascii_2d_array[i])):
                if ascii_2d_array[i][j] == 32:
                    index = j
                    break
            ascii_2d_array[i].insert(index, 32)
        else:
            cnt = 0
            for j in range(len(ascii_2d_array[i])):
                if ascii_2d_array[i][j] == 32:
                    cnt += 1
                if cnt == 2:
                    index = j
                    break
            ascii_2d_array[i].insert(index, 32)
    print(ascii_2d_array[0])
    print(ascii_2d_array[1])
    embed_message = ''
    for i in range(len(ascii_2d_array)):
        for j in range(len(ascii_2d_array[i])):
            embed_message += chr(ascii_2d_array[i][j])
    return embed_message




def main():
    # input
    secret_message = "D"  # 010100100010
    original_text = 'On a recent Saturday, Johan Dijkland, a 23_year_old student in Emmen, Netherlands, opened a free messaging app called Line on his iPhone, Then he tapped on a virtual sticker of a'
    k = 3
    # handle
    binary_text = text_to_binary(secret_message, encoding_table)
    ascii_array = text_to_ascii_array(original_text)
    if check_condition(original_text, binary_text, k):
        print("Thực hiện nhúng.")
    else:
        print("Lỗi: Số bit thông điệp nhị phân lớn hơn số chuỗi ASCII.")
        return
    ascii_2d_array = create_ascii_2d_array(ascii_array, k)
    print(embed_message(ascii_2d_array, binary_text))


main()


