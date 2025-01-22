import sys
import partA

def main():
    if len(sys.argv) != 3:
        print("Error: Wrong Argument")
        sys.exit(1)
    tokens1 = partA.tokenize(sys.argv[1])
    tokens2 = partA.tokenize(sys.argv[2])

    set1 = set(tokens1)
    set2 = set(tokens2)
    common_tokens = set1.intersection(set2)

    print(f"No. of common tokens: {len(common_tokens)}")
    for token in sorted(common_tokens):
         print(token)


if __name__ == "__main__":
    main()