with open('1.txt', encoding='utf-8') as f:
    text_1 = f.read()

with open('2.txt', encoding='utf-8') as f:
    text_2 = f.read()

with open('3.txt', encoding='utf-8') as f:
    text_3 = f.read()

number_of_lines_1 = text_1.count('\n') + 1
number_of_lines_2 = text_2.count('\n') + 1
number_of_lines_3 = text_3.count('\n') + 1

final_text = ''
text_1 = '1.txt\n' + str(number_of_lines_1) +'\n' + text_1 + '\n'
text_2 = '2.txt\n' + str(number_of_lines_2) +'\n' + text_2 + '\n'
text_3 = '3.txt\n' + str(number_of_lines_3) +'\n' + text_3 + '\n'

dict_text = {
    number_of_lines_1: text_1,
    number_of_lines_2: text_2,
    number_of_lines_3: text_3
}

list_number_of_lines = list(dict_text.keys())
list_number_of_lines.sort()

for number_of_lines in list_number_of_lines:
    final_text = final_text + dict_text[number_of_lines]

with open('final.txt', 'w', encoding='utf-8') as f:
    f.write(final_text)
