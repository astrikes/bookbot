def open_book(file_path):
    with open(file_path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    lower_string = text.lower()
    alphabet = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }
    for x in alphabet.keys():
        alphabet[x] = lower_string.count(x)      
    return alphabet
    
def sort_occurrence(dictionary):
    # In order to return both key and value you must iterate over items
    # Then use Lambda to tell it to sort by the second element
    sorted_list = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    sorted_dict = {item[0]: item[1] for item in sorted_list}
    return sorted_dict
    

def main():
    frankenstein = open_book("books/frankenstein.txt")
    print("--- Begin report of Frankenstein ---")
    print(f"There are {count_words(frankenstein)} words in the document ")
    occurrence = sort_occurrence(count_letters(frankenstein))
    for x, y in occurrence.items():
        print(f"The {x} character occurred {y} times.")
    print("--- End Report ---")

main()