# 1
# Создать файл, в нем написать текст
with open('hw_8_1.txt', 'w') as file:
    file.write('name: mariia; age:25; female\n')

# Считать данные с файла и вывести в консоль
with open('hw_8_1.txt', 'r') as file:
    print(file.read())

# Cчитать данные с этого же файла и записать в новый файл
with open('hw_8_1.txt', 'r') as file_r, open('hw_8_2.txt', 'w') as file_w:
    data = file_r.read()
    file_w.write(data)

# Считать данные с этого же файла, преобразовать (любые операции) и записать в этот же файл
with open('hw_8_1.txt', 'r') as file:
    data = (file.read()).title()
with open('hw_8_1.txt', 'r+') as file:
    file.write(data)

# 2
# Написать программу, которая откроет файл questions.json и после ответов на вопросы, запишет их назад в этот же файл
import json

with open('questions.json', 'r') as file:
    data = json.load(file)

    for q in data['questions']:
        q['answer'] = input(q['q'])

with open('questions.json', 'w') as file:
    json.dump(data, file, indent=4)
