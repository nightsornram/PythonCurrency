from tkinter import *
from tkinter import ttk
from forex_python import *
from forex_python.converter import CurrencyRates
import numpy
from matplotlib import pyplot as plt
import datetime
from forex_python.bitcoin import BtcConverter

def Selectcurrency(event):
    c1 = CurrencyRates()
    main_currency = Tk()
    main_currency.option_add("*Font", "consolas 20")
    comment_currncy1 = Label(main_currency,text = "ใส่จำวนวนเงิน")
    comment_currncy1.grid(row=0,column=0)
    comment_currncy2 = Label(main_currency, text="เลือกสกุลเงิน")
    comment_currncy2.grid(row=0, column=1)
    comment_currncy3 = Label(main_currency, text="เลือกสกุลเงิน")
    comment_currncy3.grid(row=0, column=5)
    national_currency1 = ttk.Combobox(main_currency)
    national_currency1.grid(row=1, column=1)
    national_currency1['values'] = list(c1.get_rates("").keys())
    textbow_currency1 = Entry(main_currency)
    textbow_currency1.grid(row=1, column=0)
    textbow_currency1.get()
    lebel_convert = Label(main_currency, text='>>'.center(6,' '))
    lebel_convert.grid(row=1, column=3)
    national_currency2 = ttk.Combobox(main_currency)
    national_currency2['values'] = list(c1.get_rates("").keys())
    national_currency2.grid(row=1, column=5)
    def Conversion(event):
        national_currency_list = [national_currency1.get(), national_currency2.get()]
        c = CurrencyRates()
        c.convert(national_currency_list[0], national_currency_list[1], amount=float(textbow_currency1.get()))
        result = c.convert(national_currency_list[0], national_currency_list[1], amount=float(textbow_currency1.get()))
        lebel_result.configure(text=result)
    forex_button = Button(main_currency, text="คำนวณ",bg = 'red',fg = 'white')
    forex_button.bind('<Button-1>', Conversion)
    forex_button.grid(row=2, column=0)
    lebel_result = Label(main_currency, text="ผลลัพธ์".center(10," "))
    lebel_result.grid(row=1, column=4)
    main_currency.mainloop()


def Selectgraph(event):
    c1 = CurrencyRates()
    main_graph = Tk()
    main_graph.option_add("*Font", "consolas 20")
    comment_currncy1 = Label(main_graph, text="เลือกสกุลเงิน")
    comment_currncy1.grid(row=0, column=1)
    comment_currncy1 = Label(main_graph, text="เลือกสกุลเงิน")
    comment_currncy1.grid(row=0, column=5)
    national_graph1 = ttk.Combobox(main_graph)
    national_graph1.grid(row=1, column=1)
    national_graph1['values'] = list(c1.get_rates("").keys())
    national_graph2 = ttk.Combobox(main_graph)
    national_graph2['values'] = list(c1.get_rates("").keys())
    national_graph2.grid(row=1, column=5)

    def Datetime(event):
        date_obj1 = datetime.datetime(2019, 5, 23, 18, 36, 28, 151012)
        date_obj2 = datetime.datetime(2018, 5, 23, 18, 36, 28, 151012)
        date_obj1 = datetime.datetime(2019, 5, 23, 18, 36, 28, 151012)
        date_obj2 = datetime.datetime(2018, 5, 23, 18, 36, 28, 151012)
        date_obj3 = datetime.datetime(2017, 5, 23, 18, 36, 28, 151012)
        date_obj4 = datetime.datetime(2016, 5, 23, 18, 36, 28, 151012)
        date_obj5 = datetime.datetime(2015, 5, 23, 18, 36, 28, 151012)
        date_obj6 = datetime.datetime(2014, 5, 23, 18, 36, 28, 151012)
        date_obj7 = datetime.datetime(2013, 5, 23, 18, 36, 28, 151012)
        date_obj8 = datetime.datetime(2012, 5, 23, 18, 36, 28, 151012)
        date_obj9 = datetime.datetime(2011, 5, 23, 18, 36, 28, 151012)
        date_obj10 = datetime.datetime(2010, 5, 23, 18, 36, 28, 151012)
        date_obj11 = datetime.datetime(2009, 5, 23, 18, 36, 28, 151012)
        date_obj12 = datetime.datetime(2008, 5, 23, 18, 36, 28, 151012)
        date_obj13 = datetime.datetime(2007, 5, 23, 18, 36, 28, 151012)
        date_obj14 = datetime.datetime(2006, 5, 23, 18, 36, 28, 151012)
        date_obj15 = datetime.datetime(2005, 5, 23, 18, 36, 28, 151012)
        national_currency_list = [national_graph1.get(), national_graph2.get()]
        rate = [c1.get_rate(national_currency_list[0], national_currency_list[1], date_obj15),
                c1.get_rate(national_currency_list[0], national_currency_list[1], date_obj14),
                c1.get_rate(national_currency_list[0], national_currency_list[1], date_obj13),
                c1.get_rate(national_currency_list[0], national_currency_list[1], date_obj12),
                c1.get_rate(national_currency_list[0], national_currency_list[1], date_obj11),
                c1.get_rate(national_currency_list[0], national_currency_list[1], date_obj10),
                c1.get_rate(national_currency_list[0], national_currency_list[1], date_obj9),
                c1.get_rate(national_currency_list[0], national_currency_list[1], date_obj8),
                c1.get_rate(national_currency_list[0], national_currency_list[1], date_obj7),
                c1.get_rate(national_currency_list[0], national_currency_list[1], date_obj6),
                c1.get_rate(national_currency_list[0], national_currency_list[1], date_obj5),
                c1.get_rate(national_currency_list[0], national_currency_list[1], date_obj4),
                c1.get_rate(national_currency_list[0], national_currency_list[1], date_obj3),
                c1.get_rate(national_currency_list[0], national_currency_list[1], date_obj2),
                c1.get_rate(national_currency_list[0], national_currency_list[1], date_obj1),]
        year = [2005,
                2006,
                2007,
                2008,
                2009,
                2010,
                2011,
                2012,
                2013,
                2014,
                2015,
                2016,
                2017,
                2018,
                2019]
        plt.style.use('ggplot')
        plt.plot(year, rate, marker='x')

        plt.xlabel('Year')
        plt.ylabel('Currency Exchange Rate')
        plt.show()

    graph_button = Button(main_graph, text="แสดงกราฟ",bg = 'red',fg = 'white')
    graph_button.bind('<Button-1>', Datetime)
    graph_button.grid(row=1, column=0)

def Selectbitcoin(event):
    c1 = CurrencyRates()
    main_bitcoin = Tk()
    main_bitcoin.option_add("*Font", "consolas 20")
    comment_bitcoin1 = Label(main_bitcoin, text="ใส่จำวนวนเงิน")
    comment_bitcoin1.grid(row=0, column=0)
    comment_bitcoin3 = Label(main_bitcoin, text="เลือกสกุลเงิน")
    comment_bitcoin3.grid(row=0, column=5)
    textbow_bitcoin1 = Entry(main_bitcoin)
    textbow_bitcoin1.grid(row=1, column=0)
    textbow_bitcoin1.get()
    lebel_bitcoin2 = Label(main_bitcoin,text='>>'.center(6,' '))
    lebel_bitcoin2.grid(row=1,column=3)
    lebel_bitcoin = Label(main_bitcoin, text='BTC')
    lebel_bitcoin.grid(row=1, column=1)
    national_bitcoin1 = ttk.Combobox(main_bitcoin)
    national_bitcoin1.grid(row=1, column=5)
    national_bitcoin1['values'] = list(c1.get_rates("").keys())
    def Bitcoin(event):
        b = BtcConverter()
        bitcoin_list = [float(textbow_bitcoin1.get()),national_bitcoin1.get()]
        b.convert_btc_to_cur(bitcoin_list[0],bitcoin_list[1])
        resultbitcoin = b.convert_btc_to_cur(bitcoin_list[0],bitcoin_list[1])
        lebel_bitcoin1.configure(text= resultbitcoin)
    forex_button = Button(main_bitcoin, text="คำนวณ",bg = 'red',fg = 'white')
    forex_button.bind('<Button-1>',Bitcoin)
    forex_button.grid(row=2, column=0)
    lebel_bitcoin1 = Label(main_bitcoin, text="ผลลัพธ์".center(10,' '))
    lebel_bitcoin1.grid(row=1, column=4)
    main_bitcoin.mainloop()


main_window = Tk()
main_window.option_add("*Font","consolas 20")
photo_currency = PhotoImage(file="currency-exchange.png")
button1 = Button(main_window,text = 'แปลงเงิน',image=photo_currency,compound = LEFT)
button1.grid(row=0,column=1)
button1.bind('<Button-1>',Selectcurrency)
photo_graph = PhotoImage(file = "graph.png")
button2 = Button(main_window,text = 'กราฟ',image=photo_graph,compound = LEFT)
button2.grid(row=1,column=1)
button2.bind('<Button-1>',Selectgraph)
photo_bitcoin = PhotoImage(file = "bitcoin.png")
button3 = Button(main_window,text = 'Bitcoin',image=photo_bitcoin,compound = LEFT)
button3.grid(row=2,column=1)
button3.bind('<Button-1>',Selectbitcoin)
lebel_name = Label(main_window,text="By Sornram Chareanma",anchor=E)
lebel_name.grid(row=3,column=1)
main_window.mainloop()
