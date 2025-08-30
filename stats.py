def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def count_words(text):
    words = text.split()
    return len(words)

def chars_dict_to_sorted_list(chars_dict):
    # Convert dictionary to list of dictionaries
    char_list = []
    for char, count in chars_dict.items():
        if char.isalpha():  # Only include alphabetical characters
            char_list.append({"char": char, "num": count})
    
    # Sort by count in descending order
    def sort_on(dict_item):
        return dict_item["num"]
    
    char_list.sort(key=sort_on, reverse=True)
    return char_list
