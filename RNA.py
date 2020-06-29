def main():
    file = open("data/rosalind_rna.txt", "r")
    sequence = file.readline()
    print(sequence.replace("T", "U"))

if __name__ == "__main__":
    main()