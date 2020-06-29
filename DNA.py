def main():
    file = open("data/rosalind_dna.txt", "r")
    sequence = file.readline()
    print(sequence.count("A"), sequence.count("C"), sequence.count("G"), sequence.count("T"))

if __name__ == "__main__":
    main()