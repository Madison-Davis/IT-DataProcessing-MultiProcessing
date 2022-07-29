# Imports
import multiprocessing
import time
import math


# Variables
def split(word):
    return [char for char in word]
data = "ATGGAAACACCCTTCTACGGCGATGAGGCGCTGAGCGGCCTGGGCGGCGGCGTCAGTAGCAGTGGCGGCGGTGGTAGCTTCGCGTCCCCGGGTCGCCTGTTTCCCGGGGCGCCCCCGACGGCGGCGACTGGCAGCATGATGAAGAAAGACGCGCTGACGCTGAGCCTGAGCGAGCAGGTGGCGGCGGCGCTCAAGCCCGCGGCCGCGCCGCCCCCGGCCCCCCTGCGCACCGACGGCGCCCCAGGCACGGCGCCCCCCGACGGCCTACTCTCCTCGCCCGACCTGGGGCTGCTCAAGCTCGCCTCGCCCGAGCTCGAGCGCCTAATCATCCAGTCCAACGGGCTGGTCACCACCACGCCGACGAGCACTCAGTTCCTCTACCCCAAGGTGGCGGCCAGCGAGGAGCAGGAGTTTGCCGAGGGCTTCGTCAAGGCCCTGGAAGACTTGCACAAGCAGAACCAGCTGGGCACGGGCGCGGCCTCGGCAGCCGCGGCCGCCGGAGGACCCTCGGGCACGGCTGCGGGCGCCGCGCCTCCTGGCGAACTGGCCCCAGCGGCAGCCACGCCCGAGGCGCCCGTCTACGCGAACCTGAGCAGCTACGCGGGCGGCACCGGGGGTTCGGGGGGTGCTGCGACGGTCGCCTTCGCCGCGGAGCCTGTGCCCTTCCCTCCGCCACCGCCCCCAGGCGCGCTGGGGCCGCCCCGCCTGACCGCGCTCAAGGATGAGCCGCAGACGGTGCCCGACGTGCCAAGCTTCGGCGAGAGCCCGCCGTTGTCGCCCATCGACATGGACACGCAGGAGCGCATTAAGGCGGAGCGCAAGCGGCTGCGCAACCGCATCGCTGCCTCTAAGTGCCGCAAGCGCAAGCTGGAGCGCATCTCGCGCCTCGAGGAGAAAGTGAAGACGCTCAAGAGCCAGAACACGGAGCTGGCGTCCACAGCGAGCCTGCTGCGCGAGCAGGTGGCGCAGCTCAAGCAGAAGGTCCTCAGCCACGTCAACAGCGGCTGCCAGCTGCTGCCCCAGCACCAGGTGTCCGCGTACTGAATGTGCACTAAAATGGAACAGCCCTTCTACCACGACGACTCATACGCAGCGGCGGGATACGGCCGGGCTCCGGGCGGCCTTTCTCTACACGACTACAAACTCCTGAAACCCAGCCTGGCGCTCAACCTGGCCGACCCCTACCGAAGTCTCAAAGCCCCCGGGGCGCGGGGCCCGGGACCAGAGGGCAGCGGTGGCAGCAGCTACTTTTCCGGCCAGGGTTCGGACACAGGCGCGTCGCTCAAGCTTGCCTCATCGGAGCTGGAGCGCCTGATCGTCCCCAACAGCAACGGAGTGATCACGACGACACCCACGCCCCCGGGACAGTACTTTTACCCCCGCGGGGGAGGCAGCGGCGGAGGTGCGGGGGGCGCCGGGGGCGGTGTCACCGAGGAGCAGGAGGGCTTCGCAGACGGCTTTGTCAAAGCGCTGGACGACCTGCACAAGATGAACCACGTGACGCCCCCCAACGTGTCCCTGGGCGCCAGCTCGGGGCCCCCGGCTGGGCCCGGGGGCGTCTACGCCGGCCCGGAGCCACCTCCAGTCTACACCAACCTCAACAGCTATTCCCCAGCCTCTGCGCCCTCTGGAGGCGCCGGGGCCGCCGTCGGGACTGGGAGCTCGTACCCGACGGCCACCATCAGCTACCTCCCACACGCGCCACCCTTCGCTGGCGGCCACCCGGCGCAACTGGGCCTGGGCCGAGGAGCCTCCACCTTCAAGGAGGAACCGCAGACCGTGCCTGAGGCGCGCAGCCGCGACGCCACGCCACCGGTGTCCCCCATCAATATGGAAGACCAGGAGCGCATCAAAGTGGAGCGCAAGAGGCTGCGGAACCGGCTGGCGGCCACCAAGTGCCGGAAGCGGAAGCTGGAGCGCATCGCGCGCCTGGAGGACAAGGTGAAGACACTCAAGGCCGAGAACGCGGGGCTGTCGAGCACTGCTGGGCTCCTCCGGGAGCAGGTGGCCCAGCTCAAACAGAAGGTCATGACCCACGTCAGCAACGGCTGCCAGCTGCTGCTCGGGGTCAAGGGACACGCCTTCTGA"
CanineDNA = split(data)
nucleotides = {}
nucleotideCombinations = []
stripLength = []
A = []
T = []
G = []
C = []


# Functions
def numberNucleotides(dataFile):
    for dataPoint in dataFile:
        if dataPoint == "A":
            A.append(dataPoint)
        elif dataPoint == "T":
            T.append(dataPoint)
        elif dataPoint == "G":
            G.append(dataPoint)
        elif dataPoint == "C":
            C.append(dataPoint)
        nucleotides.update({"A": len(A), "T": len(T), "G": len(G), "C": len(C)})
def lengthDNA(dataFile):
    stripLength.append(len(dataFile))
def combinationsNucleotides(dataFile):
    splitData = [dataFile[i:i + 2] for i in range(0, len(dataFile), 2)]
    for dataPoint in splitData:
        if dataPoint not in nucleotideCombinations:
            nucleotideCombinations.append(dataPoint)
if __name__ == "__main__": # must for multiprocessing, lest IDE may crash
    # Multiprocessing
    p1 = multiprocessing.Process(target = numberNucleotides, args = (CanineDNA,))
    p2 = multiprocessing.Process(target = lengthDNA, args = (CanineDNA,))
    p3 = multiprocessing.Process(target = combinationsNucleotides, args = (data,))
    start = time.time()
    p1.start()
    p2.start()
    p3.start()
    end = time.time()
    print(end - start, " seconds")
    # Normal
    start = time.time()
    numberNucleotides(CanineDNA)
    lengthDNA(CanineDNA)
    combinationsNucleotides(data)
    end = time.time()
    print(end - start, " seconds")


# Results
print(stripLength)
print(nucleotides)
print(nucleotideCombinations)