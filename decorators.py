from functools import lru_cache
import time


passwords = {
    "user1": "123456",
    "user2": "abcdef",
}


# Funkcja cached, która przechowuje wyniki funkcji w słowniku
def cached(fn):
    _cache = {}
    def wrapper(*args):
        if args not in _cache:
            _cache[args] = fn(*args)
        return _cache[args]
    return wrapper


# Dekorator log_time, która mierzy czas wykonania funkcji
def log_time(fn):
    def wrapper(*args):
        start_time = time.time()
        result = fn(*args)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Function took {duration} seconds.")
        return result
    return wrapper

# Dekorator log_to_file, który loguje wywołania funkcji do pliku
def log_to_file(fn):
    def wrapper(*args):
        with open("fibonacci_logs.txt", "a") as f:
            f.write(f"Function {fn.__name__} called with args {args}\n")
        return fn(*args)
    return wrapper


# Dekorator z parametrem, który pozwala na wybór nazwy pliku, do którego będą logowane wywołania funkcji
def log_to_file_with_parameter(filename):
    def decorator(fn):
        def wrapper(*args):
            with open(filename, "a") as f:
                f.write(f"Function {fn.__name__} called with args {args}\n")
            return fn(*args)
        return wrapper
    return decorator


@log_to_file_with_parameter("fibonacci_logs_custom.txt")
@cached
def fib(n):
    if n in [0,1]: # Warunek sprawdzający, czy n jest równe 0 lub 1.
        return n # Jeśli tak, zwracamy n.
    return fib(n-1) + fib(n-2) # Jeśli nie, zwracamy sumę dwóch poprzednich wyrazów ciągu Fibonacciego

@cached
def fib_optimized(n):
    '''
    Implementacja funkcji w ten sposób oblicza wartość ciągu Fibonacciego dla dowolnej liczby n poprzez iteracyjne obliczenia, unikając rekurencji i potencjalnych problemów z głęboką rekursją.
    '''
    if n <= 1: # Warunek sprawdzający, czy n jest mniejsze lub równe 1.
        return n # Jeśli tak, zwracamy n.
    a, b = 0, 1 # Inicjalizacja dwóch zmiennych a i b na początkowe wartości 0 i 1. Będziemy używać tych zmiennych do obliczania kolejnych wartości ciągu Fibonacciego
    for _ in range(2, n + 1): # Rozpoczynamy pętlę for, która będzie obliczać kolejne wartości ciągu Fibonacciego od 2 do n (włącznie)
        a, b = b, a + b # W każdej iteracji pętli for, zmienna a przyjmuje wartość b, a zmienna b przyjmuje wartość a + b. Dzięki temu możemy obliczyć kolejne wartości ciągu Fibonacciego
    return b # Zwracamy wartość b, która jest ostatnią wartością ciągu Fibonacciego

# @log_to_file
# @cached
# # Zdefiniuj funkcję _fib, która będzie rekurencyjnie obliczać n-ty wyraz ciągu Fibonacciego
# def _fib(n):
#     if n in [0,1]:
#         return n
#     return _fib(n-1) + _fib(n-2)

# @log_time
# # Zdefiniuj funkcję fib, która wywoła funkcję _fib
# def fib(n):
#     return _fib(n)

# fib = log_time(fib)

# def custom_cache(func):
#     cache = {}  # Dictionary to store cached results

#     def wrapper(n):
#         if n not in cache:
#             result = func(n)  # Call the original function
#             cache[n] = result  # Store the result in the cache
#         return cache[n]  # Return the cached result

#     return wrapper

# @custom_cache
# def factorial(n):
#     if n < 0:
#         return "Factorial is not defined for negative numbers"
#     elif n in (0, 1):
#         return 1
#     else:
#         return n * factorial(n - 1)

def authenticated_sum(a, b, username, passwords):
    # passwords = {"test": "4321"}
    if passwords.get(username) == password:
        return a + b
    else:
        print("Authentication error: Incorrect password.")


def auth(fn):
    def wrapper(*args):
        # passwords = {"test": "4321"}
        username = input("Nazwa użytkownika: ")
        pwd = input("Hasło: ")
        if passwords.get(username) == pwd:
            return fn(*args)
        else:
            print("Błąd uwierzytelniania: Nieprawidłowe hasło.")
    return wrapper


def add(a, b):
    return a + b


@auth
def add_with_auth(a, b):
    return a + b


if __name__ == '__main__':
    # result = log_time(fib)
    # result_ex = fib_optimized(850)
    # print(result_ex)
    # result_factorial = factorial(1000)
    # print(result_factorial)
    username = input("Username: ")
    password = input("Password: ")
    result = authenticated_sum(5, 10, username, passwords)
    print(result)
    # result_three = add_with_auth(1, 2)
    # result_4 = add_with_auth()
    # print(result)
    # print(result_two)
    # print(result_three)
    # print(result_4)
    # print(f"Result with auth: {result_four}")