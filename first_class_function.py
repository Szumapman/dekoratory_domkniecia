# Funkcja przyjmuje inną funkcję jako argument i stosuje ją do listy elementów
def apply_function(func, elements):
    result = []
    for element in elements:
        result.append(func(element))
    return result

# Przykładowe funkcje, które możemy przekazać jako argument
def square(x):
    return x * x

def double(x):
    return x * 2

if __name__ == "__main__":
    # Lista elementów
    numbers = [1, 2, 3, 4, 5]

    # Wywołanie funkcji apply_function z różnymi funkcjami
    squared_numbers = apply_function(square, numbers)
    doubled_numbers = apply_function(double, numbers)

    print("Original numbers:", numbers)
    print("Squared numbers:", squared_numbers)
    print("Doubled numbers:", doubled_numbers)
