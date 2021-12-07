
def dodawanie(x, y):
    return x + y

def odejmowanie(x, y):
    return x - y

def mnozenie(x, y):
    return x * y

def dzielenie(x, y):
    return x / y


print("1.dodawanie")
print("2.odejmowanie")
print("3.mnożenie")
print("4.dzielenie")

while True:

    choice = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")


    if choice in ('1', '2', '3', '4'):
        num1 = float(input("podaj pierwszą liczbę: "))
        num2 = float(input("podaj drugą liczbę: "))

        if choice == '1':
            print(num1, "+", num2, "=", dodawanie(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", odejmowanie(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", mnozenie(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", dzielenie(num1, num2))
        


