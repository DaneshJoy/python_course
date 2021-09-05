from time import sleep

tax_global = 0.09

def final_price(price, tax=tax_global):
    _tax = price * tax
    price_out = price + _tax
    return price_out

def typeit(text, delay=0.1):
    for c in text:
        print(c, end='')
        sleep(delay)
    print()

price = int(input('Enter product price: '))

price2 = final_price(price=price)

price3 = final_price(price=price, tax=0.12)

out2 = f'Final price is {price2}'
out3 = f'Final price is {price3}'

typeit(out2)
typeit(out3, delay=0.3)


