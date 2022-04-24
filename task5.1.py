out_f = open("out_file.txt", "w", encoding='utf-8')
count = True
while count != "":
    count = input('Введите данные: ')
    out_f.write(count + "\n")
out_f.close
