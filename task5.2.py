out_f = open('Файл для задания 2.txt', 'r', encoding='utf-8')
content = out_f.read()
num_symbols = len(content)
num_words = content.split()
print(f'Количество слов в файле: {len(num_words)}')
print(f'Количество имволов в файле: {num_symbols}')
out_f.close
