# PRZYKŁAD 1
# Funkcja z domknięciem
def outer_function_closures(x):
    def inner_function(y):
        return x + y
    return inner_function

# closure = outer_function_closures(10) # Utworzenie domknięcia
# result = closure(5) # Wywołanie funkcji wewnątrz domknięcia
# print(result)  # Wyświetli: 15

# ---------------------------------------------------------- #

# PRZYKŁAD 2
def greeter(name):
    def greeting():
        return f"Hello, {name}!"

    return greeting

# # Create closures
# greet_alice = greeter("Adrian")
# greet_bob = greeter("Jan")

# # Przykład użycia
# message1 = greet_alice()
# print(message1)  # Wyświetli: Hello, Alice!
# message2 = greet_bob()
# print(message2)  # Wyświetli: Hello, Bob!


# ---------------------------------------------------------- #

# PRZYKŁAD 3
def counter():
    count = 0 # Zmienna lokalna
    def increment():
        nonlocal count # Umożliwia modyfikację zmiennej lokalnej
        count += 1 # Zwiększenie wartości zmiennej lokalnej
        return count

    return increment # Zwrócenie funkcji wewnętrznej

# Utworzenie domknięcia
increment = counter() # inkrementacja = inkrementuj

print(increment())  # 1
print(increment())  # 2
print(increment())  # 3


# ---------------------------------------------------------- #

# PRZYKŁAD 4
def generate_sum(x):
    def add_numers(y):
        return x + y
    return add_numers

add_5 = generate_sum(5)
print(add_5(3))  # 8
print(add_5(10))  # 15
print(add_5(15))  # 20


# ---------------------------------------------------------- #

# PRZYKŁAD 5
def open_txt_file(nazwa_pliku):
    plik = open(nazwa_pliku, 'r')
    print(f"Plik {nazwa_pliku} został otwarty")
    print(f"Zawartość pliku {nazwa_pliku}:\n\n {plik.read()}\n\n")

    def close_txt_file():
        plik.close()
        print(f"Plik {nazwa_pliku} został zamknięty")

    return close_txt_file

# Utworzenie domknięcia
zamknij = open_txt_file('data.txt')

# Po zakończeniu pracy z plikiem można go zamknąć wywołując
zamknij()
