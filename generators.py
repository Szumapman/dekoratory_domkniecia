import random

def generate_integers(n):
    for i in range(n):
        yield i


def generate_text(text):
    words = text.split()
    for word in words:
        yield word


def generate_even_numbers():
    while True:
        number = random.randint(1, 100)
        if number % 2 == 0:
            yield number


if __name__ == '__main__':
    int_generator = generate_integers(5)
    # print(next(int_generator))
    # print(next(int_generator))
    # print(next(int_generator))
    for i in int_generator:
        print(i)

    text_generator = generate_text("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
    for word in text_generator:
        print(word)
    
    even_generator = generate_even_numbers()
    print(next(even_generator))
    print(next(even_generator))
    # for i in range(10):
    #     print(next(even_generator))