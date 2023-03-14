#Standard Deviation - standard_deviatiom(numbers) - numbers = list of values
import math

def standard_deviation(numbers):
    n = len(numbers)
    mean = sum(numbers) / n
    deviations = [(x - mean) ** 2 for x in numbers]
    variance = sum(deviations) / (n - 1)
    std_dev = math.sqrt(variance)
    return std_dev

#Mean - mean(numbers) - numbers = list of values
def mean(numbers):
    mean = sum(numbers) / len(numbers)
    return mean

#Median - median(numbers) - numbers = list of values
def median(numbers):
    n = len(numbers)
    sorted_numbers = sorted(numbers)
    if n % 2 == 0:
        median1 = sorted_numbers[n//2]
        median2 = sorted_numbers[n//2 - 1]
        median = (median1 + median2) / 2
    else:
        median = sorted_numbers[n//2]
    return median

