import sys
import partA

def main():
    '''
        time complexity of this function is :o(n1+n2)log(n1+n2)
        n1 =  no. of character in file 1, n2 =  no. of character in file 1,
        since we are kind of doing sorted for common token, it should be o(n1+n2) + o(n1+n2)log(n1+n2)
        which simplifies to be just : o(n1+n2)log(n1+n2)
    '''
    if len(sys.argv) != 3:
        print("Error: Wrong Argument, type like <python3> <partB.py> <file1.txt> <file2.txt>")
        sys.exit(1)
    tokens1 = partA.tokenize(sys.argv[1]) # o(n1)
    tokens2 = partA.tokenize(sys.argv[2]) # o(n2)

    set1 = set(tokens1) # o(n1)
    set2 = set(tokens2) # o(n2)
    common_tokens = set1.intersection(set2) # o(n1+n2)

    print(f"No. of common tokens: {len(common_tokens)}") # o(1)
    for token in sorted(common_tokens): # sorted is o(log(n)), so here it becomes : o(n1+n2)log(n1+n2)
         print(token) # o(1)


if __name__ == "__main__":
    main()