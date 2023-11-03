def error_handler(func):
    def wrapper(*args):
        try:
            return func(*args) # *args - to wszystkie argumenty, które przyjmie funkcja
        # except Exception as e:
            # print(f"Error caught: {e} in function {func.__name__} with values {args}")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error caught: {e} in function {func.__name__} with values {args}")
            return "Argument(s) are invalid"
        except FileNotFoundError:
            print(f"Error caught: File not found in function {func.__name__} with values {args}")
            return "File not found"
    return wrapper

@error_handler
def divide(a, b):
    return a / b

@error_handler
def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

@error_handler
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()


if __name__ == '__main__':
    # DIVIDE
    # Przykład uruchomienia funkcji bez błędu
    result = divide(10, 2)
    print(result)
    # Przykład uruchomienia funkcji z błędem
    result2 = divide(10, 0)
    print(result2)

    # # CALCULATE AVERAGE
    # # Przykład uruchomienia funkcji bez błędu
    # result = calculate_average([])
    # print(result)
    # # Przykład uruchomienia funkcji z błędem
    # result = calculate_average([1, 2, 3, 4, 5])
    # print(result)

    # READ FILE
    # Przykład uruchomienia funkcji bez błędu
    # result = read_file('data.txt')
    # print(result)
    # Przykład uruchomienia funkcji z błędem
    # result = read_file('data2.txt')
    # print(result)
