def main():
    file = open("data/rosalind_perm.txt", "r")
    number = file.readline()
    number = int(number)

    l = [x+1 for x in range(number)]
    total = 0
    for p in permutations(l):
        total += 1
        print(" ".join(map(str, p)))
    print(total)
    
def permutations(l):
    if len(l) <= 1: 
        yield l
    else:
        for i in range(len(l)):
            for p in permutations(l[:i] + l[i+1:]):
                yield [l[i]] + p

main()