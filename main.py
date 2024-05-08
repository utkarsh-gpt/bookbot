def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wordCount = word_count(text)
    letterDict = get_letter_dict(text)
    sortedDict = sort_dict(letterDict)
    print(f"--- Begin report of {book_path} ---")
    for i in range(len(sortedDict)):
        print(f"The '{sortedDict[i]['letter']}' character was found {sortedDict[i]['num']} times",
        end="\n")
    print("--- End Report ---")

def word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_letter_dict(text):
    letter_dict = {}
    lower_text = text.lower().replace(' ','')
    for letter in lower_text:
        if (letter not in letter_dict) and (letter.isalpha()):
            letter_dict[letter] = 1
        elif (letter.isalpha()):
            letter_dict[letter] += 1
    return letter_dict

def sort_key(dict):
    return dict['num']
    
def sort_dict(dict):
    arr = []
    for i in dict:
        arr.append({'letter':i,'num':dict[i]})

    arr.sort(reverse=True, key=sort_key)
    return arr
main()