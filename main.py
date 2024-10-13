def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    
    wc = word_count(text)
    print(f"{wc} words found in the document")
    
    chars = char_count(text)
    sorted_chars = dict_to_list(chars)
    sorted_chars.sort(reverse=True, key=sort_on)
    
    generate_report(book_path, wc, sorted_chars)
    
         
def get_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(content):
    count = len(content.split())
    return count

def char_count(content):
    text = content.lower()
    char_dict = {}
    for char in text:
        if char.isalpha() == True:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
    return char_dict

def dict_to_list(dict):
    lst = []
    for i in dict:
        entry = {"char":i, "num":dict[i]}
        lst.append(entry)
    return lst

def sort_on(dict):
    return dict["num"]

def generate_report(path, wc, chars):
    print(f"----- Begin report on {path} -----")
    print(f"{wc} words found in the document")
    print("")
    
    for i in chars:
        x = i.get("char")
        y = i.get("num")
        print(f"The '{x}' character was found {y} times")
    
    print("----- End Report -----")

main()