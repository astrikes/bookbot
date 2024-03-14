def open_book(file_path):
    with open(file_path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def main():
    frankenstein = open_book("books/frankenstein.txt")
    print(frankenstein)
    print(count_words(frankenstein))

main()