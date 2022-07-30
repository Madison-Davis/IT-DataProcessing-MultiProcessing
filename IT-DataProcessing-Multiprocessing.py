# Imports
import multiprocessing as mp
from math import log
from math import e
import time
import math

exponentValues = []
percentValues = []
populationChangeValues = []
startingBacteriaPopulation = 10


def exponentialFunction(numbers):
    for number in numbers:
        exponentValues.append(startingBacteriaPopulation * (e ** (0.02 * number)))
def percentGrowthFromOriginal(numbers):
    for number in numbers:
        percentValues.append(number / startingBacteriaPopulation)
def populationGrowthDaily(numbers):
    for number in range(1, len(numbers)):
        populationChangeValues.append(int(numbers[number] - numbers[number - 1]))

if __name__ == "__main__":
    number_list = list(range(30000))
    # Multiprocessing
    start = time.time()
    p1 = mp.Process(target = exponentialFunction, args = (number_list,))
    p2 = mp.Process(target = percentGrowthFromOriginal, args = (exponentValues,))
    p3 = mp.Process(target = populationGrowthDaily, args = (exponentValues,))
    p1.start()
    p2.start()
    p3.start()
    end = time.time()
    print(end - start, ": Multiprocessing")
    # Normal
    start = time.time()
    exponentialFunction(number_list)
    percentGrowthFromOriginal(exponentValues)
    populationGrowthDaily(exponentValues)
    end = time.time()
    print(end - start, ": Normal")
