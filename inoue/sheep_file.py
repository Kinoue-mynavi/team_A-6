import sys

first_arg = sys.argv[1]

if __name__ == '__main__':
    text = ""

    for i in range(int(first_arg)):
        count = i + 1
        text = text + f"ひつじが{count}匹\n"

    text_file = open('sheep.txt', 'w', encoding='UTF-8')
    text_file.write(text)


