import logger as lg

def input_data(data):
    div = [' ', ',', ';']
    for i in div:
        if i in data:
            data = ' '.join(data.split(i))

    with open('phonebook.csv', 'r', encoding='utf-8') as file:
        for line in file:
            if data + '\n' == line:
                response = 'Уже есть такая запись'
                return response

    with open('phonebook.csv', 'a', encoding='utf-8') as file:
        file.write(data + '\n')
    lg.log('input', data)
    response = 'Данные внесены'
    return response



def output_data(data):
    with open('phonebook.csv', 'r', encoding='utf-8') as file:
        response = []
        for line in file:
            if data.lower() in line.lower():
                response.append(line)
    if response:
        lg.log('output', data)
        return response
    else: return 'Нет данных'



