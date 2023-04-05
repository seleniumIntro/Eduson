import csv
import pandas
from pyparsing import Word, alphas


class TestCsv:
    def test_csv(self):
        #указываем путь до файла и открываем его как объект
        with open('../configs/account.csv', newline='') as csvfile:
            #превращаем объект в массив строк
            date = csv.reader(csvfile)
            #распечатываем каждую строку в цикле
            for row in date:
                print(', '.join(row))

    def test_pandas_sort(self):
        #создаём словарь с данными
        data = {'Clients': ['Oleg','Viktor','Maria','Andrey'],
                'Money': [44,25000,24700000,350000]
                }
        df = pandas.DataFrame(data) #закидываем данные в датафрейм
        #задаём колонку для сортировки, и тип inplace=True - по возрастанию
        df.sort_values(by=['Money'], inplace=True)
        #распечатываем отсортированный датафрейм
        print(df)

    def test_pyparsing(self):
        #Создаём шаблон для парсинга
        greet = Word(alphas) + "," + Word(alphas) + "!"
        #создаём строку, слова которой хотим разложить по шаблону
        #и добавить в массив
        hello = "Hello, World!"
        print(hello, "->", greet.parseString(hello))




