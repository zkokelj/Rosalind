def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        return -1

    diff = 0
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            diff += 1

    return diff

def main():
    file = open("data/rosalind_hamm.txt", "r")
    s1 = file.readline().rstrip()
    s2 = file.readline().rstrip()
    print(hamming_distance(s1, s2))

if __name__ == '__main__':
    main()