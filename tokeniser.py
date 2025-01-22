import sys
import re
Token=0

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
    pass

def print_frequencies(frequencies: dict[Token, int]) -> None:
    pass

