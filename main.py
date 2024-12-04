def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_count_characters(text)
    sorted_list = sorted_alphabet_list(char_dict)
    report = generate_report(book_path, num_words, sorted_list)
    print(report)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    

def get_num_words(text):
    words = text.split()
    return len(words)

def get_count_characters(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sorted_alphabet_list(dict):
    new_list = []
    for entry in dict:
        if entry.isalpha():
            new_list.append({entry: dict[entry]})

    def sort_on(dict):
        for entry in dict:
            return dict[entry]

    new_list.sort(reverse=True, key=sort_on)
    return new_list


def generate_report(path, num_words, sorted_dict):
    header = f"--- Begin report of {path} ---"
    word_count = f"{num_words} words found in the document"
    character_count = ""
    footer = "--- End report ---"
    
    for dict in sorted_dict:
        for entry in dict:
            character_count += f"\nThe '{entry}' charater was found {dict[entry]} times"

    return '\n'.join([header,word_count,character_count,footer])
    
main()