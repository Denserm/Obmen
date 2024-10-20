import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def udate_b_label(event):
    code = b_combobox.get()
    name = cur[code]
    b_label.config(text=name)


def udate_b2_label(event):
    code = b2_combobox.get()
    name = cur[code]
    b2_label.config(text=name)


def udate_t_label(event):
    code = t_combobox.get()
    name = cur[code]
    t_label.config(text=name)


def exchange():
    t_code = t_combobox.get()
    b_code = b_combobox.get()
    b2_code = b2_combobox.get()

    if t_code and b_code and b2_code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{b_code}')
            response.raise_for_status()
            data = response.json()
            response2 = requests.get(f'https://open.er-api.com/v6/latest/{b2_code}')
            response2.raise_for_status()
            data2 = response2.json()
            if t_code in data['rates'] and data2['rates']:
                exchange_rate = data['rates'][t_code]
                exchange_rate2 = data2['rates'][t_code]
                t_name = cur[t_code]
                b_name = cur[b_code]
                b2_name = cur[b2_code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2f} {t_name} за 1 {b_name}"'\n'
                                           f"Курс: {exchange_rate2:.2f} {t_name} за 1 {b2_name}")
            else:
                mb.showerror("Ошибка", f"Валюта {t_code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")
    elif t_code and b_code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{b_code}')
            response.raise_for_status()
            data = response.json()
            if t_code in data['rates']:
                exchange_rate = data['rates'][t_code]
                t_name = cur[t_code]
                b_name = cur[b_code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2f} {t_name} за 1 {b_name}")
            else:
                mb.showerror("Ошибка", f"Валюта {t_code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")
    elif t_code and b2_code:
        try:
            response2 = requests.get(f'https://open.er-api.com/v6/latest/{b2_code}')
            response2.raise_for_status()
            data2 = response2.json()
            if t_code in data2['rates']:
                exchange_rate2 = data2['rates'][t_code]
                t_name = cur[t_code]
                b2_name = cur[b2_code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate2:.2f} {t_name} за 1 {b2_name}")
            else:
                mb.showerror("Ошибка", f"Валюта {t_code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")

    else:
        mb.showwarning("Внимание", "Введите код валюты!")



cur = {
    'RUB': 'Российский рубль',
    'EUR': 'Евро',
    'USD': 'Американский доллар',
    'GBP': 'Британский фунт стерлингов',
    'JPY': 'Японская йена',
    'CNY': 'Китайский юань',
    'KZT': 'Казахский танге',
    'UZS': 'Узбекский сум',
    'CHF': 'Швейцарский франк',
    'AED': 'Дирхам ОАЭ',
    'CAD': 'Канадский доллар'
}


window = Tk()
window.title("Курсы обмена валют")
window.geometry("360x400")

Label(text="Базовая валюта").pack(padx=10, pady=10)
b_combobox = ttk.Combobox(values=list(cur.keys()))
b_combobox.pack(padx=10, pady=10)
b_combobox.bind("<<ComboboxSelected>>", udate_b_label)

b_label = ttk.Label()
b_label.pack(padx=10, pady=10)

Label(text="Вторая базовая валюта").pack(padx=10, pady=10)
b2_combobox = ttk.Combobox(values=list(cur.keys()))
b2_combobox.pack(padx=10, pady=10)
b2_combobox.bind("<<ComboboxSelected>>", udate_b2_label)

b2_label = ttk.Label()
b2_label.pack(padx=10, pady=10)

Label(text="Целевая валюта").pack(padx=10, pady=10)
# cur = ['RUB', 'EUR', 'GBP', 'JPY', 'CNY', 'KZT', 'UZS', 'CHF', 'AED', 'CAD']
t_combobox = ttk.Combobox(values=list(cur.keys()))
t_combobox.pack(padx=10, pady=10)
t_combobox.bind("<<ComboboxSelected>>", udate_t_label)

t_label = ttk.Label()
t_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()

