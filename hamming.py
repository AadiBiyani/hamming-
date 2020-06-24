import random
dna = ["A","G","C","T"]
strand_a = ''
strand_b = ''
def distance(strand_a, strand_b):
    differences = 0
    index = 0
    for i in range(10):
        strand_a+=random.choice(dna)
        strand_b+=random.choice(dna)
    print(strand_a)
    print(strand_b)
    for i in range(10):
        if strand_a[index] == strand_b[index]:
            index = index+1
        else:
            differences = differences + 1
            index = index+1
    print ("There are " + str(differences) + " Hamming distances")
    pass

distance(strand_a, strand_b)
