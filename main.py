import string

start, end = input("Введіть діапазон літер (наприклад, 'a-c'): ").split('-')
all_letters = string.ascii_letters
print(all_letters[all_letters.index(start):all_letters.index(end)+1])