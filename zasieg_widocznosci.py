from closures import outer_function_closures

# Zasieg lokalny
def my_function():
    x = 100  # Zmienna lokalna
    print(x)


# Zasieg zagniezdzony
z = 10  # Zmienna globalna
def outer_function():
    z = 20  # Zmienna zagnieżdżona
    def inner_function():
        print(z)  # Ma dostęp do zmiennej x z zasięgu zagnieżdżonego
    inner_function()


# Zasieg globalny
y = 50  # Zmienna globalna

def my_function():
    print(y)  # Ma dostęp do zmiennej y z zasięgu globalnego


if __name__ == '__main__': # Kod, który będzie wykonany tylko wtedy, gdy ten skrypt jest uruchamiany jako główny program
    closure2 = outer_function_closures(20)
    result2 = closure2(7)
    print(result2)  # Wyświetli: 27
    # my_function()
    # print(y) 
    # print(x)  # Spowoduje błąd, ponieważ x jest widoczne tylko wewnątrz funkcji.
    # outer_function()  # Wyświetli: 20
