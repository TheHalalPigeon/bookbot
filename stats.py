def get_num_words(text):
    return len(text.split())

def count_chars(text):
    char_count = {}
    
    for char in text:
        converted_char = char.lower()
        if converted_char not in char_count:
            char_count[converted_char] = 0
        char_count[converted_char] += 1
        
    return char_count

def sort_chars(char_dict):
    def sort_on(char):
        return char["count"]
    
    char_list = []
    for char in char_dict:
        char_list.append({ "name": char, "count": char_dict[char] })
        
    char_list.sort(reverse=True, key=sort_on)
    return char_list