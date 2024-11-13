from collections import defaultdict

def count_chars(text):
    text = text.lower()
    d = defaultdict(int)
    for c in text:
        d[c] += 1
    return d

def count_words(text):
    return len(text.split())


def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        print(file_contents)

        n = count_words(file_contents)
        print(f'In dem Buch sind {n} Wörter.')

        d = count_chars(file_contents)
        for k in d.keys():
            if k == " ":    print(f'space   ---> {d[k]}')
            elif k == '\n': print(f'newline ---> {d[k]}')
            else:           print(f'{k}       ---> {d[k]}')


main()

