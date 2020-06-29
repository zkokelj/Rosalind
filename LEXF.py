from itertools import product

def readFile():
    file = open("data/rosalind_lexf.txt", "r")
    string = file.readline().rstrip().replace(" ", "")
    length = file.readline().rstrip()
    return (string, length)


if __name__ == "__main__":
    string, length = readFile()
    result_file = open("results/lexf_result.txt", "a")
    for item in product(string, repeat=int(length)):
        a = "".join(item) +"\n"
        result_file.write(a)