import unittest
from datetime import datetime

def symbols (var):
    if len(var) < 1 or len(var) > 7:
        raise Exception("Symbol must be between 1-7 characters")
    else:
        return True

def capsym(var) :
    if var.isupper() == False:
        raise Exception("Symbol must be all capitalized")
    else:
        return True

def charttypes(var):
    if len(var) < 1 or len(var) > 1:
        raise Exception("Chart choice must be between 1 Character")
    else:
        return True
    
def chartright(var):
    if var == "1" or  var == "2":
        return True
    else:
        raise Exception("Please Pick 1 or 2")

def timetypes(var):
    if len(var) == 1 :
        return True
    else:
        raise Exception("Time Series must be 1 Character")
    
def timeright(var):
    if var == "1" or  var == "2" or var == "3" or var == "4":
        return True
    else:
        raise Exception("Please Pick 1,2,3,or 4")
    
def starttest(var):
    if len(var) == 10:
        return True
    else:
        raise Exception("Must be in Date format")

def endtest(var):
    if len(var) == 10:
        return True
    else:
        raise Exception("Must be in Date format")
    



class LearnTest(unittest.TestCase):
    

    def test_chart(self):
        print('\nChart Types:')
        print('1. Bar')
        print('2. Line') 
        charttype = input("\nPlease enter the chart type that you want: Either 1 or 2 ")
        self.assertEqual(charttypes(charttype),True)
        self.assertEqual(chartright(charttype),True)
    
    
    def test_asymbol(self):
       symbol = input('\nEnter stock symbol: ')
       print(type(symbol))
       self.assertEqual(symbols(symbol), True)
       self.assertEqual(capsym(symbol), True)

    def test_dtseries(self):
        print('\nSelect the Time Series of the chart you want to generate:')
        print('1. Intraday')
        print('2. Daily')
        print('3. Weekly')
        print('4. Monthly')
        time = input('\nWhat time series option would you like: Options (1-4): ')
        self.assertEqual(timetypes(time),True)
        self.assertEqual(timeright(time),True)

    def test_estart(self):
        format = "%Y-%m-%d"
        startDate = input('\nEnter the start date (format: YYYY-MM-DD): ')
        self.assertEqual(starttest(startDate),True)

    def test_fend(self):
        format = "%Y-%m-%d"
        endDate = input('\nEnter the end date (format: YYYY-MM-DD): ')
        self.assertEqual(endtest(endDate),True)



    






if __name__ == '__main__':
    unittest.main()