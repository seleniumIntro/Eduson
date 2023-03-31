import csv
import pandas
from pyparsing import Word, alphas


class TestCsv:
    def test_csv(self):
        with open('../configs/account.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(', '.join(row))

    def test_pandas_sort(self):

        data = {'Clients': ['Oleg','Viktor','Maria','Andrey'],
                'Money': [44,25000,24700000,350000]
                }
        df = pandas.DataFrame(data)
        df.sort_values(by=['Money'], inplace=True)

        print(df)

    def test_pyparsing(self):
        greet = Word(alphas) + "," + Word(alphas) + "!"
        hello = "Hello, World!"
        print(hello, "->", greet.parseString(hello))




