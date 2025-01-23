import sys
import re
Token=""

def tokenize(text_file_path: str) -> list[Token]:
    ''' This function tokenises the file items and add em to the list.
        we also use the open fn to handel the case of automatically closing the file, also enforcing uts-8 encoding.
        I used 2 exceptions one in case file is not found/ name is wrong, and non-unicode text is read.
        I also used a simple regex statement finding letters like (a-z), (A-Z), (0-9), (+, repetition operator)
        Here Time complexity appears to be o(n+m), where n is total text length and m is number of lines, but since
        we can't have more tokens than characters, we can say Time complexity is o(n).
    '''
    tokens = [] # o(1)
    regex_pattern = re.compile(r"[A-Za-z0-9]+") # o(1)
    try:
        with open(text_file_path, "r", encoding="utf-8") as f: # o(1)
            for line in f: # o(m)
                match = regex_pattern.findall(line) # o(n)
                for i in match: # o(token)
                    tokens.append(i.lower())
        return tokens # o(1)
    except FileNotFoundError:# o(1)
        print("Error: File was not found.") # o(1)
        sys.exit(1)
    except UnicodeDecodeError:# o(1)
        print("Error: Not Unicode file.") # o(1)
        sys.exit(1)


def compute_word_frequencies(tokens: list[Token]) -> dict[Token, int]:
    '''This function uses the previously computed tokenised list and add em to a map/dict.
        Here Time complexity is o(n), where n is no. of tokens in the list, and we run it n times
        to add tokens in the dict.
    '''
    token_dict = {} # o(1)
    for i in tokens: # o(n)
        if i not in token_dict: # o(1)
            token_dict[i] = 0 # o(1)
        token_dict[i] += 1 # o(1)
    return token_dict # o(1)

def print_frequencies(frequencies: dict[Token, int]) -> None:
    ''' This function prints the sorted token in a  format "i -> j", we sort using the sorted function
        that has the time complexity of o(nlog(n)) and dominates the function. Hence, the time complexity of
        the function is o(nlog(n)). Here n is items in the dictionary
    '''
    sorted_dict = sorted(frequencies.items(), key=lambda item: item[1], reverse=True) # o(nlog(n))
    # print(sorted_dict)
    for i, j in sorted_dict:  # o(n)
        print(f"{i} -> {j}") # o(1)


def main():
    if len(sys.argv) != 2:
        print("Error: Wrong Argument")
        sys.exit(1)

    tokens = tokenize(sys.argv[1])
    # print(tokens)
    token_dict = compute_word_frequencies(tokens)
    print_frequencies(token_dict)

if __name__ == "__main__":
    main()