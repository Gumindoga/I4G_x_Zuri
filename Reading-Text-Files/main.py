# Read text from a file, and count the occurrence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    
    with open(filename) as f:
        words = f.read()
    
    return words


def count_words():

    text = read_file_content("./story.txt")
    text.strip()
    
    words = text.split()
    my_dict = {}

    for i in words:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1

    return my_dict

print(count_words())

