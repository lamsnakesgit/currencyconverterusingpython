import tkinter as tk
# import requests #double

root = tk.Tk()
var1 = tk.StringVar(root)
var2 = tk.StringVar(root)
var1.set("currency")
var2.set("currency")

def Realtimeconversion():

    import requests, json
    from_currency = var1.get()
    to_currency = var2.get()

    api_key = "Your_Api_Key"

    base_url = r"https://www.alphavantage.co/query?function = CURRENCY_EXCHANGE_RATE"
    main_url = base_url + "&from_currency =" + from_currency + "&to_currency =" + to_currency + "&apikey =" + api_key

    req_ob = requests.get(main_url)

    result = req_ob.json()

    Exchange_Rate = float(result["Realtime Currency Exchange Rate"]
            ['5. Exchange Rate'])

    #amount - float(Amount1_field.get())
    amount = float(Amount1_field.get())

    new_amount = round(amount * Exchange_Rate, 3)

    Amount2_field.insert(0, str(new_amount))

def clear_all():
    Amount1_field.delete(0, tk.END)
    Amount2_field.delete(0, tk.END)
               #     END)#up the variable

if __name__ == "__main__":
    root.configure(background = 'light green')

    root.geometry("400x175")

    headlabel = tk.Label(root, text = 'welcome to Real Time Currency Convert!!',
            fg = 'black', bg = 'red')
    label1 = tk.Label(root, text = "Amount :",
            fg = 'black', bg = 'dark green')
    label2 = tk.Label(root, text = "From Currency",
            fg = 'black', bg = 'dark green')
    label3 = tk.Label(root, text = "To currency",
            fg = 'black', bg = 'dark green')
    label4 = tk.Label(root, text = "Converted Amount :",
            fg = 'black', bg = 'dark green')

    headlabel.grid(row = 0, column = 1)
    label1.grid(row = 1, column = 0)
    label2.grid(row = 2, column = 0)
    label3.grid(row = 3, column = 0)
    label4.grid(row = 5, column = 0)

    Amount1_field =  tk.Entry(root)
    Amount2_field = tk.Entry(root)

    Amount1_field.grid(row = 1, column = 1, ipadx = "25")
    Amount2_field.grid(row = 5, column = 1, ipadx = "25")

    CurrencyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"]

    FromCurrency_option = tk.OptionMenu(root, var1, *CurrencyCode_list)
    ToCurrency_option = tk.OptionMenu(root, var2, *CurrencyCode_list)

    FromCurrency_option.grid(row = 2, column = 1, ipadx = 10)
    ToCurrency_option.grid(row = 3, column = 1, ipadx = 10)

    button1 = tk.Button(root, text = "Convert", bg = "red",fg='black',
            command = Realtimeconversion)
    #lat touch
    ##button2.grid(row = 6, column =  1) #fail syntx
    button1.grid(row = 5, column = 1)
    button2 = tk.Button(root, text = "Clear", bg = "blue", fg = "yellow",
            command = clear_all)
    # no grid = no show
    button2.grid(row = 6, column = 1)
    root.mainloop()
