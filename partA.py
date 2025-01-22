import sys
import re
from collections import defaultdict
Token=""

def tokenize(text_file_path: str) -> list[Token]:
    tokens = []
    regex_pattern = re.compile(r"[A-Za-z0-9]+")
    try:
        with open(text_file_path, "r", encoding="utf-8") as f:
            for line in f:
                match = regex_pattern.findall(line)
                for i in match:
                    tokens.append(i.lower())
        return tokens
    except FileNotFoundError:
        print(f"Error: File was not found.")
        sys.exit(1)

def compute_word_frequencies(tokens: list[Token]) -> dict[Token, int]:
    token_dict = {}
    for i in tokens:
        if i not in token_dict:
            token_dict[i] = 0
        token_dict[i] += 1
    return token_dict

def print_frequencies(frequencies: dict[Token, int]) -> None:
    sorted_dict = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)
    # print(sorted_dict)
    for i, j in sorted_dict:
        print(f"{i} {j}")


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